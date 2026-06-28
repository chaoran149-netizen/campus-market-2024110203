<script setup lang="ts">
const stats = {
  total: 128,
  byType: [
    { type: '二手交易', count: 52 },
    { type: '失物招领', count: 28 },
    { type: '拼单搭子', count: 31 },
    { type: '跑腿委托', count: 17 },
  ],
  byCampus: [
    { campus: '主校区', count: 68 },
    { campus: '东校区', count: 35 },
    { campus: '西校区', count: 25 },
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
    <h2>趋势看板</h2>
    <div class="stats-grid">
      <div class="stat-card total">
        <span class="stat-num">{{ stats.total }}</span>
        <span class="stat-label">信息总数</span>
      </div>
    </div>
    <div class="chart-section">
      <h3>信息类型占比</h3>
      <div class="bar-chart">
        <div v-for="item in stats.byType" :key="item.type" class="bar-row">
          <span class="bar-label">{{ item.type }}</span>
          <div class="bar-track">
            <div class="bar-fill" :style="{ width: (item.count / stats.total * 100) + '%' }"></div>
          </div>
          <span class="bar-count">{{ item.count }}</span>
        </div>
      </div>
    </div>
    <div class="chart-section">
      <h3>校区分布</h3>
      <div class="bar-chart">
        <div v-for="item in stats.byCampus" :key="item.campus" class="bar-row">
          <span class="bar-label">{{ item.campus }}</span>
          <div class="bar-track">
            <div class="bar-fill campus" :style="{ width: (item.count / stats.total * 100) + '%' }"></div>
          </div>
          <span class="bar-count">{{ item.count }}</span>
        </div>
      </div>
    </div>
    <div class="chart-section">
      <h3>状态统计</h3>
      <div v-for="item in stats.byStatus" :key="item.status" class="status-row">
        <span>{{ item.status }}</span>
        <span class="status-count">{{ item.count }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.board-view { padding: 16px; max-width: 600px; }
.stats-grid { margin-bottom: 24px; }
.stat-card.total { display: flex; flex-direction: column; align-items: center; padding: 24px; background: linear-gradient(135deg, #667eea, #764ba2); color: #fff; border-radius: 12px; }
.stat-num { font-size: 48px; font-weight: bold; }
.stat-label { font-size: 14px; opacity: 0.9; }
.chart-section { margin-bottom: 24px; }
.chart-section h3 { margin-bottom: 12px; }
.bar-chart { display: flex; flex-direction: column; gap: 8px; }
.bar-row { display: flex; align-items: center; gap: 8px; }
.bar-label { width: 80px; font-size: 13px; }
.bar-track { flex: 1; height: 20px; background: #f0f0f0; border-radius: 10px; overflow: hidden; }
.bar-fill { height: 100%; background: #409eff; border-radius: 10px; transition: width 0.3s; }
.bar-fill.campus { background: #67c23a; }
.bar-count { width: 30px; text-align: right; font-size: 13px; }
.status-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #f0f0f0; }
.status-count { font-weight: bold; }
</style>
