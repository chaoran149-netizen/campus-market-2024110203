<script setup lang="ts">
import { ref } from 'vue'

const type = ref('secondhand')
const types = [
  { value: 'secondhand', label: '二手交易', icon: '♻️' },
  { value: 'lostfound', label: '失物招领', icon: '🔍' },
  { value: 'groupbuy', label: '拼单搭子', icon: '👥' },
  { value: 'errand', label: '跑腿委托', icon: '🏃' },
]
</script>

<template>
  <div class="publish-view">
    <div class="page-top">
      <h2>发布信息</h2>
      <p>选择类型，填写内容，一键发布到校园集市</p>
    </div>

    <form class="publish-form" @submit.prevent>
      <!-- Type Selector -->
      <div class="type-grid">
        <label
          v-for="t in types"
          :key="t.value"
          class="type-option"
          :class="{ selected: type === t.value }"
        >
          <input type="radio" v-model="type" :value="t.value" />
          <span class="type-icon">{{ t.icon }}</span>
          <span class="type-label">{{ t.label }}</span>
        </label>
      </div>

      <div class="form-group">
        <label class="form-label">标题</label>
        <input type="text" class="form-input" placeholder="起个吸引人的标题吧" />
      </div>

      <div class="form-row">
        <div class="form-group half">
          <label class="form-label">价格 ¥</label>
          <input type="number" class="form-input" placeholder="0" />
        </div>
        <div class="form-group half">
          <label class="form-label">校区</label>
          <select class="form-input">
            <option>主校区</option>
            <option>东校区</option>
            <option>西校区</option>
          </select>
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">详细描述</label>
        <textarea class="form-input" rows="4" placeholder="描述一下物品状况、交易地点…"></textarea>
      </div>

      <button type="submit" class="submit-btn">发布到集市</button>
    </form>
  </div>
</template>

<style scoped>
.publish-view { display: flex; flex-direction: column; gap: 24px; max-width: 560px; }

.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }

/* ── Type Grid ── */
.type-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }

.type-option {
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  padding: 16px 12px; border: 1px solid var(--color-border); border-radius: var(--radius-lg);
  cursor: pointer; transition: all var(--transition-fast); position: relative;
}
.type-option input { position: absolute; opacity: 0; }
.type-option:hover { border-color: var(--color-primary-soft); }
.type-option.selected { border-color: var(--color-primary); background: var(--color-primary-light); }

.type-icon { font-size: 24px; }
.type-label { font-size: 14px; font-weight: 600; color: var(--color-text); }

/* ── Form ── */
.publish-form { display: flex; flex-direction: column; gap: 20px; }

.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-label { font-size: 13px; font-weight: 600; color: var(--color-text); }
.form-input {
  padding: 10px 14px; border: 1px solid var(--color-border); border-radius: var(--radius-md);
  font-size: 14px; font-family: inherit; color: var(--color-text); background: var(--color-surface);
  transition: border-color var(--transition-fast); outline: none;
}
.form-input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.form-input::placeholder { color: var(--color-text-muted); }

textarea.form-input { resize: vertical; min-height: 80px; }

.form-row { display: flex; gap: 12px; }
.form-group.half { flex: 1; }

.submit-btn {
  padding: 14px 24px; border: none; border-radius: var(--radius-md);
  background: var(--color-primary); color: #fff; font-size: 15px; font-weight: 600;
  font-family: inherit; cursor: pointer; transition: all var(--transition);
}
.submit-btn:hover { background: var(--color-primary-hover); box-shadow: var(--shadow-md); }

@media (max-width: 640px) {
  .type-grid { grid-template-columns: repeat(2, 1fr); }
  .form-row { flex-direction: column; }
}
</style>
