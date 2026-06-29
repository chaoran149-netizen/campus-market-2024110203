<script setup lang="ts"></script>

<template>
  <div class="app-layout">
    <slot name="header" />
    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-main {
  flex: 1;
  padding: 32px var(--content-padding) 64px;
  max-width: var(--content-width);
  width: 100%;
  margin: 0 auto;
}

@media (max-width: 640px) {
  .app-main {
    padding: 20px 16px 48px;
  }
}
</style>
