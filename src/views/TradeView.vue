<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { getTrades } from '@/api/trade'
import ItemCard from '@/components/ItemCard.vue'
import EmptyState from '@/components/EmptyState.vue'
import LoadingState from '@/components/LoadingState.vue'
import ErrorState from '@/components/ErrorState.vue'
import SearchBar from '@/components/SearchBar.vue'

interface Trade {
  id: number; title: string; price: number; category: string;
  condition: string; campus: string; publisher: string;
}

const trades = ref<Trade[]>([])
const loading = ref(true)
const error = ref(false)
const keyword = ref('')
const activeCat = ref('全部')
const categories = ['全部', '教材书籍', '数码电子', '生活用品', '运动装备']

const fetchTrades = async () => {
  loading.value = true
  error.value = false
  try {
    const res = await getTrades()
    trades.value = res.data
  } catch {
    error.value = true
  } finally {
    loading.value = false
  }
}

onMounted(fetchTrades)

const filtered = computed(() => {
  let list = trades.value
  if (activeCat.value !== '全部') list = list.filter(t => t.category === activeCat.value)
  if (keyword.value.trim()) {
    const kw = keyword.value.trim().toLowerCase()
    list = list.filter(t => t.title.toLowerCase().includes(kw) || t.publisher.toLowerCase().includes(kw))
  }
  return list
})
</script>

<template>
  <div class="trade-view">
    <div class="page-top">
      <h2>二手交易</h2>
      <p>买卖闲置好物，让物品找到新主人</p>
    </div>

    <SearchBar v-model="keyword" placeholder="搜索商品标题或发布人…" />

    <div class="cat-bar">
      <button v-for="cat in categories" :key="cat" :class="{ active: activeCat === cat }" @click="activeCat = cat">{{ cat }}</button>
    </div>

    <LoadingState v-if="loading" />
    <ErrorState v-else-if="error" message="加载失败，请检查 Mock 服务" @retry="fetchTrades" />
    <EmptyState v-else-if="filtered.length === 0" message="没有找到匹配的商品" />

    <div v-else class="item-list">
      <ItemCard v-for="item in filtered" :key="item.id" type="trade" :data="item" />
    </div>
  </div>
</template>

<style scoped>
.trade-view { display: flex; flex-direction: column; gap: 24px; }
.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }
.cat-bar { display: flex; gap: 8px; flex-wrap: wrap; }
.cat-bar button {
  padding: 8px 18px; border-radius: var(--radius-full); border: 1px solid var(--color-border);
  background: var(--color-surface); font-size: 13px; font-weight: 500; font-family: inherit;
  color: var(--color-text-secondary); cursor: pointer; transition: all var(--transition-fast);
}
.cat-bar button:hover { border-color: var(--color-primary-soft); color: var(--color-primary); }
.cat-bar button.active { background: var(--color-primary); color: #fff; border-color: var(--color-primary); }
.item-list { display: flex; flex-direction: column; gap: 10px; }
</style>
