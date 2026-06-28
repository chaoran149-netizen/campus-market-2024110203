<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <div class="app-layout">
    <header class="app-header">
      <h1 class="app-title" @click="router.push('/')">校园轻集市</h1>
      <nav class="app-nav">
        <button :class="{ active: router.currentRoute.value.name === 'home' }" @click="router.push('/')">首页</button>
        <button :class="{ active: router.currentRoute.value.name === 'list' }" @click="router.push('/list')">列表</button>
        <button :class="{ active: router.currentRoute.value.name === 'publish' }" @click="router.push('/publish')">发布</button>
        <button :class="{ active: router.currentRoute.value.name === 'message' }" @click="router.push('/message')">消息</button>
        <button :class="{ active: router.currentRoute.value.name === 'profile' }" @click="router.push('/profile')">个人</button>
        <button :class="{ active: router.currentRoute.value.name === 'board' }" @click="router.push('/board')">看板</button>
      </nav>
    </header>
    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-layout { min-height: 100vh; display: flex; flex-direction: column; }
.app-header { display: flex; align-items: center; gap: 24px; padding: 12px 32px; border-bottom: 1px solid #e0e0e0; background: #fff; }
.app-title { font-size: 20px; cursor: pointer; margin: 0; color: #409eff; white-space: nowrap; }
.app-nav { display: flex; gap: 8px; flex-wrap: wrap; }
.app-nav button { padding: 6px 16px; border: 1px solid #dcdfe6; background: #fff; border-radius: 4px; cursor: pointer; font-size: 14px; }
.app-nav button:hover { color: #409eff; border-color: #409eff; }
.app-nav button.active { background: #409eff; color: #fff; border-color: #409eff; }
.app-main { flex: 1; padding: 16px; }
</style>
