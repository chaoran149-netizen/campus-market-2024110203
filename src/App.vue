<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <div class="app-layout">
    <header class="app-header">
      <h1 class="app-title" @click="router.push('/')">校园轻集市</h1>
      <nav class="app-nav">
        <button :class="{ active: router.currentRoute.value.name === 'home' }" @click="router.push('/')">🏠 首页</button>
        <button :class="{ active: router.currentRoute.value.name === 'list' }" @click="router.push('/list')">📋 列表</button>
        <button :class="{ active: router.currentRoute.value.name === 'publish' }" @click="router.push('/publish')">✏️ 发布</button>
        <button :class="{ active: router.currentRoute.value.name === 'message' }" @click="router.push('/message')">💬 消息</button>
        <button :class="{ active: router.currentRoute.value.name === 'profile' }" @click="router.push('/profile')">👤 个人</button>
        <button :class="{ active: router.currentRoute.value.name === 'board' }" @click="router.push('/board')">📊 看板</button>
      </nav>
    </header>
    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Noto Sans SC', system-ui, sans-serif;
  background: #FFF8F0;
  color: #3D2C1B;
  line-height: 1.6;
}

:root {
  --doodle-yellow: #F59E0B;
  --doodle-red: #EF4444;
  --doodle-cream: #FEF3C7;
  --doodle-bg: #FFF8F0;
  --doodle-text: #3D2C1B;
  --doodle-border: #D97706;
  --doodle-radius: 18px;
  --doodle-shadow: 4px 4px 0px #D97706;
}
</style>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

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
}

.app-title:hover {
  transform: rotate(-1deg);
}

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

.app-main {
  flex: 1;
  padding: 24px 32px;
  max-width: 960px;
  width: 100%;
  margin: 0 auto;
}
</style>
