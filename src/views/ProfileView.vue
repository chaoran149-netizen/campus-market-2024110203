<script setup lang="ts">
import { ref } from 'vue'

const user = ref({
  nickname: '校园用户',
  college: '计算机学院',
  campus: '主校区',
  creditScore: 85,
  joinDays: 7,
})

const myPosts = ref([
  { id: 1, title: '出售二手教材', status: '进行中' },
  { id: 2, title: '求组学习搭子', status: '已完成' },
])

const myFavorites = ref([
  { id: 3, title: '蓝牙耳机 九成新' },
  { id: 4, title: '奶茶拼单！一点点' },
])
</script>

<template>
  <div class="profile-view">
    <h2 class="page-title">👤 个人中心</h2>

    <div class="user-card">
      <div class="user-avatar">{{ user.nickname[0] }}</div>
      <div class="user-info">
        <h3>{{ user.nickname }}</h3>
        <p class="user-meta">{{ user.college }} · {{ user.campus }}</p>
        <div class="user-stats">
          <span class="stat-item">
            <span class="stat-num">⭐ {{ user.creditScore }}</span>
            <span class="stat-label">信用分</span>
          </span>
          <span class="stat-item">
            <span class="stat-num">📅 {{ user.joinDays }}</span>
            <span class="stat-label">加入天数</span>
          </span>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-title">
        <span>📋</span>
        <h3>我的发布</h3>
      </div>
      <div class="list-items">
        <div v-for="post in myPosts" :key="post.id" class="list-item">
          <span class="item-title">{{ post.title }}</span>
          <span class="item-status">{{ post.status }}</span>
        </div>
        <div v-if="!myPosts.length" class="empty-text">还没有发布过信息</div>
      </div>
    </div>

    <div class="section">
      <div class="section-title">
        <span>❤️</span>
        <h3>我的收藏</h3>
      </div>
      <div class="list-items">
        <div v-for="fav in myFavorites" :key="fav.id" class="list-item">
          <span class="item-title">{{ fav.title }}</span>
          <span class="item-arrow">→</span>
        </div>
        <div v-if="!myFavorites.length" class="empty-text">还没有收藏</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-title {
  font-size: 22px;
  font-weight: 900;
  margin-bottom: 20px;
}

.user-card {
  display: flex;
  gap: 18px;
  align-items: center;
  padding: 20px;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  background: #FFFDF5;
  box-shadow: 6px 6px 0px var(--doodle-border);
  margin-bottom: 28px;
}

.user-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: var(--doodle-yellow);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  font-weight: 900;
  border: 3px solid var(--doodle-border);
  flex-shrink: 0;
}

.user-info h3 {
  font-size: 18px;
  font-weight: 900;
  margin-bottom: 2px;
}

.user-meta {
  font-size: 13px;
  color: #A16207;
  margin-bottom: 10px;
}

.user-stats {
  display: flex;
  gap: 20px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-num {
  font-weight: 900;
  font-size: 15px;
  color: var(--doodle-text);
}

.stat-label {
  font-size: 11px;
  color: #A16207;
}

.section {
  margin-bottom: 24px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.section-title h3 {
  font-size: 16px;
  font-weight: 900;
}

.list-items {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  cursor: pointer;
  transition: all 0.15s;
}

.list-item:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.item-title {
  font-weight: 700;
  font-size: 14px;
}

.item-status {
  font-size: 12px;
  padding: 2px 12px;
  border-radius: 10px;
  background: var(--doodle-cream);
  border: 1.5px solid var(--doodle-border);
  color: #A16207;
  font-weight: 700;
}

.item-arrow {
  color: #A16207;
  font-weight: 700;
}

.empty-text {
  font-size: 13px;
  color: #A16207;
  text-align: center;
  padding: 20px;
  border: 2px dashed var(--doodle-border);
  border-radius: var(--doodle-radius);
}
</style>
