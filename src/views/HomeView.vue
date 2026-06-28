<script setup lang="ts"></script>

<template>
  <div class="home-view">
    <div class="welcome-card">
      <h2>欢迎来到校园轻集市</h2>
      <p>二手交易 · 失物招领 · 拼单搭子 · 跑腿委托</p>
    </div>
    <div class="quick-links">
      <router-link to="/list" class="quick-card">浏览集市</router-link>
      <router-link to="/publish" class="quick-card">发布信息</router-link>
      <router-link to="/message" class="quick-card">消息中心</router-link>
      <router-link to="/profile" class="quick-card">个人中心</router-link>
      <router-link to="/board" class="quick-card">趋势看板</router-link>
    </div>
    <div class="info-section">
      <h3>最新信息</h3>
      <div v-for="i in 3" :key="i" class="info-card">
        <router-link :to="'/detail/' + i">
          <h4>示例物品 {{ i }}</h4>
          <p>二手交易 · 主校区 · ￥{{ i * 15 }}</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-view { padding: 16px; }
.welcome-card { text-align: center; padding: 32px; background: linear-gradient(135deg, #667eea, #764ba2); color: #fff; border-radius: 12px; margin-bottom: 24px; }
.welcome-card h2 { margin: 0 0 8px; }
.quick-links { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
.quick-card { flex: 1; min-width: 100px; padding: 20px; text-align: center; border: 1px solid #e0e0e0; border-radius: 8px; text-decoration: none; color: #333; font-weight: bold; }
.quick-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.info-section h3 { margin-bottom: 12px; }
.info-card { padding: 12px; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 8px; }
.info-card a { text-decoration: none; color: inherit; }
.info-card h4 { margin: 0 0 4px; }
.info-card p { margin: 0; color: #666; font-size: 14px; }
</style>
