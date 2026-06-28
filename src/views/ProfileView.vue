<script setup lang="ts">
import { ref } from 'vue'

const user = ref({
  nickname: '校园用户',
  college: '计算机学院',
  campus: '主校区',
  creditScore: 85,
})

const myPosts = ref([
  { id: 1, title: '出售二手教材', status: '进行中' },
  { id: 2, title: '求组学习搭子', status: '已完成' },
])
</script>

<template>
  <div class="profile-view">
    <h2>个人中心</h2>
    <div class="user-card">
      <div class="avatar">{{ user.nickname[0] }}</div>
      <div class="user-info">
        <h3>{{ user.nickname }}</h3>
        <p>{{ user.college }} · {{ user.campus }}</p>
        <p class="credit">信用分：{{ user.creditScore }}</p>
      </div>
    </div>
    <div class="section">
      <h3>我的发布</h3>
      <div v-for="post in myPosts" :key="post.id" class="post-item">
        <span>{{ post.title }}</span>
        <span class="status-tag">{{ post.status }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-view { padding: 16px; max-width: 600px; }
.user-card { display: flex; gap: 16px; align-items: center; padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 24px; }
.avatar { width: 56px; height: 56px; border-radius: 50%; background: #409eff; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 24px; }
.user-info h3 { margin: 0; }
.credit { color: #e67e22; font-weight: bold; }
.section { margin-bottom: 24px; }
.post-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
.status-tag { font-size: 12px; padding: 2px 8px; border-radius: 4px; background: #f0f0f0; }
</style>
