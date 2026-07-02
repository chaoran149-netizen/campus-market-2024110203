<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { computed } from 'vue'
import { useFavoriteStore } from '@/stores/favorite'
import type { FavoriteItem } from '@/stores/favorite'

const route = useRoute()
const router = useRouter()
const favoriteStore = useFavoriteStore()

const items: Record<number, { title: string; type: string; campus: string; price: number; emoji: string; desc: string; tags: string[] }> = {
  1: { title: '二手教材 - 高等数学', type: '二手交易', campus: '主校区', price: 25, emoji: '📚', desc: '大二高数教材，几乎全新，只有前两章有笔记。需要自取，主校区3号楼。', tags: ['九成新', '可议价', '自取'] },
  2: { title: '蓝牙耳机 九成新', type: '二手交易', campus: '东校区', price: 80, emoji: '🎧', desc: '用了两个月，充电仓完好，音质很好。附赠一条充电线。', tags: ['九成新', '带配件'] },
  3: { title: '丢失校园卡 - 李**', type: '失物招领', campus: '主校区', price: 0, emoji: '🪪', desc: '在主校区食堂捡到校园卡一张，失主请联系认领。', tags: ['已捡到', '食堂'] },
  4: { title: '奶茶拼单！一点点', type: '拼单搭子', campus: '西校区', price: 0, emoji: '🧋', desc: '满20起送，还差2杯！要喝的dd我～', tags: ['进行中', '差2人'] },
}

const item = items[Number(route.params.id)] || items[1]

const itemId = Number(route.params.id) || 1
const isFavorited = computed(() => favoriteStore.isFavorited(itemId))

function toggleFav() {
  const typeMap: Record<string, FavoriteItem['type']> = {
    '二手交易': 'trade',
    '失物招领': 'lostFound',
    '拼单搭子': 'groupBuy',
  }
  const favItem: FavoriteItem = {
    id: itemId,
    type: typeMap[item.type] || 'trade',
    title: item.title,
    price: item.price || undefined,
    campus: item.campus,
    addedAt: new Date().toLocaleString(),
  }
  favoriteStore.toggleFavorite(favItem)
}
</script>

<template>
  <div class="detail-view">
    <button class="back-btn" @click="router.back()">← 回去</button>

    <div class="detail-card">
      <div class="detail-emoji">{{ item.emoji }}</div>
      <h2 class="detail-title">{{ item.title }}</h2>

      <div class="detail-tags">
        <span class="tag tag-type">{{ item.type }}</span>
        <span class="tag tag-campus">{{ item.campus }}</span>
        <span v-if="item.price" class="tag tag-price">￥{{ item.price }}</span>
      </div>

      <div class="detail-meta">
        <span>👤 校园用户</span>
        <span>🕐 2026-06-27</span>
        <span>👁️ {{ Number(route.params.id) * 23 }} 次浏览</span>
      </div>

      <p class="detail-desc">{{ item.desc }}</p>

      <div class="detail-tags-list">
        <span v-for="t in item.tags" :key="t" class="tag-simple">{{ t }}</span>
      </div>

      <div class="detail-actions">
        <button class="action-btn favorite" :class="{ liked: isFavorited }" @click="toggleFav">
          {{ isFavorited ? '❤️ 已收藏' : '🤍 收藏' }}
        </button>
        <button class="action-btn contact">💬 联系发布者</button>
        <button v-if="item.type === '二手交易'" class="action-btn bargain">💰 砍个价</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-view {
  max-width: 600px;
}

.back-btn {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  padding: 8px 18px;
  border-radius: var(--radius-md);
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 16px;
  transition: all 0.15s;
}

.back-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.detail-card {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  background: var(--color-surface);
  box-shadow: var(--shadow-md);
}

.detail-emoji {
  font-size: 56px;
  text-align: center;
  margin-bottom: 12px;
}

.detail-title {
  font-size: 22px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 12px;
  color: var(--color-text);
}

.detail-tags {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 16px;
}

.tag {
  font-size: 12px;
  padding: 4px 14px;
  border-radius: 14px;
  font-weight: 700;
}

.tag-type { background: var(--color-primary-light); color: var(--color-text-secondary); border: 1.5px solid var(--color-border); }
.tag-campus { background: #E0F2FE; color: #0369A1; border: 1.5px solid #38BDF8; }
.tag-price { background: #FEE2E2; color: #DC2626; border: 1.5px solid var(--color-primary); font-size: 14px; }

.detail-meta {
  display: flex;
  justify-content: center;
  gap: 16px;
  font-size: 13px;
  color: var(--color-text-secondary);
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.detail-desc {
  font-size: 15px;
  line-height: 1.8;
  color: #5C4A2E;
  padding: 16px;
  background: var(--color-accent-light);
  border-radius: var(--radius-md);
  margin-bottom: 16px;
}

.detail-tags-list {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.tag-simple {
  font-size: 12px;
  padding: 4px 12px;
  border: 1px dashed var(--color-primary);
  border-radius: 14px;
  color: var(--color-text-secondary);
  background: var(--color-accent-light);
}

.detail-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.action-btn {
  flex: 1;
  min-width: 120px;
  padding: 10px 16px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
  color: var(--color-text);
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.action-btn.favorite.liked {
  background: #FEE2E2;
  border-color: var(--color-primary);
  color: #DC2626;
}

.action-btn.contact {
  background: var(--color-primary-light);
}

.action-btn.bargain {
  background: var(--color-accent-light);
  border-color: var(--color-primary);
}
</style>
