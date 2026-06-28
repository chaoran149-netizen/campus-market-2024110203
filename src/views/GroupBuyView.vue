<script setup lang="ts"></script>

<template>
  <div class="group-buy-view">
    <div class="page-header">
      <h2>👥 拼单搭子</h2>
      <p>找人一起拼、一起学、一起玩</p>
    </div>

    <div class="category-bar">
      <span class="cat-chip active">全部</span>
      <span class="cat-chip">🍔 外卖拼单</span>
      <span class="cat-chip">🧋 奶茶拼单</span>
      <span class="cat-chip">📖 学习搭子</span>
      <span class="cat-chip">⚽ 运动搭子</span>
    </div>

    <div class="group-list">
      <div v-for="i in 6" :key="i" class="group-card">
        <div class="group-top">
          <div class="group-emoji">{{ ['🍔', '🧋', '📖', '⚽', '🎮', '🎬'][i - 1] }}</div>
          <div class="group-info">
            <h4>{{ ['中午一起点外卖', '一点点拼单', '考研自习搭子', '足球组队缺 2', '王者荣耀组队', '周末看电影'][i - 1] }}</h4>
            <p class="group-meta">{{ ['已有 3/5 人', '已有 2/4 人', '已有 2/6 人', '已有 5/11 人', '已有 4/5 人', '已有 2/4 人'][i - 1] }}</p>
          </div>
        </div>
        <div class="group-tags">
          <span class="tag">{{ ['主校区', '东校区', '西校区', '主校区', '线上', '主校区'][i - 1] }}</span>
          <span class="tag">今天 12:00</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.group-buy-view {
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

.category-bar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.cat-chip {
  padding: 8px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: 40px;
  background: #FFFDF5;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
}

.cat-chip:hover {
  background: var(--doodle-cream);
}

.cat-chip.active {
  background: var(--doodle-yellow);
  color: #fff;
  border-color: var(--doodle-yellow);
}

.group-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.group-card {
  padding: 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  transition: all 0.15s;
}

.group-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.group-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 10px;
}

.group-emoji {
  font-size: 32px;
}

.group-info {
  flex: 1;
}

.group-info h4 {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 2px;
}

.group-meta {
  font-size: 13px;
  color: var(--doodle-red);
  font-weight: 700;
}

.group-tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 3px 10px;
  border: 2px solid var(--doodle-border);
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  background: var(--doodle-cream);
  color: #A16207;
}
</style>
