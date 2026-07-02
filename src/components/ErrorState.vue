<script setup lang="ts">
defineProps<{ message?: string }>()
const emit = defineEmits<{ retry: [] }>()
</script>

<template>
  <div class="error-state">
    <span class="error-icon">⚠️</span>
    <p>{{ message || '加载失败，请检查网络或 Mock 服务' }}</p>
    <button class="retry-btn" @click="emit('retry')">重新加载</button>
  </div>
</template>

<style scoped>
.error-state {
  display: flex; flex-direction: column; align-items: center; gap: 12px;
  padding: 48px 24px; text-align: center;
}
.error-icon { font-size: 36px; }
.error-state p { font-size: 14px; color: var(--color-text-secondary); }
.retry-btn {
  padding: 8px 20px; border: 1px solid var(--color-border); border-radius: var(--radius-md);
  background: var(--color-surface); font-size: 13px; font-weight: 500;
  font-family: inherit; cursor: pointer; color: var(--color-primary);
  transition: all var(--transition-fast);
}
.retry-btn:hover { border-color: var(--color-primary); background: var(--color-primary-light); }
</style>
