<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getLostFounds } from '@/api/lostFound'
import ItemCard from '@/components/ItemCard.vue'
import EmptyState from '@/components/EmptyState.vue'

interface LostFound {
  id: number; title: string; type: string; itemName: string;
  location: string; time: string; description: string;
  status: string; campus: string; contact: string;
}

const items = ref<LostFound[]>([])
const loading = ref(true)
const activeTab = ref<'lost' | 'found'>('lost')

onMounted(async () => {
  try {
    const res = await getLostFounds()
    items.value = res.data
  } finally {
    loading.value = false
  }
})

const filteredItems = () => items.value.filter((i: LostFound) => i.type === activeTab.value)
</script>

<template>
  <div class="lost-found-view">
    <div class="page-top">
      <h2>失物招领</h2>
      <p>丢了东西别着急，捡到东西也别放着</p>
    </div>

    <div class="tab-bar">
      <button :class="{ active: activeTab === 'lost' }" @click="activeTab = 'lost'">遗失求助</button>
      <button :class="{ active: activeTab === 'found' }" @click="activeTab = 'found'">拾取启事</button>
    </div>

    <EmptyState v-if="!loading && filteredItems().length === 0" message="暂无相关信息" />

    <div v-else class="item-list">
      <ItemCard
        v-for="item in filteredItems()"
        :key="item.id"
        type="lostFound"
        :data="item"
      />
    </div>
  </div>
</template>

<style scoped>
.lost-found-view { display: flex; flex-direction: column; gap: 24px; }

.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }

.tab-bar { display: flex; gap: 8px; background: var(--color-border-light); padding: 4px; border-radius: var(--radius-lg); }
.tab-bar button {
  flex: 1; padding: 10px 20px; border: none; border-radius: var(--radius-md); background: transparent;
  font-size: 14px; font-weight: 600; font-family: inherit; cursor: pointer; color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}
.tab-bar button.active { background: var(--color-surface); color: var(--color-text); box-shadow: var(--shadow-xs); }

.item-list { display: flex; flex-direction: column; gap: 10px; }
</style>
