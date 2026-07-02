<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getErrands } from '@/api/errand'
import ItemCard from '@/components/ItemCard.vue'
import EmptyState from '@/components/EmptyState.vue'

interface Errand {
  id: number; title: string; taskType: string; reward: number;
  description: string; status: string; campus: string;
  deadline: string; publisher: string;
}

const items = ref<Errand[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await getErrands()
    items.value = res.data
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="errand-view">
    <div class="page-top">
      <h2>跑腿委托</h2>
      <p>找人帮忙，轻松搞定杂事</p>
    </div>

    <EmptyState v-if="!loading && items.length === 0" message="暂无跑腿任务" />

    <div v-else class="item-grid">
      <ItemCard
        v-for="item in items"
        :key="item.id"
        type="errand"
        :data="item"
      />
    </div>
  </div>
</template>

<style scoped>
.errand-view { display: flex; flex-direction: column; gap: 24px; }

.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }

.item-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px;
}
@media (max-width: 640px) { .item-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; } }
</style>
