<script setup lang="ts"></script>

<template>
  <div class="errand-view">
    <div class="page-header">
      <h2>🏃 跑腿委托</h2>
      <p>找人帮忙，轻松搞定杂事</p>
    </div>

    <div class="errand-list">
      <div v-for="i in 5" :key="i" class="errand-card">
        <div class="errand-type">
          <span class="type-icon">{{ ['📦', '🛒', '📄', '🍱', '🔧'][i - 1] }}</span>
          <span class="type-text">{{ ['代取快递', '超市代购', '文件打印', '代拿外卖', '小件维修'][i - 1] }}</span>
        </div>
        <div class="errand-body">
          <p class="errand-desc">{{ ['菜鸟驿站取三个包裹', '买一瓶洗发水和牙膏', '打印 20 页复习资料', '二食堂一楼麻辣烫', '换一个自行车内胎'][i - 1] }}</p>
        </div>
        <div class="errand-footer">
          <span class="reward">💰 报酬：￥{{ i * 5 + 5 }}</span>
          <span class="deadline">⏰ 截止：今天 {{ 14 + i }}:00</span>
          <span class="status">{{ i <= 3 ? '🟡 待接单' : '🟢 已接单' }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.errand-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.page-header {
  text-align: center;
  padding: 28px 24px 20px;
  background: #FFFDF5;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  box-shadow: 6px 6px 0px var(--doodle-border);
}

.page-header h2 {
  font-size: 22px;
  font-weight: 900;
  color: var(--doodle-red);
  margin-bottom: 6px;
}

.page-header p {
  color: #A16207;
  font-size: 14px;
}

.errand-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.errand-card {
  padding: 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  transition: all 0.15s;
}

.errand-card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.errand-type {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.type-icon {
  font-size: 24px;
}

.type-text {
  font-size: 14px;
  font-weight: 900;
  color: var(--doodle-yellow);
  padding: 2px 10px;
  border: 2px solid var(--doodle-yellow);
  border-radius: 20px;
}

.errand-body {
  margin-bottom: 10px;
}

.errand-desc {
  font-size: 14px;
  color: var(--doodle-text);
}

.errand-footer {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font-size: 13px;
}

.reward {
  font-weight: 900;
  color: var(--doodle-red);
}

.deadline {
  color: #A16207;
}

.status {
  font-weight: 700;
}
</style>
