<script setup lang="ts">
import { ref } from 'vue'

const type = ref('secondhand')
</script>

<template>
  <div class="publish-view">
    <h2>发布信息</h2>
    <form class="publish-form" @submit.prevent>
      <div class="form-group">
        <label>信息类型</label>
        <select v-model="type" class="form-input">
          <option value="secondhand">二手交易</option>
          <option value="lostfound">失物招领</option>
          <option value="groupbuy">拼单搭子</option>
          <option value="errand">跑腿委托</option>
        </select>
      </div>
      <div class="form-group">
        <label>标题</label>
        <input type="text" class="form-input" placeholder="请输入标题" />
      </div>
      <div class="form-group">
        <label>校区</label>
        <select class="form-input"><option>主校区</option><option>东校区</option><option>西校区</option></select>
      </div>
      <div class="form-group">
        <label>详细描述</label>
        <textarea class="form-input textarea" placeholder="请输入详细描述"></textarea>
      </div>
      <div v-if="type === 'secondhand'" class="form-group">
        <label>价格（元）</label>
        <input type="number" class="form-input" placeholder="0" />
      </div>
      <div v-if="type === 'groupbuy'" class="form-group">
        <label>目标人数</label>
        <input type="number" class="form-input" placeholder="2" />
      </div>
      <div v-if="type === 'errand'" class="form-group">
        <label>酬劳（元）</label>
        <input type="number" class="form-input" placeholder="0" />
      </div>
      <button type="submit" class="submit-btn">发布</button>
    </form>
  </div>
</template>

<style scoped>
.publish-view { padding: 16px; max-width: 600px; }
.publish-form { display: flex; flex-direction: column; gap: 16px; }
.form-group { display: flex; flex-direction: column; gap: 4px; }
.form-group label { font-weight: bold; font-size: 14px; }
.form-input { padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.textarea { min-height: 100px; resize: vertical; }
.submit-btn { padding: 10px; background: #409eff; color: #fff; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
.submit-btn:hover { background: #66b1ff; }
</style>
