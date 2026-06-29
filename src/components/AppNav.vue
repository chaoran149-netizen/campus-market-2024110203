<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

interface NavItem {
  path: string
  name: string
  label: string
}

const navItems: NavItem[] = [
  { path: '/',           name: 'home',        label: '首页' },
  { path: '/trade',      name: 'trade',       label: '二手交易' },
  { path: '/lost-found', name: 'lost-found',  label: '失物招领' },
  { path: '/group-buy',  name: 'group-buy',   label: '拼单搭子' },
  { path: '/errand',     name: 'errand',      label: '跑腿委托' },
  { path: '/publish',    name: 'publish',     label: '发布' },
  { path: '/message',    name: 'message',     label: '消息' },
  { path: '/user',       name: 'user',        label: '我的' },
]
</script>

<template>
  <nav class="app-nav">
    <button
      v-for="item in navItems"
      :key="item.name"
      :class="{ active: router.currentRoute.value.name === item.name }"
      @click="router.push(item.path)"
    >
      {{ item.label }}
    </button>
  </nav>
</template>

<style scoped>
.app-nav {
  display: flex;
  gap: 4px;
  flex-wrap: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
}

.app-nav::-webkit-scrollbar { display: none; }

.app-nav button {
  padding: 8px 16px;
  border: none;
  border-radius: var(--radius-full);
  background: transparent;
  color: var(--color-text-secondary);
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  font-family: inherit;
  white-space: nowrap;
  transition: all var(--transition-fast);
  position: relative;
}

.app-nav button:hover {
  background: var(--color-primary-light);
  color: var(--color-primary);
}

.app-nav button.active {
  background: var(--color-primary);
  color: var(--color-text-inverse);
  box-shadow: var(--shadow-sm);
}

@media (max-width: 768px) {
  .app-nav { overflow-x: auto; }

  .app-nav button {
    padding: 6px 12px;
    font-size: 13px;
  }
}
</style>
