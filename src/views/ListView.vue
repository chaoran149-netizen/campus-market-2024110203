<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goDetail = (id: number) => {
  router.push({ name: 'detail', params: { id } })
}
</script>

<template>
  <div class="list-view">
    <h2>集市信息列表</h2>
    <div class="filters">
      <input type="text" placeholder="搜索关键词..." class="search-input" />
      <select class="filter-select"><option value="">全部类型</option><option>二手交易</option><option>失物招领</option><option>拼单搭子</option><option>跑腿委托</option></select>
      <select class="filter-select"><option value="">全部校区</option><option>主校区</option><option>东校区</option><option>西校区</option></select>
    </div>
    <div class="item-list">
      <div v-for="i in 6" :key="i" class="item-card" @click="goDetail(i)">
        <h3>示例物品 {{ i }}</h3>
        <p class="item-meta">二手交易 · 主校区 · ￥{{ i * 10 }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.list-view { padding: 16px; }
.filters { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
.search-input { flex: 1; min-width: 180px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.filter-select { padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.item-list { display: grid; gap: 12px; }
.item-card { padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; cursor: pointer; }
.item-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.item-meta { color: #666; font-size: 14px; }
</style>
