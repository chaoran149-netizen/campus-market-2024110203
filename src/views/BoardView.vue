<script setup lang="ts">
const stats = {
  total: 128,
  byType: [
    { type: '二手交易', count: 52, color: '#F59E0B' },
    { type: '失物招领', count: 28, color: '#38BDF8' },
    { type: '拼单搭子', count: 31, color: '#10B981' },
    { type: '跑腿委托', count: 17, color: '#EF4444' },
  ],
  byCampus: [
    { campus: '主校区', count: 68, color: '#8B5CF6' },
    { campus: '东校区', count: 35, color: '#EC4899' },
    { campus: '西校区', count: 25, color: '#14B8A6' },
  ],
  byStatus: [
    { status: '进行中', count: 82 },
    { status: '已完成', count: 36 },
    { status: '已关闭', count: 10 },
  ],
}
</script>

<template>
  <div class="board-view">
    <h2 class="page-title">📊 校园数据看板</h2>

    <div class="total-card">
      <span class="total-num">{{ stats.total }}</span>
      <span class="total-label">条校园信息</span>
    </div>

    <div class="chart-section">
      <div class="section-title">
        <span>📦</span>
        <h3>信息类型</h3>
      </div>
      <div class="bar-chart">
        <div v-for="item in stats.byType" :key="item.type" class="bar-row">
          <span class="bar-label">{{ item.type }}</span>
          <div class="bar-track">
            <div class="bar-fill" :style="{ width: (item.count / stats.total * 100) + '%', background: item.color }"></div>
          </div>
          <span class="bar-count">{{ item.count }}</span>
        </div>
      </div>
    </div>

    <div class="chart-section">
      <div class="section-title">
        <span>📍</span>
        <h3>校区分布</h3>
      </div>
      <div class="bar-chart">
        <div v-for="item in stats.byCampus" :key="item.campus" class="bar-row">
          <span class="bar-label">{{ item.campus }}</span>
          <div class="bar-track">
            <div class="bar-fill" :style="{ width: (item.count / stats.total * 100) + '%', background: item.color }"></div>
          </div>
          <span class="bar-count">{{ item.count }}</span>
        </div>
      </div>
    </div>

    <div class="chart-section">
      <div class="section-title">
        <span>🔄</span>
        <h3>状态统计</h3>
      </div>
      <div class="status-list">
        <div v-for="item in stats.byStatus" :key="item.status" class="status-item">
          <div class="status-left">
            <span class="status-dot" :class="item.status"></span>
            <span>{{ item.status }}</span>
          </div>
          <span class="status-right">{{ item.count }} 条</span>
        </div>
      </div>
    </div>

    <div class="chart-section">
      <div class="section-title">
        <span>🔥</span>
        <h3>热门排行</h3>
      </div>
      <div class="rank-list">
        <div class="rank-item rank-1">
          <span class="rank-num">🥇</span>
          <span>二手教材 - 高等数学</span>
          <span class="rank-count">152 浏览</span>
        </div>
        <div class="rank-item rank-2">
          <span class="rank-num">🥈</span>
          <span>奶茶拼单！一点点</span>
          <span class="rank-count">98 浏览</span>
        </div>
        <div class="rank-item rank-3">
          <span class="rank-num">🥉</span>
          <span>蓝牙耳机 九成新</span>
          <span class="rank-count">76 浏览</span>
        </div>
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

.total-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 28px 24px;
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  background: #FFFDF5;
  box-shadow: 6px 6px 0px var(--doodle-border);
  margin-bottom: 24px;
}

.total-num {
  font-size: 56px;
  font-weight: 900;
  color: var(--doodle-red);
  line-height: 1;
}

.total-label {
  font-size: 14px;
  color: #A16207;
  margin-top: 4px;
}

.chart-section {
  margin-bottom: 24px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.section-title h3 {
  font-size: 16px;
  font-weight: 900;
}

.bar-chart {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.bar-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.bar-label {
  width: 80px;
  font-size: 13px;
  font-weight: 700;
  flex-shrink: 0;
}

.bar-track {
  flex: 1;
  height: 22px;
  background: #FEF3C7;
  border-radius: 11px;
  overflow: hidden;
  border: 2px solid var(--doodle-border);
}

.bar-fill {
  height: 100%;
  border-radius: 9px;
  transition: width 0.3s;
}

.bar-count {
  width: 30px;
  text-align: right;
  font-size: 13px;
  font-weight: 700;
  color: #A16207;
}

.status-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
}

.status-left {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
}

.status-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.status-dot.进行中 { background: #10B981; }
.status-dot.已完成 { background: #F59E0B; }
.status-dot.已关闭 { background: #9CA3AF; }

.status-right {
  font-weight: 700;
  color: #A16207;
}

.rank-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rank-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
}

.rank-num {
  font-size: 20px;
  flex-shrink: 0;
}

.rank-item span:nth-child(2) {
  flex: 1;
  font-weight: 700;
  font-size: 14px;
}

.rank-count {
  font-size: 12px;
  color: #A16207;
  flex-shrink: 0;
}
</style>
