<script setup lang="ts"></script>

<template>
  <div class="message-view">
    <div class="page-top">
      <h2>消息</h2>
      <p>与你相关的私信和系统通知</p>
    </div>

    <div class="tab-bar">
      <button class="tab active">全部</button>
      <button class="tab">未读</button>
    </div>

    <div class="msg-list">
      <div v-for="i in 6" :key="i" class="msg-card" :class="{ unread: i <= 2 }">
        <div class="msg-avatar" :style="{ background: ['#EEF2FF','#D1FAE5','#FEF3C7','#F3E8FF','#FCE7F3','#E5E7EB'][i-1], color: ['#4F46E5','#059669','#D97706','#7C3AED','#BE185D','#6B7280'][i-1] }">
          {{ ['👤','🛒','📢','👥','🏃','🔔'][i-1] }}
        </div>
        <div class="msg-body">
          <div class="msg-header">
            <span class="msg-name">{{ ['李同学','系统通知','集市小助手','王同学','张同学','交易提醒'][i-1] }}</span>
            <span class="msg-time">{{ ['10分钟前','1小时前','昨天','昨天','2天前','3天前'][i-1] }}</span>
          </div>
          <p class="msg-preview">{{ ['你好，蓝牙耳机还在吗？','你的二手教材已被收藏','拼单搭子有新的组队请求','足球组队还差人吗？','菜鸟驿站的快递已取到','安全交易小贴士已更新'][i-1] }}</p>
        </div>
        <span v-if="i <= 2" class="unread-dot"></span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.message-view { display: flex; flex-direction: column; gap: 24px; max-width: 600px; }

.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }

/* ── Tabs ── */
.tab-bar { display: flex; gap: 8px; }
.tab {
  padding: 8px 20px; border: 1px solid var(--color-border); border-radius: var(--radius-full);
  background: var(--color-surface); font-size: 13px; font-weight: 500; font-family: inherit;
  color: var(--color-text-secondary); cursor: pointer; transition: all var(--transition-fast);
}
.tab.active { background: var(--color-primary); color: #fff; border-color: var(--color-primary); }

/* ── Message List ── */
.msg-list { display: flex; flex-direction: column; gap: 2px; }

.msg-card {
  display: flex; align-items: center; gap: 14px; padding: 14px 18px;
  border-radius: var(--radius-lg); transition: background var(--transition-fast); cursor: pointer; position: relative;
}
.msg-card:hover { background: var(--color-surface-hover); }

.msg-avatar {
  width: 44px; height: 44px; border-radius: var(--radius-md); display: flex;
  align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0;
}

.msg-body { flex: 1; min-width: 0; }
.msg-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px; }
.msg-name { font-size: 14px; font-weight: 600; color: var(--color-text); }
.msg-time { font-size: 12px; color: var(--color-text-muted); flex-shrink: 0; }
.msg-preview { font-size: 13px; color: var(--color-text-secondary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.unread-dot {
  width: 8px; height: 8px; border-radius: 50%; background: var(--color-primary);
  position: absolute; right: 18px; top: 50%; transform: translateY(-50%);
}
.msg-card.unread .msg-name { font-weight: 700; }
.msg-card.unread .msg-preview { color: var(--color-text); }
</style>
