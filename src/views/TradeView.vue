<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getTrades } from '@/api/trade'
import { useFavoriteStore } from '@/stores/favorite'
import ItemCard from '@/components/ItemCard.vue'
import EmptyState from '@/components/EmptyState.vue'

interface Trade {
  id: number; title: string; price: number; category: string;
  condition: string; campus: string; status: string;
  publisher: string; publishTime: string; location: string;
}

const trades = ref<Trade[]>([])
const loading = ref(true)
const favoriteStore = useFavoriteStore()

const categories = ['全部', '教材书籍', '数码电子', '生活用品', '运动装备']
const activeCat = ref('全部')

onMounted(async () => {
  try {
    const res = await getTrades()
    trades.value = res.data
  } finally {
    loading.value = false
  }
})

const filteredTrades = () => {
  if (activeCat.value === '全部') return trades.value
  return trades.value.filter((t: Trade) => t.category === activeCat.value)
}

function toggleFav(item: Trade) {
  favoriteStore.toggleFavorite({
    id: item.id,
    type: 'trade',
    title: item.title,
    price: item.price,
    campus: item.campus,
    addedAt: '',
  })
}
</script>

<template>
  <div class="trade-view">
    <div class="page-top">
      <h2>二手交易</h2>
      <p>买卖闲置好物，让物品找到新主人</p>
    </div>

    <div class="search-bar">
      <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="text" placeholder="搜索商品、分类、校区..." />
    </div>

    <div class="cat-bar">
      <button v-for="cat in categories" :key="cat" :class="{ active: activeCat === cat }" @click="activeCat = cat">{{ cat }}</button>
    </div>

    <EmptyState v-if="!loading && filteredTrades().length === 0" message="暂无商品信息" />

    <div v-else class="item-list">
      <div v-for="item in filteredTrades()" :key="item.id" class="item-row">
        <ItemCard type="trade" :data="(item as unknown as Record<string, unknown>)" class="flex-1" />
        <button class="fav-btn" :class="{ favorited: favoriteStore.isFavorited(item.id) }" @click.stop="toggleFav(item)" :title="favoriteStore.isFavorited(item.id) ? '取消收藏' : '收藏'">
          <svg width="18" height="18" viewBox="0 0 24 24" :fill="favoriteStore.isFavorited(item.id) ? 'currentColor' : 'none'" :stroke="favoriteStore.isFavorited(item.id) ? 'none' : 'currentColor'" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.trade-view { display: flex; flex-direction: column; gap: 24px; }
.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }
.search-bar { display: flex; align-items: center; gap: 10px; padding: 12px 18px; border: 1px solid var(--color-border); border-radius: var(--radius-lg); background: var(--color-surface); transition: border-color var(--transition-fast); }
.search-bar:focus-within { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.search-icon { color: var(--color-text-muted); flex-shrink: 0; }
.search-bar input { flex: 1; border: none; outline: none; font-size: 14px; font-family: inherit; background: transparent; color: var(--color-text); }
.search-bar input::placeholder { color: var(--color-text-muted); }
.cat-bar { display: flex; gap: 8px; flex-wrap: wrap; }
.cat-bar button { padding: 8px 18px; border-radius: var(--radius-full); border: 1px solid var(--color-border); background: var(--color-surface); font-size: 13px; font-weight: 500; font-family: inherit; color: var(--color-text-secondary); cursor: pointer; transition: all var(--transition-fast); }
.cat-bar button:hover { border-color: var(--color-primary-soft); color: var(--color-primary); }
.cat-bar button.active { background: var(--color-primary); color: #fff; border-color: var(--color-primary); }
.item-list { display: flex; flex-direction: column; gap: 10px; }
.item-row { display: flex; align-items: center; gap: 10px; }
.flex-1 { flex: 1; }
.fav-btn { width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--color-border); background: var(--color-surface); cursor: pointer; display: flex; align-items: center; justify-content: center; color: var(--color-text-muted); transition: all var(--transition-fast); flex-shrink: 0; }
.fav-btn:hover { border-color: #F43F5E; color: #F43F5E; }
.fav-btn.favorited { color: #F43F5E; background: #FFF1F2; border-color: #F43F5E; }
</style>
