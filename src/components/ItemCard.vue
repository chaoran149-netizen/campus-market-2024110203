<script setup lang="ts">
defineProps<{
  type: 'trade' | 'lostFound' | 'groupBuy' | 'errand'
  data: Record<string, unknown>
}>()
</script>

<template>
  <!-- Trade Card -->
  <router-link v-if="type === 'trade'" :to="'/detail/' + data.id" class="item-card">
    <span class="card-emoji">{{ data.category === '教材书籍' ? '📚' : data.category === '数码电子' ? '📱' : data.category === '生活用品' ? '🏠' : '⚽' }}</span>
    <div class="card-body">
      <h4>{{ data.title }}</h4>
      <div class="card-row">
        <span class="card-price">¥{{ data.price }}</span>
        <span class="card-meta">{{ data.campus }} · {{ data.condition }}</span>
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
        <span class="progress-bar"><span class="progress-fill" :style="{ width: (data.currentCount / data.targetCount * 100) + '%' }"></span></span>
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
      <span class="errand-type-tag" :class="[{express:'express',shop:'shop',print:'print',food:'food',repair:'repair',move:'move',other:'other'}[data.taskType]] || 'other'">
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
.item-card {
  display: flex; align-items: center; gap: 14px;
  padding: 16px; border: 1px solid var(--color-border); border-radius: var(--radius-lg);
  background: var(--color-surface); color: inherit; text-decoration: none;
  transition: all var(--transition);
}
.item-card:hover { border-color: var(--color-border-hover); box-shadow: var(--shadow-sm); transform: translateY(-1px); }

.card-emoji { font-size: 32px; flex-shrink: 0; }
.card-body { flex: 1; min-width: 0; }

.card-body h4 { font-size: 14px; font-weight: 600; color: var(--color-text); margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

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

.card-tags { display: flex; gap: 6px; }
.tag { padding: 2px 8px; border-radius: var(--radius-full); font-size: 11px; font-weight: 500; background: var(--color-border-light); color: var(--color-text-secondary); }

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
