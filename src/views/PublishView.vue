<script setup lang="ts">
import { ref } from 'vue'

const type = ref('secondhand')
</script>

<template>
  <div class="publish-view">
    <div class="pub-header">
      <h2>发布新帖</h2>
      <p>选个类型，填个内容，搞定！</p>
    </div>

    <form class="publish-form" @submit.prevent>
      <div class="form-group">
        <label><span class="label-icon">📌</span> 信息类型</label>
        <select v-model="type" class="form-input">
          <option value="secondhand">♻️ 二手交易</option>
          <option value="lostfound">🔍 失物招领</option>
          <option value="groupbuy">👥 拼单搭子</option>
          <option value="errand">🏃 跑腿委托</option>
        </select>
      </div>

      <div class="form-group">
        <label><span class="label-icon">📝</span> 标题</label>
        <input type="text" class="form-input" placeholder="起个吸引人的标题吧" />
      </div>

      <div class="form-row">
        <div class="form-group flex-1">
          <label><span class="label-icon">📍</span> 校区</label>
          <select class="form-input">
            <option>主校区</option><option>东校区</option><option>西校区</option>
          </select>
        </div>
        <div class="form-group flex-1">
          <label><span class="label-icon">🏷️</span> 标签</label>
          <input type="text" class="form-input" placeholder="如：九成新、自取" />
        </div>
      </div>

      <div class="form-group">
        <label><span class="label-icon">📄</span> 详细描述</label>
        <textarea class="form-input textarea" placeholder="多说两句，别人更懂你~"></textarea>
      </div>

      <div v-if="type === 'secondhand'" class="form-row">
        <div class="form-group flex-1">
          <label><span class="label-icon">💰</span> 价格（元）</label>
          <input type="number" class="form-input" placeholder="0" />
        </div>
        <div class="form-group flex-1">
          <label><span class="label-icon">⭐</span> 成色</label>
          <select class="form-input">
            <option>全新</option><option>九成新</option><option>七成新</option><option>有瑕疵</option>
          </select>
        </div>
      </div>

      <div v-if="type === 'lostfound'" class="form-row">
        <div class="form-group flex-1">
          <label><span class="label-icon">📌</span> 类型</label>
          <select class="form-input">
            <option>丢失</option><option>捡到</option>
          </select>
        </div>
        <div class="form-group flex-1">
          <label><span class="label-icon">🕐</span> 发生时间</label>
          <input type="date" class="form-input" />
        </div>
      </div>

      <div v-if="type === 'groupbuy'" class="form-row">
        <div class="form-group flex-1">
          <label><span class="label-icon">👥</span> 目标人数</label>
          <input type="number" class="form-input" placeholder="4" />
        </div>
        <div class="form-group flex-1">
          <label><span class="label-icon">⏰</span> 截止时间</label>
          <input type="datetime-local" class="form-input" />
        </div>
      </div>

      <div v-if="type === 'errand'" class="form-row">
        <div class="form-group flex-1">
          <label><span class="label-icon">💰</span> 酬劳（元）</label>
          <input type="number" class="form-input" placeholder="0" />
        </div>
        <div class="form-group flex-1">
          <label><span class="label-icon">📍</span> 任务地点</label>
          <input type="text" class="form-input" placeholder="如：菜鸟驿站" />
        </div>
      </div>

      <button type="submit" class="submit-btn">✏️ 发布！</button>
    </form>
  </div>
</template>

<style scoped>
.publish-view {
  max-width: 600px;
}

.pub-header {
  margin-bottom: 24px;
}

.pub-header h2 {
  font-size: 22px;
  font-weight: 900;
  margin-bottom: 4px;
}

.pub-header p {
  font-size: 14px;
  color: #A16207;
}

.publish-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-group label {
  font-weight: 700;
  font-size: 14px;
}

.label-icon {
  font-size: 14px;
}

.form-row {
  display: flex;
  gap: 12px;
}

.flex-1 {
  flex: 1;
}

.form-input {
  padding: 10px 14px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  font-family: inherit;
  font-size: 14px;
  background: #FFFDF5;
  transition: all 0.15s;
}

.form-input:focus {
  outline: none;
  box-shadow: 3px 3px 0px var(--doodle-border);
}

.textarea {
  min-height: 100px;
  resize: vertical;
}

.submit-btn {
  padding: 14px;
  background: var(--doodle-yellow);
  color: #fff;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  cursor: pointer;
  font-size: 18px;
  font-weight: 900;
  font-family: inherit;
  transition: all 0.15s;
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.submit-btn:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px var(--doodle-border);
}

.submit-btn:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0px var(--doodle-border);
}
</style>
