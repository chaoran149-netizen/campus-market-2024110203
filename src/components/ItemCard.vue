<script setup lang="ts">
import { computed } from 'vue'
import { useFavoriteStore } from '@/stores/favorite'
import type { FavoriteItem } from '@/stores/favorite'

const props = defineProps<{
  type: 'trade' | 'lostFound' | 'groupBuy' | 'errand'
    data: Record<string, unknown>
}>()

const favoriteStore = useFavoriteStore()
const fallbackImg = 'https://images.unsplash.com/photo-1586769852044-692d6e3703f0?w=400&h=300&fit=crop'

const favId = computed(() => Number(props.data.id))
const isFav = computed(() => favoriteStore.isFavorited(favId.value))

function toggleFav(e: Event) {
  e.preventDefault()
  e.stopPropagation()
  const item: FavoriteItem = {
    id: favId.value,
    type: props.type,
    title: (props.data.title || props.data.itemName || '') as string,
    price: (props.data.price || props.data.reward) as number | undefined,
    campus: props.data.campus as string,
    addedAt: new Date().toLocaleString(),
  }
  favoriteStore.toggleFavorite(item)
}
</script>

<template>
  <!-- Trade Card -->
  <router-link v-if="type === 'trade'" :to="'/detail/' + data.id" class="image-card">
    <div class="card-img-wrap">
      <img :src="(data.image as string) || fallbackImg" :alt="data.title as string" loading="lazy" />
      <span v-if="data.status === 'closed'" class="corner-badge sold">已售</span>
      <button class="fav-btn" :class="{ active: isFav }" @click="toggleFav">{{ isFav ? '❤️' : '🤍' }}</button>
    </div>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <div class="price-row">
        <span class="card-price">¥{{ data.price }}</span>
        <span class="card-meta">{{ data.campus }}</span>
      </div>
      <div class="tag-row">
        <span class="tag">{{ data.category }}</span>
        <span class="tag">{{ data.condition }}</span>
      </div>
    </div>
  </router-link>

  <!-- LostFound Card -->
  <div v-else-if="type === 'lostFound'" class="image-card">
    <div class="card-img-wrap">
      <img :src="(data.image as string) || fallbackImg" :alt="data.itemName as string" loading="lazy" />
      <span class="corner-badge" :class="data.type">{{ data.type === 'lost' ? '寻物' : '拾取' }}</span>
      <button class="fav-btn" :class="{ active: isFav }" @click="toggleFav">{{ isFav ? '❤️' : '🤍' }}</button>
    </div>
    <div class="card-body">
      <h4>{{ data.itemName }}</h4>
      <p class="card-desc">{{ data.description }}</p>
      <div class="tag-row">
        <span class="tag">{{ data.location }}</span>
        <span class="tag">{{ data.time }}</span>
        <span class="status-dot-sm" :class="data.status"></span>
      </div>
    </div>
  </div>

  <!-- GroupBuy Card -->
  <div v-else-if="type === 'groupBuy'" class="image-card">
    <div class="card-img-wrap">
      <img :src="(data.image as string) || fallbackImg" :alt="data.title as string" loading="lazy" />
      <span class="corner-badge group">{{ data.type }}</span>
      <button class="fav-btn" :class="{ active: isFav }" @click="toggleFav">{{ isFav ? '❤️' : '🤍' }}</button>
    </div>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <div class="progress-mini">
        <span class="prog-bar"><span class="prog-fill" :style="{ width: (Number(data.currentCount) / Number(data.targetCount) * 100) + '%' }"></span></span>
        <span class="prog-text">{{ data.currentCount }}/{{ data.targetCount }} 人</span>
      </div>
      <div class="tag-row">
        <span class="tag">{{ data.campus }}</span>
        <span class="tag">{{ data.deadline }}</span>
      </div>
    </div>
  </div>

  <!-- Errand Card -->
  <div v-else-if="type === 'errand'" class="image-card">
    <div class="card-img-wrap">
      <img :src="(data.image as string) || fallbackImg" :alt="data.title as string" loading="lazy" />
      <span class="corner-badge errand">{{ data.taskType }}</span>
      <button class="fav-btn" :class="{ active: isFav }" @click="toggleFav">{{ isFav ? '❤️' : '🤍' }}</button>
    </div>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <p class="card-desc">{{ data.description }}</p>
      <div class="price-row">
        <span class="card-price">¥{{ data.reward }}</span>
        <span class="status-dot-sm" :class="data.status"></span>
        <span class="card-meta">{{ data.deadline }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ── 统一图片卡片 ── */
.image-card {
  display: flex; flex-direction: column;
  border-radius: var(--radius-lg); background: var(--color-surface);
  overflow: hidden; border: 1px solid var(--color-border);
  transition: all var(--transition); color: inherit; text-decoration: none; cursor: pointer;
}
.image-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); border-color: var(--color-border-hover); }

/* 图片区 (固定 4:3 比例) */
.card-img-wrap {
  position: relative; width: 100%; padding-top: 75%; overflow: hidden; background: var(--color-border-light);
}
.card-img-wrap img {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;
  transition: transform var(--transition-slow);
}
.image-card:hover .card-img-wrap img { transform: scale(1.05); }

/* 角标 */
.corner-badge {
  position: absolute; top: 8px; right: 8px;
  padding: 4px 10px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;
  color: #fff;
}
.corner-badge.sold   { background: rgba(0,0,0,0.6); }
.corner-badge.lost   { background: #D97706; }
.corner-badge.found  { background: #059669; }
.corner-badge.group  { background: var(--color-primary); }
.corner-badge.errand { background: #7C3AED; }

/* 收藏按钮 */
.fav-btn {
  position: absolute; top: 8px; left: 8px;
  width: 32px; height: 32px; border: none; border-radius: 50%;
  background: rgba(255,255,255,0.85); font-size: 16px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all var(--transition-fast); line-height: 1; padding: 0;
}
.fav-btn:hover { background: #fff; transform: scale(1.1); }
.fav-btn.active { background: #FEE2E2; }

/* 内容区 */
.card-body { padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; }
.card-body h4 {
  font-size: 14px; font-weight: 600; color: var(--color-text);
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
  overflow: hidden; line-height: 1.4;
}

/* 价格行 */
.price-row { display: flex; align-items: baseline; gap: 8px; }
.card-price { font-size: 18px; font-weight: 700; color: #F43F5E; flex-shrink: 0; }
.card-meta { font-size: 12px; color: var(--color-text-muted); flex: 1; text-align: right; }

/* 描述 */
.card-desc { font-size: 12px; color: var(--color-text-secondary); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; line-height: 1.4; }

/* 标签行 */
.tag-row { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.tag { padding: 2px 8px; border-radius: var(--radius-full); font-size: 11px; font-weight: 500; background: var(--color-border-light); color: var(--color-text-secondary); }

/* 迷你进度条 */
.progress-mini { display: flex; align-items: center; gap: 8px; }
.prog-bar { flex: 1; height: 6px; background: var(--color-border-light); border-radius: var(--radius-full); overflow: hidden; position: relative; }
.prog-fill { display: block; height: 100%; background: var(--color-primary); border-radius: var(--radius-full); transition: width var(--transition-slow); }
.prog-text { font-size: 12px; color: var(--color-text-secondary); white-space: nowrap; }

/* 迷你状态点 */
.status-dot-sm { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.status-dot-sm.open { background: #F59E0B; }
.status-dot-sm.taken { background: var(--color-primary); }
.status-dot-sm.done { background: #10B981; }
.status-dot-sm.closed { background: #6B7280; }
</style>
