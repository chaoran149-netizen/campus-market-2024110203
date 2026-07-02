<script setup lang="ts">
defineProps<{ message?: string }>()
</script>

<template>
  <div class="loading-state">
    <span class="spinner"></span>
    <p>{{ message || '加载中…' }}</p>
  </div>
</template>

<style scoped>
.loading-state {
  display: flex; flex-direction: column; align-items: center; gap: 12px;
  padding: 48px 24px; color: var(--color-text-muted);
}
.spinner {
  width: 32px; height: 32px; border: 3px solid var(--color-border);
  border-top-color: var(--color-primary); border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.loading-state p { font-size: 14px; }
</style>
