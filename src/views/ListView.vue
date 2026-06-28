<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const keyword = ref('')
const typeFilter = ref('')
const campusFilter = ref('')

const items = ref([
  { id: 1, title: '二手教材 - 高等数学', type: '二手交易', campus: '主校区', price: 25, emoji: '📚' },
  { id: 2, title: '蓝牙耳机 九成新', type: '二手交易', campus: '东校区', price: 80, emoji: '🎧' },
  { id: 3, title: '丢失校园卡 - 李**, 计算机学院', type: '失物招领', campus: '主校区', price: 0, emoji: '🪪' },
  { id: 4, title: '奶茶拼单！一点点', type: '拼单搭子', campus: '西校区', price: 0, emoji: '🧋' },
  { id: 5, title: '代取快递 - 菜鸟驿站', type: '跑腿委托', campus: '主校区', price: 5, emoji: '📦' },
  { id: 6, title: '捡到一个水杯', type: '失物招领', campus: '东校区', price: 0, emoji: '🥤' },
])

const goDetail = (id: number) => {
  router.push({ name: 'detail', params: { id } })
}
</script>

<template>
  <div class="list-view">
    <div class="list-header">
      <h2>集市货架</h2>
      <span class="count-badge">共 {{ items.length }} 件</span>
    </div>

    <div class="filters">
      <input v-model="keyword" type="text" placeholder="搜点什么..." class="search-input" />
      <select v-model="typeFilter" class="filter-select">
        <option value="">🎯 全部分类</option>
        <option>二手交易</option>
        <option>失物招领</option>
        <option>拼单搭子</option>
        <option>跑腿委托</option>
      </select>
      <select v-model="campusFilter" class="filter-select">
        <option value="">📍 全部校区</option>
        <option>主校区</option>
        <option>东校区</option>
        <option>西校区</option>
      </select>
    </div>

    <div class="item-list">
      <div v-for="item in items" :key="item.id" class="item-card" @click="goDetail(item.id)">
        <div class="item-emoji">{{ item.emoji }}</div>
        <div class="item-info">
          <h3 class="item-title">{{ item.title }}</h3>
          <p class="item-tags">
            <span class="tag tag-type">{{ item.type }}</span>
            <span class="tag tag-campus">{{ item.campus }}</span>
            <span v-if="item.price" class="tag tag-price">￥{{ item.price }}</span>
          </p>
        </div>
        <div class="item-arrow">→</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.list-header {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 16px;
}

.list-header h2 {
  font-size: 22px;
  font-weight: 900;
}

.count-badge {
  font-size: 13px;
  padding: 2px 12px;
  border: 2px solid var(--doodle-border);
  border-radius: 20px;
  background: var(--doodle-cream);
  font-weight: 700;
  color: #A16207;
}

.filters {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.search-input {
  flex: 1;
  min-width: 180px;
  padding: 10px 14px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  font-family: inherit;
  font-size: 14px;
  background: #FFFDF5;
}

.search-input:focus {
  outline: none;
  box-shadow: 3px 3px 0px var(--doodle-border);
}

.filter-select {
  padding: 10px 14px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  font-family: inherit;
  font-size: 14px;
  background: #FFFDF5;
  cursor: pointer;
}

.filter-select:focus {
  outline: none;
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
  padding: 14px 18px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  cursor: pointer;
  background: #FFFDF5;
  transition: all 0.15s;
}

.item-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.item-emoji {
  font-size: 36px;
  flex-shrink: 0;
}

.item-info {
  flex: 1;
  min-width: 0;
}

.item-title {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 6px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.tag {
  font-size: 11px;
  padding: 2px 10px;
  border-radius: 12px;
  font-weight: 700;
}

.tag-type {
  background: #FEF3C7;
  color: #A16207;
  border: 1.5px solid #D97706;
}

.tag-campus {
  background: #E0F2FE;
  color: #0369A1;
  border: 1.5px solid #38BDF8;
}

.tag-price {
  background: #FEE2E2;
  color: #DC2626;
  border: 1.5px solid #EF4444;
}

.item-arrow {
  font-size: 20px;
  color: #A16207;
  font-weight: 700;
  flex-shrink: 0;
}
</style>
