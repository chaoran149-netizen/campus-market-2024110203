<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useFavoriteStore } from '@/stores/favorite'
import { getTrades, deleteTrade } from '@/api/trade'
import { getLostFounds, deleteLostFound } from '@/api/lostFound'
import { getGroupBuys, deleteGroupBuy } from '@/api/groupBuy'
import { getErrands, deleteErrand } from '@/api/errand'

const router = useRouter()
const userStore = useUserStore()
const favoriteStore = useFavoriteStore()

interface MyPost { id: number; title: string; type: string; collection: string; time: string; price?: number }
const myPosts = ref<MyPost[]>([])
const postsLoading = ref(false)

const publishCount = computed(() => myPosts.value.length)

async function loadMyPosts() {
  if (!userStore.isLoggedIn) { myPosts.value = []; return }
  postsLoading.value = true
  try {
    const nickname = userStore.displayName
    const [trades, lostFounds, groupBuys, errands] = await Promise.all([
      getTrades(), getLostFounds(), getGroupBuys(), getErrands(),
    ])
    myPosts.value = [
      ...trades.data.filter((t: { publisher: string }) => t.publisher === nickname).map((t: { id: number; title: string; price: number; publishTime: string }) => ({ id: t.id, title: t.title, type: '二手交易', collection: 'trades', time: t.publishTime, price: t.price })),
      ...lostFounds.data.filter((t: { contact: string }) => t.contact === nickname).map((t: { id: number; title: string; time: string }) => ({ id: t.id, title: t.title, type: '失物招领', collection: 'lostFounds', time: t.time })),
      ...groupBuys.data.filter((t: { publisher: string }) => t.publisher === nickname).map((t: { id: number; title: string; deadline: string }) => ({ id: t.id, title: t.title, type: '拼单搭子', collection: 'groupBuys', time: t.deadline })),
      ...errands.data.filter((t: { publisher: string }) => t.publisher === nickname).map((t: { id: number; title: string; deadline: string; reward: number }) => ({ id: t.id, title: t.title, type: '跑腿委托', collection: 'errands', time: t.deadline, price: t.reward })),
    ]
  } catch { myPosts.value = [] }
  finally { postsLoading.value = false }
}

onMounted(loadMyPosts)

async function handleDelete(post: MyPost) {
  if (!confirm(`确定要删除「${post.title}」吗？`)) return
  try {
    if (post.collection === 'trades') await deleteTrade(post.id)
    else if (post.collection === 'lostFounds') await deleteLostFound(post.id)
    else if (post.collection === 'groupBuys') await deleteGroupBuy(post.id)
    else if (post.collection === 'errands') await deleteErrand(post.id)
    myPosts.value = myPosts.value.filter(p => p.id !== post.id || p.collection !== post.collection)
  } catch { alert('删除失败，请检查 Mock 服务') }
}

const stats = computed(() => [
  { num: publishCount.value, label: '我的发布' },
  { num: favoriteStore.count, label: '收藏' },
  { num: 5, label: '消息' },
])

const menus = [
  { icon: '💬', label: '消息中心', action: () => router.push('/message') },
  { icon: '⚙️', label: '账号设置', action: () => {} },
]
</script>

<template>
  <div class="user-view">
    <!-- 未登录 -->
    <div v-if="!userStore.isLoggedIn" class="login-prompt">
      <div class="avatar-circle">?</div>
      <h3>尚未登录</h3>
      <p>登录后查看个人信息和收藏</p>
      <button class="to-login-btn" @click="router.push('/login')">去登录</button>
    </div>

    <!-- 已登录 -->
    <template v-else>
    <div class="profile-card">
      <div class="avatar-circle">{{ userStore.initial }}</div>
      <div class="profile-info">
        <h3>{{ userStore.displayName }}</h3>
        <p>{{ userStore.currentUser?.college ?? '' }} · {{ userStore.currentUser?.campus ?? '' }}</p>
      </div>
    </div>

    <div class="stats-row">
      <div v-for="s in stats" :key="s.label" class="stat-item">
        <span class="stat-num">{{ s.num }}</span>
        <span class="stat-label">{{ s.label }}</span>
      </div>
    </div>

    <!-- 我的发布 -->
    <div class="section">
      <h3 class="section-title">📋 我的发布 ({{ publishCount }})</h3>
      <div v-if="myPosts.length === 0" class="empty-hint">还没有发布过内容</div>
      <div v-else class="post-list">
        <div v-for="post in myPosts" :key="post.collection + post.id" class="post-item">
          <div class="post-info">
            <span class="post-type">{{ post.type }}</span>
            <span class="post-title">{{ post.title }}</span>
            <span class="post-time">{{ post.time }}</span>
          </div>
          <button class="delete-btn" @click="handleDelete(post)">删除</button>
        </div>
      </div>
    </div>

    <!-- 收藏 -->
    <div class="section">
      <h3 class="section-title">❤️ 我的收藏 ({{ favoriteStore.count }})</h3>
      <div v-if="favoriteStore.favorites.length === 0" class="empty-hint">暂无收藏内容</div>
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

    <div class="menu-list">
      <button v-for="m in menus" :key="m.label" class="menu-item" @click="m.action()">
        <span>{{ m.icon }}</span>
        <span>{{ m.label }}</span>
        <svg class="menu-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
      </button>
    </div>
    </template>
  </div>
</template>

<style scoped>
.user-view { display: flex; flex-direction: column; gap: 20px; max-width: 520px; }

.login-prompt { display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 48px 24px; border: 1px solid var(--color-border); border-radius: var(--radius-xl); background: var(--color-surface); text-align: center; }
.login-prompt .avatar-circle { width: 64px; height: 64px; font-size: 26px; }
.login-prompt h3 { font-size: 18px; font-weight: 700; }
.login-prompt p { font-size: 14px; color: var(--color-text-secondary); }
.to-login-btn { padding: 10px 32px; border: none; border-radius: var(--radius-md); background: var(--color-primary); color: #fff; font-size: 14px; font-weight: 600; font-family: inherit; cursor: pointer; transition: all var(--transition); }
.to-login-btn:hover { background: var(--color-primary-hover); }

.profile-card { display: flex; align-items: center; gap: 16px; padding: 24px; border: 1px solid var(--color-border); border-radius: var(--radius-xl); background: var(--color-surface); }
.avatar-circle { width: 56px; height: 56px; border-radius: 50%; background: var(--color-primary); color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 22px; font-weight: 700; }
.profile-info h3 { font-size: 18px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 2px; }
.profile-info p { font-size: 13px; color: var(--color-text-secondary); }

.stats-row { display: flex; gap: 1px; background: var(--color-border); border-radius: var(--radius-lg); overflow: hidden; }
.stat-item { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 16px 8px; background: var(--color-surface); }
.stat-num { font-size: 22px; font-weight: 700; color: var(--color-primary); }
.stat-label { font-size: 12px; color: var(--color-text-muted); }

.section { margin-top: 4px; }
.section-title { font-size: 16px; font-weight: 700; margin-bottom: 12px; }
.empty-hint { text-align: center; padding: 24px; color: var(--color-text-muted); font-size: 14px; border: 1px dashed var(--color-border); border-radius: var(--radius-lg); }

/* 我的发布列表 */
.post-list { display: flex; flex-direction: column; gap: 6px; }
.post-item { display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 12px 16px; border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); }
.post-info { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1; }
.post-type { font-size: 11px; font-weight: 600; color: var(--color-primary); }
.post-title { font-size: 14px; font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.post-time { font-size: 12px; color: var(--color-text-muted); }
.delete-btn { padding: 6px 14px; border: 1px solid var(--color-border); border-radius: var(--radius-full); background: #fff; font-size: 12px; font-weight: 500; color: var(--color-text-secondary); cursor: pointer; font-family: inherit; white-space: nowrap; flex-shrink: 0; transition: all var(--transition-fast); }
.delete-btn:hover { border-color: #F43F5E; color: #F43F5E; background: #FFF1F2; }

/* 收藏 */
.fav-list { display: flex; flex-direction: column; gap: 8px; }
.fav-item { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); }
.fav-info { display: flex; flex-direction: column; gap: 2px; }
.fav-title { font-size: 14px; font-weight: 600; }
.fav-meta { font-size: 12px; color: var(--color-text-muted); }
.fav-right { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.fav-price { font-size: 15px; font-weight: 700; color: #F43F5E; }
.remove-btn { padding: 4px 12px; border: 1px solid var(--color-border); border-radius: var(--radius-full); background: #fff; font-size: 12px; font-weight: 500; color: var(--color-text-secondary); cursor: pointer; font-family: inherit; transition: all var(--transition-fast); }
.remove-btn:hover { border-color: #F43F5E; color: #F43F5E; }

.menu-list { display: flex; flex-direction: column; border: 1px solid var(--color-border); border-radius: var(--radius-lg); overflow: hidden; background: var(--color-surface); }
.menu-item { display: flex; align-items: center; gap: 14px; padding: 16px 20px; border: none; border-bottom: 1px solid var(--color-border-light); background: transparent; font-size: 15px; font-weight: 500; font-family: inherit; cursor: pointer; transition: background var(--transition-fast); text-align: left; width: 100%; }
.menu-item:last-child { border-bottom: none; }
.menu-item:hover { background: var(--color-surface-hover); }
.menu-item span:first-child { font-size: 18px; }
.menu-item span:nth-child(2) { flex: 1; }
.menu-arrow { color: var(--color-text-muted); flex-shrink: 0; }
</style>
