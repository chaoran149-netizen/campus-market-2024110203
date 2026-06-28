<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <header class="app-header">
    <h1 class="app-title" @click="router.push('/')">校园轻集市</h1>
    <slot name="nav" />
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 16px 32px;
  background: #FFFDF5;
  border-bottom: 3px solid var(--doodle-border);
  flex-wrap: wrap;
}

.app-title {
  font-size: 24px;
  font-weight: 900;
  cursor: pointer;
  color: var(--doodle-red);
  white-space: nowrap;
  letter-spacing: 2px;
  text-shadow: 2px 2px 0 #FEF3C7;
  user-select: none;
}

.app-title:hover {
  transform: rotate(-1deg);
}

@media (max-width: 640px) {
  .app-header {
    padding: 12px 16px;
    gap: 12px;
  }

  .app-title {
    font-size: 20px;
  }
}
</style>
