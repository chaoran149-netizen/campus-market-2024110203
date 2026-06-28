<script setup lang="ts">
import { ref } from 'vue'

const conversations = ref([
  { id: 1, user: '张三', avatar: '🧑‍🎓', lastMsg: '这个还卖吗？', unread: 2, time: '10:32' },
  { id: 2, user: '李四', avatar: '👩‍🎓', lastMsg: '好的，谢谢！', unread: 0, time: '昨天' },
  { id: 3, user: '王五', avatar: '🧑‍💻', lastMsg: '明天下午可以吗？', unread: 1, time: '昨天' },
  { id: 4, user: '赵六', avatar: '👨‍🌾', lastMsg: '我在3号教学楼等你', unread: 0, time: '6/26' },
])
</script>

<template>
  <div class="message-view">
    <div class="msg-header">
      <h2>💬 消息</h2>
      <span class="total-badge">{{ conversations.filter(c => c.unread).length }} 条未读</span>
    </div>

    <div class="conv-list">
      <div v-for="conv in conversations" :key="conv.id" class="conv-item">
        <div class="conv-avatar">{{ conv.avatar }}</div>
        <div class="conv-info">
          <div class="conv-top">
            <span class="conv-user">{{ conv.user }}</span>
            <span class="conv-time">{{ conv.time }}</span>
          </div>
          <div class="conv-bottom">
            <span class="conv-msg" :class="{ unread: conv.unread }">{{ conv.lastMsg }}</span>
            <span v-if="conv.unread" class="unread-badge">{{ conv.unread }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="empty-state" v-if="!conversations.length">
      <p>📭 还没有消息，去集市逛逛吧</p>
    </div>
  </div>
</template>

<style scoped>
.msg-header {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 16px;
}

.msg-header h2 {
  font-size: 22px;
  font-weight: 900;
}

.total-badge {
  font-size: 13px;
  padding: 2px 12px;
  border: 2px solid var(--doodle-border);
  border-radius: 20px;
  background: var(--doodle-cream);
  font-weight: 700;
  color: #A16207;
}

.conv-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.conv-item {
  display: flex;
  gap: 14px;
  align-items: center;
  padding: 14px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  cursor: pointer;
  background: #FFFDF5;
  transition: all 0.15s;
}

.conv-item:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.conv-avatar {
  font-size: 36px;
  flex-shrink: 0;
}

.conv-info {
  flex: 1;
  min-width: 0;
}

.conv-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.conv-user {
  font-weight: 900;
  font-size: 15px;
}

.conv-time {
  font-size: 12px;
  color: #A16207;
}

.conv-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.conv-msg {
  font-size: 13px;
  color: #A16207;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 220px;
}

.conv-msg.unread {
  color: var(--doodle-text);
  font-weight: 700;
}

.unread-badge {
  background: var(--doodle-red);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 1px 8px;
  border-radius: 10px;
  flex-shrink: 0;
}

.empty-state {
  text-align: center;
  padding: 40px;
  border: 2.5px dashed var(--doodle-border);
  border-radius: var(--doodle-radius);
  color: #A16207;
}
</style>
