<script setup lang="ts"></script>

<template>
  <div class="home-view">
    <div class="welcome-card">
      <div class="welcome-icon">🎒</div>
      <h2>嘿，今天逛集市了吗？</h2>
      <p>二手好物 · 失物招领 · 组队拼单 · 跑腿帮忙</p>
    </div>

    <div class="quick-links">
      <router-link to="/list" class="quick-card quick-list">📋 逛集市</router-link>
      <router-link to="/publish" class="quick-card quick-pub">✏️ 发布</router-link>
      <router-link to="/message" class="quick-card quick-msg">💬 消息</router-link>
      <router-link to="/profile" class="quick-card quick-profile">👤 我的</router-link>
    </div>

    <div class="section">
      <div class="section-title">
        <span class="section-mark">🔥</span>
        <h3>最新出炉</h3>
      </div>
      <div class="info-list">
        <router-link v-for="i in 4" :key="i" :to="'/detail/' + i" class="info-card">
          <div class="card-left">
            <div class="card-emoji">{{ ['📚', '🎧', '🚲', '💡'][i - 1] }}</div>
          </div>
          <div class="card-body">
            <h4>{{ ['二手教材', '蓝牙耳机', '校园自行车', '台灯'][i - 1] }}</h4>
            <p class="card-meta">￥{{ i * 15 }} · 主校区</p>
          </div>
        </router-link>
      </div>
    </div>

    <div class="section">
      <div class="section-title">
        <span class="section-mark">📢</span>
        <h3>安全小贴士</h3>
      </div>
      <div class="tip-card">
        <p>📍 尽量选择教学楼、食堂等公共区域交易</p>
        <p>🔒 保护好个人联系方式，谨防诈骗</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.welcome-card {
  text-align: center;
  padding: 36px 24px 28px;
  background: #FFFDF5;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  box-shadow: 6px 6px 0px var(--doodle-border);
  position: relative;
}

.welcome-card::after {
  content: '';
  position: absolute;
  top: 6px; left: 6px;
  width: 100%; height: 100%;
  border: 2px dashed var(--doodle-yellow);
  border-radius: 24px;
  pointer-events: none;
}

.welcome-icon {
  font-size: 48px;
  margin-bottom: 8px;
}

.welcome-card h2 {
  font-size: 22px;
  font-weight: 900;
  color: var(--doodle-red);
  margin-bottom: 6px;
}

.welcome-card p {
  color: #A16207;
  font-size: 14px;
}

.quick-links {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.quick-card {
  flex: 1;
  min-width: 100px;
  padding: 18px 12px;
  text-align: center;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  text-decoration: none;
  font-weight: 900;
  font-size: 16px;
  background: #FFFDF5;
  color: var(--doodle-text);
  transition: all 0.15s;
}

.quick-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.section-mark {
  font-size: 20px;
}

.section-title h3 {
  font-size: 18px;
  font-weight: 900;
  color: var(--doodle-text);
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.info-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  text-decoration: none;
  color: inherit;
  background: #FFFDF5;
  transition: all 0.15s;
}

.info-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.card-emoji {
  font-size: 32px;
}

.card-body h4 {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 2px;
}

.card-meta {
  font-size: 13px;
  color: #A16207;
}

.tip-card {
  padding: 16px;
  border: 2.5px dashed var(--doodle-yellow);
  border-radius: var(--doodle-radius);
  background: #FFFBEB;
}

.tip-card p {
  font-size: 13px;
  margin-bottom: 6px;
  color: #92400E;
}

.tip-card p:last-child {
  margin-bottom: 0;
}
</style>
