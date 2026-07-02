<script setup lang="ts">
const model = defineModel<string>({ default: '' })
defineProps<{ placeholder?: string }>()
</script>

<template>
  <div class="search-bar">
    <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
    <input
      type="text"
      :value="model"
      @input="model = ($event.target as HTMLInputElement).value"
      :placeholder="placeholder ?? '搜索…'"
    />
    <button v-if="model" class="clear-btn" @click="model = ''">✕</button>
  </div>
</template>

<style scoped>
.search-bar {
  display: flex; align-items: center; gap: 10px;
  padding: 12px 18px; border: 1px solid var(--color-border); border-radius: var(--radius-lg);
  background: var(--color-surface); transition: border-color var(--transition-fast);
}
.search-bar:focus-within { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.search-icon { color: var(--color-text-muted); flex-shrink: 0; }
.search-bar input {
  flex: 1; border: none; outline: none; font-size: 14px; font-family: inherit;
  background: transparent; color: var(--color-text);
}
.search-bar input::placeholder { color: var(--color-text-muted); }
.clear-btn {
  border: none; background: var(--color-border-light); border-radius: 50%;
  width: 22px; height: 22px; font-size: 12px; cursor: pointer;
  color: var(--color-text-muted); display: flex; align-items: center; justify-content: center;
  transition: all var(--transition-fast);
}
.clear-btn:hover { background: var(--color-border); color: var(--color-text-secondary); }
</style>
