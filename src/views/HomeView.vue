<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getTrades } from '@/api/trade'

interface Trade {
  id: number; title: string; price: number;
  category: string; campus: string;
}

const latestItems = ref<Trade[]>([])

onMounted(async () => {
  try {
    const res = await getTrades()
    latestItems.value = res.data.slice(0, 4)
  } catch { /* use fallback */ }
})
</script>

<template>
  <div class="home-view">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-badge">校园生活服务平台</div>
      <h1>今天，在集市发现什么？</h1>
      <p>二手好物 · 失物招领 · 组队拼单 · 跑腿帮忙 — 一个轻量的校园互助空间</p>
    </section>

    <!-- Quick Actions -->
    <section class="quick-actions">
      <router-link to="/trade" class="action-card">
        <div class="action-icon trade-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        </div>
        <span class="action-label">逛集市</span>
        <span class="action-sub">二手交易</span>
      </router-link>
      <router-link to="/publish" class="action-card">
        <div class="action-icon pub-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        </div>
        <span class="action-label">发布信息</span>
        <span class="action-sub">快速发布</span>
      </router-link>
      <router-link to="/group-buy" class="action-card">
        <div class="action-icon group-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <span class="action-label">拼单搭子</span>
        <span class="action-sub">组队找人</span>
      </router-link>
      <router-link to="/message" class="action-card">
        <div class="action-icon msg-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        </div>
        <span class="action-label">消息</span>
        <span class="action-sub">查看通知</span>
      </router-link>
    </section>

    <!-- Latest Items -->
    <section class="section-block">
      <div class="section-header">
        <h2>最新发布</h2>
        <router-link to="/trade" class="see-all">查看全部 →</router-link>
      </div>
      <div class="item-grid">
        <router-link v-for="item in latestItems" :key="item.id" :to="'/detail/' + item.id" class="item-card">
          <span class="item-emoji">{{ item.category === '教材书籍' ? '📚' : item.category === '数码电子' ? '🎧' : item.category === '生活用品' ? '🚲' : '⌨️' }}</span>
          <div class="item-info">
            <h4>{{ item.title }}</h4>
            <span class="item-price">¥{{ item.price }}</span>
            <span class="item-campus">{{ item.campus }}</span>
          </div>
        </router-link>
      </div>
    </section>

    <!-- Safety Tips -->
    <section class="tips-card">
      <div class="tips-icon">🛡️</div>
      <div class="tips-content">
        <h3>安全交易小贴士</h3>
        <p>选择教学楼、食堂等公共区域交易 · 保护好个人信息 · 遇到可疑行为及时举报</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

/* ── Hero ── */
.hero {
  text-align: center;
  padding: 48px 24px;
  background: linear-gradient(135deg, var(--color-primary-light) 0%, #F5F3FF 50%, var(--color-bg) 100%);
  border-radius: var(--radius-2xl);
  border: 1px solid var(--color-border-light);
}

.hero-badge {
  display: inline-block;
  padding: 4px 14px;
  background: var(--color-primary-soft);
  color: var(--color-primary);
  border-radius: var(--radius-full);
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 16px;
}

.hero h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--color-text);
  letter-spacing: -0.03em;
  margin-bottom: 8px;
}

.hero p {
  font-size: 15px;
  color: var(--color-text-secondary);
  max-width: 480px;
  margin: 0 auto;
}

/* ── Quick Actions ── */
.quick-actions {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.action-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 20px 12px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition);
}

.action-card:hover {
  border-color: var(--color-primary-soft);
  background: var(--color-primary-light);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.action-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 2px;
}

.trade-icon { background: #EEF2FF; color: var(--color-primary); }
.pub-icon  { background: #FEF3C7; color: #D97706; }
.group-icon { background: #D1FAE5; color: #059669; }
.msg-icon  { background: #FCE7F3; color: #BE185D; }

.action-label {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text);
}

.action-sub {
  font-size: 12px;
  color: var(--color-text-muted);
}

/* ── Section Block ── */
.section-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-header h2 {
  font-size: 18px;
  font-weight: 700;
  color: var(--color-text);
  letter-spacing: -0.02em;
}

.see-all {
  font-size: 13px;
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
  transition: color var(--transition-fast);
}

.see-all:hover { color: var(--color-primary-hover); }

/* ── Item Grid ── */
.item-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 12px;
}

.item-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition);
}

.item-card:hover {
  border-color: var(--color-border-hover);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.item-emoji { font-size: 32px; flex-shrink: 0; }

.item-info { flex: 1; min-width: 0; }

.item-info h4 {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.item-price {
  font-size: 15px;
  font-weight: 700;
  color: var(--color-primary);
  margin-right: 8px;
}

.item-campus {
  font-size: 12px;
  color: var(--color-text-muted);
}

/* ── Tips Card ── */
.tips-card {
  display: flex;
  gap: 16px;
  padding: 20px 24px;
  background: var(--color-accent-light);
  border-radius: var(--radius-lg);
  border: 1px solid #FDE68A;
}

.tips-icon { font-size: 28px; flex-shrink: 0; }

.tips-content h3 {
  font-size: 15px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 4px;
}

.tips-content p {
  font-size: 13px;
  color: var(--color-text-secondary);
  line-height: 1.5;
}

@media (max-width: 640px) {
  .hero { padding: 36px 16px; }
  .hero h1 { font-size: 24px; }

  .quick-actions { grid-template-columns: repeat(2, 1fr); }

  .item-grid { grid-template-columns: 1fr; }
}
</style>
