<script setup lang="ts"></script>

<template>
  <div class="lost-found-view">
    <div class="page-header">
      <h2>🔍 失物招领</h2>
      <p>丢了东西别着急，捡到东西也别放着</p>
    </div>

    <div class="tab-bar">
      <button class="tab-btn active">遗失求助</button>
      <button class="tab-btn">拾取启示</button>
    </div>

    <div class="item-list">
      <div v-for="i in 5" :key="i" class="item-card">
        <div class="card-left">
          <div class="card-emoji">{{ ['🪪', '🔑', '📱', '👛', '🧣'][i - 1] }}</div>
        </div>
        <div class="card-body">
          <h4>{{ ['校园卡', '钥匙串', '手机', '钱包', '围巾'][i - 1] }}</h4>
          <p class="card-desc">{{ ['李同学 · 计算机学院', '一串钥匙 + 红色挂件', 'iPhone 14 黑色', '棕色钱包含证件', '灰色羊绒围巾'][i - 1] }}</p>
          <p class="card-meta">主校区 · 二食堂附近 · 昨天</p>
        </div>
        <div class="card-badge">{{ i === 3 ? '🔴 未找到' : '🟢 已找到' }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.lost-found-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.page-header {
  text-align: center;
  padding: 28px 24px 20px;
  background: #FFFDF5;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  box-shadow: 6px 6px 0px var(--doodle-border);
}

.page-header h2 {
  font-size: 22px;
  font-weight: 900;
  color: var(--doodle-red);
  margin-bottom: 6px;
}

.page-header p {
  color: #A16207;
  font-size: 14px;
}

.tab-bar {
  display: flex;
  gap: 8px;
}

.tab-btn {
  flex: 1;
  padding: 10px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  font-size: 14px;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.15s;
}

.tab-btn:hover {
  background: var(--doodle-cream);
}

.tab-btn.active {
  background: var(--doodle-yellow);
  color: #fff;
  border-color: var(--doodle-yellow);
  box-shadow: 3px 3px 0px var(--doodle-border);
}

.item-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.item-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  transition: all 0.15s;
}

.item-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.card-emoji {
  font-size: 32px;
}

.card-body {
  flex: 1;
}

.card-body h4 {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 2px;
}

.card-desc {
  font-size: 13px;
  color: #A16207;
  margin-bottom: 2px;
}

.card-meta {
  font-size: 12px;
  color: #B45309;
}

.card-badge {
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
}
</style>
