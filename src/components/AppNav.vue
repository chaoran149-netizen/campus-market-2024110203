<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

interface NavItem {
  path: string
  name: string
  label: string
}

const navItems: NavItem[] = [
  { path: '/',           name: 'home',        label: '🏠 首页' },
  { path: '/trade',      name: 'trade',       label: '📋 二手交易' },
  { path: '/lost-found', name: 'lost-found',  label: '🔍 失物招领' },
  { path: '/group-buy',  name: 'group-buy',   label: '👥 拼单搭子' },
  { path: '/errand',     name: 'errand',      label: '🏃 跑腿委托' },
  { path: '/publish',    name: 'publish',     label: '✏️ 发布' },
  { path: '/message',    name: 'message',     label: '💬 消息' },
  { path: '/user',       name: 'user',        label: '👤 我的' },
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
  gap: 8px;
  flex-wrap: wrap;
}

.app-nav button {
  padding: 8px 16px;
  border: 2.5px solid var(--doodle-border);
  background: #FFFDF5;
  color: var(--doodle-text);
  border-radius: var(--doodle-radius);
  cursor: pointer;
  font-size: 14px;
  font-weight: 700;
  font-family: inherit;
  transition: all 0.15s;
}

.app-nav button:hover {
  background: var(--doodle-cream);
  transform: rotate(-2deg) scale(1.05);
}

.app-nav button.active {
  background: var(--doodle-yellow);
  color: #fff;
  border-color: var(--doodle-yellow);
  box-shadow: var(--doodle-shadow);
  transform: rotate(1deg);
}

@media (max-width: 640px) {
  .app-nav {
    gap: 6px;
  }

  .app-nav button {
    padding: 6px 10px;
    font-size: 12px;
  }
}
</style>
