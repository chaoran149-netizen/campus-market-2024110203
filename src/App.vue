<script setup lang="ts">
import AppLayout from '@/components/AppLayout.vue'
import AppHeader from '@/components/AppHeader.vue'
import AppNav from '@/components/AppNav.vue'
</script>

<template>
  <AppLayout>
    <template #header>
      <AppHeader>
        <template #nav>
          <AppNav />
        </template>
      </AppHeader>
    </template>
  </AppLayout>
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
