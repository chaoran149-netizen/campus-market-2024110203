<script setup lang="ts">
const stats = [
  { num: 12, label: '我的发布' },
  { num: 5, label: '收藏' },
  { num: 3, label: '消息' },
]

const menus = [
  { icon: '📋', label: '我的发布' },
  { icon: '❤️', label: '我的收藏' },
  { icon: '📦', label: '我的订单' },
  { icon: '🔍', label: '浏览记录' },
  { icon: '⚙️', label: '账号设置' },
  { icon: '🛡️', label: '安全中心' },
]
</script>

<template>
  <div class="user-view">
    <!-- Profile Card -->
    <div class="profile-card">
      <div class="avatar-circle">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <div class="profile-info">
        <h3>校园用户</h3>
        <p>学号 20240*** · 主校区</p>
      </div>
    </div>

    <!-- Stats -->
    <div class="stats-row">
      <div v-for="s in stats" :key="s.label" class="stat-item">
        <span class="stat-num">{{ s.num }}</span>
        <span class="stat-label">{{ s.label }}</span>
      </div>
    </div>

    <!-- Menu -->
    <div class="menu-list">
      <button v-for="m in menus" :key="m.label" class="menu-item">
        <span>{{ m.icon }}</span>
        <span>{{ m.label }}</span>
        <svg class="menu-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.user-view { display: flex; flex-direction: column; gap: 20px; max-width: 480px; }

/* ── Profile Card ── */
.profile-card {
  display: flex; align-items: center; gap: 16px;
  padding: 24px; border: 1px solid var(--color-border); border-radius: var(--radius-xl);
  background: var(--color-surface);
}

.avatar-circle {
  width: 56px; height: 56px; border-radius: 50%; background: var(--color-primary-light);
  color: var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}

.profile-info h3 { font-size: 18px; font-weight: 700; color: var(--color-text); margin-bottom: 2px; letter-spacing: -0.02em; }
.profile-info p { font-size: 13px; color: var(--color-text-secondary); }

/* ── Stats ── */
.stats-row {
  display: flex; gap: 1px; background: var(--color-border);
  border-radius: var(--radius-lg); overflow: hidden;
}

.stat-item {
  flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px;
  padding: 16px 8px; background: var(--color-surface);
}

.stat-num { font-size: 22px; font-weight: 700; color: var(--color-primary); }
.stat-label { font-size: 12px; color: var(--color-text-muted); }

/* ── Menu ── */
.menu-list {
  display: flex; flex-direction: column; border: 1px solid var(--color-border);
  border-radius: var(--radius-lg); overflow: hidden; background: var(--color-surface);
}

.menu-item {
  display: flex; align-items: center; gap: 14px; padding: 16px 20px;
  border: none; border-bottom: 1px solid var(--color-border-light); background: transparent;
  font-size: 15px; font-weight: 500; color: var(--color-text); font-family: inherit;
  cursor: pointer; transition: background var(--transition-fast); text-align: left; width: 100%;
}
.menu-item:last-child { border-bottom: none; }
.menu-item:hover { background: var(--color-surface-hover); }
.menu-item span:first-child { font-size: 18px; }
.menu-item span:nth-child(2) { flex: 1; }
.menu-arrow { color: var(--color-text-muted); flex-shrink: 0; }
</style>
