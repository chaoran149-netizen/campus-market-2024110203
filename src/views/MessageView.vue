<script setup lang="ts">
import { ref } from 'vue'

const conversations = ref([
  { id: 1, user: '张三', lastMsg: '这个还卖吗？', unread: 2 },
  { id: 2, user: '李四', lastMsg: '好的，谢谢', unread: 0 },
  { id: 3, user: '王五', lastMsg: '明天下午可以吗？', unread: 1 },
])
</script>

<template>
  <div class="message-view">
    <h2>消息中心</h2>
    <div class="conv-list">
      <div v-for="conv in conversations" :key="conv.id" class="conv-item">
        <div class="conv-info">
          <span class="conv-user">{{ conv.user }}</span>
          <span class="conv-msg">{{ conv.lastMsg }}</span>
        </div>
        <span v-if="conv.unread" class="unread-badge">{{ conv.unread }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.message-view { padding: 16px; }
.conv-list { display: flex; flex-direction: column; gap: 8px; }
.conv-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; border: 1px solid #e0e0e0; border-radius: 8px; cursor: pointer; }
.conv-item:hover { background: #f5f7fa; }
.conv-info { display: flex; flex-direction: column; gap: 4px; }
.conv-user { font-weight: bold; }
.conv-msg { color: #666; font-size: 13px; }
.unread-badge { background: #e74c3c; color: #fff; border-radius: 50%; padding: 2px 8px; font-size: 12px; }
</style>
