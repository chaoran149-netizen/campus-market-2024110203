<script setup lang="ts">
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
    <div class="user-card">
      <div class="avatar">👤</div>
      <h3>校园用户</h3>
      <p class="user-id">学号：20240***</p>
      <div class="stats">
        <div class="stat-item">
          <span class="stat-num">12</span>
          <span class="stat-label">我的发布</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">5</span>
          <span class="stat-label">收藏</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">3</span>
          <span class="stat-label">消息</span>
        </div>
      </div>
    </div>

    <div class="menu-list">
      <div v-for="(item, i) in menus" :key="i" class="menu-item">
        <span class="menu-icon">{{ item.icon }}</span>
        <span class="menu-label">{{ item.label }}</span>
        <span class="menu-arrow">→</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.user-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.user-card {
  text-align: center;
  padding: 32px 24px 20px;
  background: #FFFDF5;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  box-shadow: 6px 6px 0px var(--doodle-border);
}

.avatar {
  font-size: 56px;
  margin-bottom: 8px;
}

.user-card h3 {
  font-size: 20px;
  font-weight: 900;
  color: var(--doodle-red);
  margin-bottom: 2px;
}

.user-id {
  font-size: 13px;
  color: #A16207;
  margin-bottom: 16px;
}

.stats {
  display: flex;
  justify-content: center;
  gap: 32px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-num {
  font-size: 20px;
  font-weight: 900;
  color: var(--doodle-yellow);
}

.stat-label {
  font-size: 12px;
  color: #A16207;
}

.menu-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  cursor: pointer;
  transition: all 0.15s;
}

.menu-item:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.menu-icon {
  font-size: 20px;
}

.menu-label {
  flex: 1;
  font-size: 15px;
  font-weight: 700;
}

.menu-arrow {
  font-size: 16px;
  color: var(--doodle-yellow);
}
</style>
