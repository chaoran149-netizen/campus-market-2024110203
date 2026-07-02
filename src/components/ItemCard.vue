<script setup lang="ts">
defineProps<{
  type: 'trade' | 'lostFound' | 'groupBuy' | 'errand'
  data: Record<string, unknown>
}>()
</script>

<template>
  <!-- Trade Card — 电商卡片 -->
  <router-link v-if="type === 'trade'" :to="'/detail/' + data.id" class="trade-card">
    <div class="card-img-wrap">
      <img :src="(data.image as string) || 'https://images.unsplash.com/photo-1586769852044-692d6e3703f0?w=400&h=300&fit=crop'" :alt="data.title as string" loading="lazy" />
      <span v-if="data.status === 'closed'" class="sold-badge">已售</span>
    </div>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <div class="card-row">
        <span class="card-price">¥{{ data.price }}</span>
        <span class="card-meta">{{ data.campus }}</span>
      </div>
      <div class="card-tags">
        <span class="tag">{{ data.category }}</span>
        <span class="tag">{{ data.condition }}</span>
      </div>
    </div>
  </router-link>

  <!-- LostFound Card -->
  <div v-else-if="type === 'lostFound'" class="item-card lost-card">
    <span class="card-emoji">{{ data.type === 'lost' ? '🔍' : '✅' }}</span>
    <div class="card-body">
      <div class="card-row">
        <h4>{{ data.itemName }}</h4>
        <span class="status-badge" :class="data.type">{{ data.type === 'lost' ? '遗失' : '拾取' }}</span>
      </div>
      <p class="card-desc">{{ data.description }}</p>
      <p class="card-meta">{{ data.location }} · {{ data.time }}</p>
    </div>
  </div>

  <!-- GroupBuy Card -->
  <div v-else-if="type === 'groupBuy'" class="item-card group-card">
    <span class="card-emoji">{{ data.type === '外卖拼单' ? '🍔' : data.type === '奶茶拼单' ? '🧋' : data.type === '学习搭子' ? '📖' : data.type === '运动搭子' ? '⚽' : data.type === '游戏组队' ? '🎮' : '🎬' }}</span>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <div class="progress-row">
        <span class="progress-bar"><span class="progress-fill" :style="{ width: (Number(data.currentCount) / Number(data.targetCount) * 100) + '%' }"></span></span>
        <span class="progress-text">{{ data.currentCount }}/{{ data.targetCount }} 人</span>
      </div>
      <div class="card-tags">
        <span class="tag">{{ data.campus }}</span>
        <span class="tag">{{ data.deadline }}</span>
      </div>
    </div>
  </div>

  <!-- Errand Card -->
  <div v-else-if="type === 'errand'" class="item-card errand-card">
    <div class="card-left">
      <span class="errand-type-tag" :class="([{express:'express',shop:'shop',print:'print',food:'food',repair:'repair',move:'move',other:'other'}] as Record<string,string>)[data.taskType as string] || 'other'">
        {{ data.taskType }}
      </span>
      <h4>{{ data.title }}</h4>
      <p class="card-desc">{{ data.description }}</p>
    </div>
    <div class="card-right">
      <span class="card-price">¥{{ data.reward }}</span>
      <span class="status-dot" :class="data.status"></span>
    </div>
  </div>
</template>

<style scoped>
/* ── Trade Card (电商卡片) ── */
.trade-card {
  display: flex; flex-direction: column;
  border-radius: var(--radius-lg); background: var(--color-surface);
  overflow: hidden; text-decoration: none; color: inherit;
  transition: all var(--transition); border: 1px solid var(--color-border);
}
.trade-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); border-color: var(--color-border-hover); }

.card-img-wrap {
  position: relative; width: 100%; padding-top: 75%; overflow: hidden; background: var(--color-border-light);
}
.card-img-wrap img {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;
  transition: transform var(--transition-slow);
}
.trade-card:hover .card-img-wrap img { transform: scale(1.05); }

.sold-badge {
  position: absolute; top: 8px; right: 8px;
  padding: 3px 10px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;
  background: rgba(0,0,0,0.6); color: #fff;
}

.trade-card .card-body { padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; }
.trade-card h4 {
  font-size: 14px; font-weight: 600; color: var(--color-text);
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
  overflow: hidden; line-height: 1.4;
}

.trade-card .card-row { display: flex; align-items: baseline; gap: 8px; }
.trade-card .card-price { font-size: 18px; font-weight: 700; color: #F43F5E; }
.trade-card .card-meta { font-size: 12px; color: var(--color-text-muted); }

.card-tags { display: flex; gap: 6px; flex-wrap: wrap; }
.tag { padding: 2px 8px; border-radius: var(--radius-full); font-size: 11px; font-weight: 500; background: var(--color-border-light); color: var(--color-text-secondary); }

/* ── Common Item Card (非交易) ── */
.item-card {
  display: flex; align-items: center; gap: 14px;
  padding: 16px; border: 1px solid var(--color-border); border-radius: var(--radius-lg);
  background: var(--color-surface); color: inherit; text-decoration: none;
  transition: all var(--transition);
}
.item-card:hover { border-color: var(--color-border-hover); box-shadow: var(--shadow-sm); transform: translateY(-1px); }

.card-emoji { font-size: 32px; flex-shrink: 0; }
.card-body { flex: 1; min-width: 0; }
.card-body h4 { font-size: 14px; font-weight: 600; color: var(--color-text); margin-bottom: 4px; }

.card-row { display: flex; align-items: center; gap: 10px; }
.card-price { font-size: 15px; font-weight: 700; color: var(--color-primary); }
.card-meta { font-size: 12px; color: var(--color-text-muted); }
.card-desc { font-size: 13px; color: var(--color-text-secondary); margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.status-badge { padding: 2px 10px; border-radius: var(--radius-full); font-size: 11px; font-weight: 600; flex-shrink: 0; }
.status-badge.lost { background: #FEF3C7; color: #D97706; }
.status-badge.found { background: #D1FAE5; color: #059669; }

/* GroupBuy */
.progress-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.progress-bar { flex: 1; height: 6px; background: var(--color-border-light); border-radius: var(--radius-full); overflow: hidden; }
.progress-fill { display: block; height: 100%; background: var(--color-primary); border-radius: var(--radius-full); transition: width var(--transition-slow); }
.progress-text { font-size: 12px; color: var(--color-text-secondary); white-space: nowrap; }

/* Errand */
.errand-card { align-items: flex-start; }
.card-left { flex: 1; min-width: 0; }
.card-right { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0; }

.errand-type-tag { display: inline-block; padding: 2px 10px; border-radius: var(--radius-full); font-size: 11px; font-weight: 600; margin-bottom: 6px; }
.errand-type-tag.express { background: #EEF2FF; color: var(--color-primary); }
.errand-type-tag.shop { background: #FEF3C7; color: #D97706; }
.errand-type-tag.print { background: #F3E8FF; color: #7C3AED; }
.errand-type-tag.food { background: #FCE7F3; color: #BE185D; }
.errand-type-tag.repair { background: #D1FAE5; color: #059669; }
.errand-type-tag.move { background: #FFEDD5; color: #EA580C; }
.errand-type-tag.other { background: var(--color-border-light); color: var(--color-text-secondary); }

.status-dot { width: 8px; height: 8px; border-radius: 50%; }
.status-dot.open { background: #F59E0B; }
.status-dot.taken { background: var(--color-primary); }
.status-dot.done { background: #10B981; }
</style>
