<script setup lang="ts"></script>

<template>
  <div class="trade-view">
    <div class="page-header">
      <h2>📋 二手交易</h2>
      <p>买卖闲置好物，让物品找到新主人</p>
    </div>

    <div class="filter-bar">
      <input type="text" class="search-input" placeholder="搜一搜你想找的好物..." />
      <select class="select-input">
        <option value="">全部分类</option>
        <option value="book">📚 教材书籍</option>
        <option value="digital">📱 数码电子</option>
        <option value="life">🏠 生活用品</option>
        <option value="sport">⚽ 运动装备</option>
      </select>
    </div>

    <div class="item-grid">
      <div v-for="i in 6" :key="i" class="item-card">
        <div class="item-emoji">{{ ['📚', '🎧', '🚲', '💡', '⌨️', '🎸'][i - 1] }}</div>
        <h4>{{ ['高等数学教材', '蓝牙耳机', '校园自行车', 'LED 台灯', '机械键盘', '民谣吉他'][i - 1] }}</h4>
        <p class="item-price">￥{{ i * 15 + 10 }}</p>
        <p class="item-meta">主校区 · 九成新</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.trade-view {
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

.filter-bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.search-input {
  flex: 1;
  min-width: 160px;
  padding: 10px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  font-size: 14px;
  font-family: inherit;
  outline: none;
  transition: box-shadow 0.15s;
}

.search-input:focus {
  box-shadow: 0 0 0 3px var(--doodle-cream);
}

.select-input {
  padding: 10px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  font-size: 14px;
  font-family: inherit;
  cursor: pointer;
}

.item-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 16px;
}

.item-card {
  padding: 20px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  text-align: center;
  cursor: pointer;
  transition: all 0.15s;
}

.item-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.item-emoji {
  font-size: 36px;
  margin-bottom: 8px;
}

.item-card h4 {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
}

.item-price {
  font-size: 16px;
  font-weight: 900;
  color: var(--doodle-red);
  margin-bottom: 2px;
}

.item-meta {
  font-size: 12px;
  color: #A16207;
}
</style>
