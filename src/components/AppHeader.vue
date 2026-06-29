<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <header class="app-header">
    <div class="header-inner">
      <h1 class="app-title" @click="router.push('/')">
        校园轻集市
      </h1>
      <slot name="nav" />
    </div>
  </header>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--color-border);
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 32px;
  padding: 0 var(--content-padding);
  max-width: var(--content-width);
  margin: 0 auto;
  height: var(--header-height);
}

.app-title {
  font-family: 'Inter', 'Noto Sans SC', sans-serif;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  color: var(--color-text);
  white-space: nowrap;
  letter-spacing: -0.02em;
  user-select: none;
  transition: color var(--transition);
  flex-shrink: 0;
}

.app-title:hover {
  color: var(--color-primary);
}

@media (max-width: 640px) {
  .header-inner {
    padding: 0 16px;
    gap: 16px;
  }

  .app-title {
    font-size: 16px;
  }
}
</style>
