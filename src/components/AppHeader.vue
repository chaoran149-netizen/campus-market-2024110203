<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
</script>

<template>
  <header class="app-header">
    <div class="header-inner">
      <h1 class="app-title" @click="router.push('/')">
        校园轻集市
      </h1>
      <slot name="nav" />
      <div class="header-right">
        <button class="user-btn" @click="router.push('/user')">
          <span class="user-avatar">{{ userStore.initial }}</span>
          <span class="user-name">{{ userStore.displayName }}</span>
        </button>
      </div>
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

.header-right {
  margin-left: auto;
  flex-shrink: 0;
}

.user-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px 6px 6px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: var(--color-surface);
  cursor: pointer;
  font-family: inherit;
  transition: all var(--transition-fast);
}

.user-btn:hover {
  border-color: var(--color-primary-soft);
  background: var(--color-primary-light);
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--color-primary);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  flex-shrink: 0;
}

.user-name {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text);
}

@media (max-width: 640px) {
  .header-inner { padding: 0 16px; gap: 16px; }
  .app-title { font-size: 16px; }
  .user-name { display: none; }
}
</style>
