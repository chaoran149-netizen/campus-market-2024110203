<script setup lang="ts">
defineProps<{
  message?: string
}>()
</script>

<template>
  <div class="empty-state">
    <span class="empty-icon">📭</span>
    <p>{{ message || '暂无数据' }}</p>
  </div>
</template>

<style scoped>
.empty-state {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 64px 24px; color: var(--color-text-muted);
}
.empty-icon { font-size: 48px; margin-bottom: 12px; }
.empty-state p { font-size: 15px; }
</style>
