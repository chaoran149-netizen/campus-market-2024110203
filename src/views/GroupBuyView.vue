<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getGroupBuys } from '@/api/groupBuy'
import ItemCard from '@/components/ItemCard.vue'
import EmptyState from '@/components/EmptyState.vue'

interface GroupBuy {
  id: number; title: string; type: string; targetCount: number;
  currentCount: number; deadline: string; location: string;
  publisher: string; status: string; campus: string;
}

const items = ref<GroupBuy[]>([])
const loading = ref(true)
const categories = ['全部', '外卖拼单', '奶茶拼单', '学习搭子', '运动搭子', '游戏组队', '休闲搭子']
const activeCat = ref('全部')

onMounted(async () => {
  try {
    const res = await getGroupBuys()
    items.value = res.data
  } finally {
    loading.value = false
  }
})

const filteredItems = () => {
  if (activeCat.value === '全部') return items.value
  return items.value.filter((i: GroupBuy) => i.type === activeCat.value)
}
</script>

<template>
  <div class="group-buy-view">
    <div class="page-top">
      <h2>拼单搭子</h2>
      <p>找人一起拼、一起学、一起玩</p>
    </div>

    <div class="cat-scroll">
      <button
        v-for="cat in categories"
        :key="cat"
        :class="{ active: activeCat === cat }"
        @click="activeCat = cat"
      >{{ cat }}</button>
    </div>

    <EmptyState v-if="!loading && filteredItems().length === 0" message="暂无拼单信息" />

    <div v-else class="item-grid">
      <ItemCard
        v-for="item in filteredItems()"
        :key="item.id"
        type="groupBuy"
        :data="item"
      />
    </div>
  </div>
</template>

<style scoped>
.group-buy-view { display: flex; flex-direction: column; gap: 24px; }

.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }

.cat-scroll { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; scrollbar-width: none; }
.cat-scroll::-webkit-scrollbar { display: none; }
.cat-scroll button {
  padding: 8px 18px; border-radius: var(--radius-full); border: 1px solid var(--color-border);
  background: var(--color-surface); font-size: 13px; font-weight: 500; font-family: inherit;
  color: var(--color-text-secondary); white-space: nowrap; cursor: pointer; transition: all var(--transition-fast);
}
.cat-scroll button:hover { border-color: var(--color-primary-soft); color: var(--color-primary); }
.cat-scroll button.active { background: var(--color-primary); color: #fff; border-color: var(--color-primary); }

.item-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px;
}
@media (max-width: 640px) { .item-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; } }
</style>
