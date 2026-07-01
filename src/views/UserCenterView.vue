<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import { useFavoriteStore } from '@/stores/favorite'
import { useRouter } from 'vue-router'

const router = useRouter()
const userStore = useUserStore()
const favoriteStore = useFavoriteStore()

const stats = [
  { num: 12, label: '我的发布' },
  { num: favoriteStore.count, label: '收藏' },
  { num: 5, label: '消息' },
]

const menus = [
  { icon: '📋', label: '我的发布', action: () => router.push('/trade') },
  { icon: '❤️', label: '我的收藏', action: () => {} },
  { icon: '💬', label: '消息中心', action: () => router.push('/message') },
  { icon: '📦', label: '浏览记录', action: () => {} },
  { icon: '⚙️', label: '账号设置', action: () => {} },
]
</script>

<template>
  <div class="user-view">
    <div class="profile-card">
      <div class="avatar-circle">{{ userStore.initial }}</div>
      <div class="profile-info">
        <h3>{{ userStore.displayName }}</h3>
        <p>{{ userStore.user.college }} · {{ userStore.user.campus }}</p>
        <span class="credit-badge">⭐ 信用分 {{ userStore.user.creditScore }}</span>
      </div>
    </div>

    <div class="stats-row">
      <div v-for="s in stats" :key="s.label" class="stat-item">
        <span class="stat-num">{{ s.num }}</span>
        <span class="stat-label">{{ s.label }}</span>
      </div>
    </div>

    <div class="menu-list">
      <button v-for="m in menus" :key="m.label" class="menu-item" @click="m.action()">
        <span>{{ m.icon }}</span>
        <span>{{ m.label }}</span>
        <svg class="menu-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
      </button>
    </div>

    <div class="section">
      <h3 class="section-title">❤️ 我的收藏 ({{ favoriteStore.count }})</h3>
      <div v-if="favoriteStore.favorites.length === 0" class="empty-hint">暂无收藏内容，去集市逛逛吧</div>
      <div v-else class="fav-list">
        <div v-for="fav in favoriteStore.favorites" :key="fav.id" class="fav-item">
          <div class="fav-info">
            <span class="fav-title">{{ fav.title }}</span>
            <span class="fav-meta">{{ fav.campus }} · {{ fav.addedAt }}</span>
          </div>
          <div class="fav-right">
            <span v-if="fav.price" class="fav-price">¥{{ fav.price }}</span>
            <button class="remove-btn" @click.stop="favoriteStore.removeFavorite(fav.id)">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.user-view { display: flex; flex-direction: column; gap: 20px; max-width: 480px; }
.profile-card { display: flex; align-items: center; gap: 16px; padding: 24px; border: 1px solid var(--color-border); border-radius: var(--radius-xl); background: var(--color-surface); }
.avatar-circle { width: 56px; height: 56px; border-radius: 50%; background: var(--color-primary); color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 22px; font-weight: 700; }
.profile-info h3 { font-size: 18px; font-weight: 700; color: var(--color-text); margin-bottom: 2px; letter-spacing: -0.02em; }
.profile-info p { font-size: 13px; color: var(--color-text-secondary); }
.credit-badge { display: inline-block; margin-top: 4px; padding: 2px 10px; border-radius: var(--radius-full); font-size: 12px; font-weight: 600; background: var(--color-primary-light); color: var(--color-primary); }
.stats-row { display: flex; gap: 1px; background: var(--color-border); border-radius: var(--radius-lg); overflow: hidden; }
.stat-item { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 16px 8px; background: var(--color-surface); }
.stat-num { font-size: 22px; font-weight: 700; color: var(--color-primary); }
.stat-label { font-size: 12px; color: var(--color-text-muted); }
.menu-list { display: flex; flex-direction: column; border: 1px solid var(--color-border); border-radius: var(--radius-lg); overflow: hidden; background: var(--color-surface); }
.menu-item { display: flex; align-items: center; gap: 14px; padding: 16px 20px; border: none; border-bottom: 1px solid var(--color-border-light); background: transparent; font-size: 15px; font-weight: 500; color: var(--color-text); font-family: inherit; cursor: pointer; transition: background var(--transition-fast); text-align: left; width: 100%; }
.menu-item:last-child { border-bottom: none; }
.menu-item:hover { background: var(--color-surface-hover); }
.menu-item span:first-child { font-size: 18px; }
.menu-item span:nth-child(2) { flex: 1; }
.menu-arrow { color: var(--color-text-muted); flex-shrink: 0; }
.section { margin-top: 4px; }
.section-title { font-size: 16px; font-weight: 700; color: var(--color-text); margin-bottom: 12px; }
.empty-hint { text-align: center; padding: 24px; color: var(--color-text-muted); font-size: 14px; border: 1px dashed var(--color-border); border-radius: var(--radius-lg); }
.fav-list { display: flex; flex-direction: column; gap: 8px; }
.fav-item { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); }
.fav-info { display: flex; flex-direction: column; gap: 2px; }
.fav-title { font-size: 14px; font-weight: 600; color: var(--color-text); }
.fav-meta { font-size: 12px; color: var(--color-text-muted); }
.fav-right { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.fav-price { font-size: 15px; font-weight: 700; color: var(--color-primary); }
.remove-btn { padding: 4px 12px; border: 1px solid var(--color-border); border-radius: var(--radius-full); background: #fff; font-size: 12px; font-weight: 500; color: var(--color-text-secondary); cursor: pointer; font-family: inherit; transition: all var(--transition-fast); }
.remove-btn:hover { border-color: #F43F5E; color: #F43F5E; }
</style>
