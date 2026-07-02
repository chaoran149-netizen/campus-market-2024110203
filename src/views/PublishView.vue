<script setup lang="ts">
import { ref, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { createTrade } from '@/api/trade'
import { createLostFound } from '@/api/lostFound'
import { createGroupBuy } from '@/api/groupBuy'
import { createErrand } from '@/api/errand'
import FormField from '@/components/FormField.vue'

const router = useRouter()
const userStore = useUserStore()

const publishType = ref<'trade' | 'lostFound' | 'groupBuy' | 'errand'>('trade')
const submitting = ref(false)
const successMsg = ref('')
const errorMsg = ref('')

const form = reactive({ title: '', description: '', campus: '主校区' })

const tradeFields = reactive({ price: null as number | null, category: '教材书籍', condition: '九成新', location: '' })
const lostFoundFields = reactive({ type: 'lost' as 'lost' | 'found', itemName: '', location: '', time: '', contact: '' })
const groupBuyFields = reactive({ type: '外卖拼单', targetCount: null as number | null, deadline: '', location: '' })
const errandFields = reactive({ taskType: '取快递', reward: null as number | null, pickupLocation: '', deliveryLocation: '', deadline: '' })

const errors = reactive<Record<string, string>>({})

function validate(): boolean {
  const e: Record<string, string> = {}
  if (!form.title.trim()) e.title = '请输入标题'
  if (!form.description.trim()) e.description = '请输入描述'
  if (publishType.value === 'trade') {
    if (tradeFields.price === null || tradeFields.price <= 0) e.price = '请输入有效的价格'
    if (!tradeFields.location.trim()) e.location = '请输入交易地点'
  }
  if (publishType.value === 'lostFound') {
    if (!lostFoundFields.itemName.trim()) e.itemName = '请输入物品名称'
    if (!lostFoundFields.location.trim()) e.location = '请输入丢失/拾取地点'
    if (!lostFoundFields.time.trim()) e.time = '请输入时间'
  }
  if (publishType.value === 'groupBuy') {
    if (groupBuyFields.targetCount === null || groupBuyFields.targetCount <= 1) e.targetCount = '目标人数至少为2'
    if (!groupBuyFields.deadline.trim()) e.deadline = '请输入截止时间'
  }
  if (publishType.value === 'errand') {
    if (errandFields.reward === null || errandFields.reward <= 0) e.reward = '请输入有效的酬劳'
    if (!errandFields.pickupLocation.trim()) e.pickupLocation = '请输入取件地点'
    if (!errandFields.deadline.trim()) e.deadline = '请输入截止时间'
  }
  Object.assign(errors, e)
  return Object.keys(e).length === 0
}

function clearErrors() { Object.keys(errors).forEach(k => delete errors[k]) }

function resetForm() {
  form.title = ''; form.description = ''; form.campus = '主校区'
  tradeFields.price = null; tradeFields.category = '教材书籍'; tradeFields.condition = '九成新'; tradeFields.location = ''
  lostFoundFields.type = 'lost'; lostFoundFields.itemName = ''; lostFoundFields.location = ''; lostFoundFields.time = ''; lostFoundFields.contact = ''
  groupBuyFields.type = '外卖拼单'; groupBuyFields.targetCount = null; groupBuyFields.deadline = ''; groupBuyFields.location = ''
  errandFields.taskType = '取快递'; errandFields.reward = null; errandFields.pickupLocation = ''; errandFields.deliveryLocation = ''; errandFields.deadline = ''
  clearErrors()
}

const now = () => new Date().toLocaleString('zh-CN', { hour12: false }).replace(/\//g, '-')

async function handleSubmit() {
  clearErrors()
  errorMsg.value = ''
  successMsg.value = ''

  if (!userStore.isLoggedIn) {
    errorMsg.value = '请先登录后再发布'
    return
  }
  if (!validate()) return

  const publisher = userStore.displayName
  submitting.value = true
  try {
    const publisher = userStore.displayName
    if (publishType.value === 'trade') {
      await createTrade({
        title: form.title, price: tradeFields.price!, category: tradeFields.category,
        condition: tradeFields.condition, location: tradeFields.location, campus: form.campus,
        description: form.description, publisher, publishTime: now(), status: 'open',
      })
    } else if (publishType.value === 'lostFound') {
      await createLostFound({
        title: form.title, type: lostFoundFields.type, itemName: lostFoundFields.itemName,
        location: lostFoundFields.location, time: lostFoundFields.time, description: form.description,
        contact: lostFoundFields.contact || publisher, status: 'open', campus: form.campus,
      })
    } else if (publishType.value === 'groupBuy') {
      await createGroupBuy({
        title: form.title, type: groupBuyFields.type, targetCount: groupBuyFields.targetCount!,
        currentCount: 1, deadline: groupBuyFields.deadline, location: groupBuyFields.location || form.campus,
        description: form.description, campus: form.campus, publisher, status: 'open',
      })
    } else if (publishType.value === 'errand') {
      await createErrand({
        title: form.title, taskType: errandFields.taskType, reward: errandFields.reward!,
        pickupLocation: errandFields.pickupLocation, deliveryLocation: errandFields.deliveryLocation || form.campus,
        deadline: errandFields.deadline, description: form.description, campus: form.campus, publisher, status: 'open',
      })
    }
    successMsg.value = '发布成功！正在跳转…'
    setTimeout(() => {
      const routeMap: Record<string, string> = { trade: '/trade', lostFound: '/lost-found', groupBuy: '/group-buy', errand: '/errand' }
      router.push(routeMap[publishType.value])
    }, 800)
  } catch {
    errorMsg.value = '发布失败，请检查 Mock 服务是否已启动'
  } finally { submitting.value = false }
}

watch(publishType, () => { clearErrors(); errorMsg.value = ''; successMsg.value = '' })
</script>

<template>
  <div class="publish-view">
    <div class="page-top"><h2>发布信息</h2><p>选择类型，填写内容，一键发布到校园集市</p></div>
    <form class="publish-form" @submit.prevent="handleSubmit">
      <div class="type-grid">
        <label v-for="t in typeOptions" :key="t.value" class="type-option" :class="{ selected: publishType === t.value }">
          <input type="radio" v-model="publishType" :value="t.value" />
          <span class="type-icon">{{ t.icon }}</span>
          <span class="type-label">{{ t.label }}</span>
        </label>
      </div>
      <FormField label="标题" :required="true" :error="errors.title">
        <input v-model="form.title" type="text" class="form-input" placeholder="起个吸引人的标题" />
      </FormField>
      <template v-if="publishType === 'trade'">
        <div class="form-row">
          <FormField label="价格 ¥" :required="true" :error="errors.price" class="half"><input v-model.number="tradeFields.price" type="number" class="form-input" placeholder="0" min="0" /></FormField>
          <FormField label="成色" class="half"><select v-model="tradeFields.condition" class="form-input"><option>全新</option><option>九成新</option><option>七八成新</option><option>五成新以下</option></select></FormField>
        </div>
        <div class="form-row">
          <FormField label="分类" class="half"><select v-model="tradeFields.category" class="form-input"><option>教材书籍</option><option>数码电子</option><option>生活用品</option><option>运动装备</option></select></FormField>
          <FormField label="交易地点" :required="true" :error="errors.location" class="half"><input v-model="tradeFields.location" type="text" class="form-input" placeholder="如图书馆一楼" /></FormField>
        </div>
      </template>
      <template v-if="publishType === 'lostFound'">
        <div class="form-row">
          <FormField label="类型" class="half"><select v-model="lostFoundFields.type" class="form-input"><option value="lost">遗失求助</option><option value="found">拾取启事</option></select></FormField>
          <FormField label="物品名称" :required="true" :error="errors.itemName" class="half"><input v-model="lostFoundFields.itemName" type="text" class="form-input" placeholder="如校园卡" /></FormField>
        </div>
        <div class="form-row">
          <FormField label="丢失/拾取地点" :required="true" :error="errors.location" class="half"><input v-model="lostFoundFields.location" type="text" class="form-input" placeholder="如二食堂" /></FormField>
          <FormField label="时间" :required="true" :error="errors.time" class="half"><input v-model="lostFoundFields.time" type="text" class="form-input" placeholder="如今天下午3点" /></FormField>
        </div>
        <FormField label="联系方式"><input v-model="lostFoundFields.contact" type="text" class="form-input" placeholder="手机号或微信号" /></FormField>
      </template>
      <template v-if="publishType === 'groupBuy'">
        <div class="form-row">
          <FormField label="拼单类型" class="half"><select v-model="groupBuyFields.type" class="form-input"><option>外卖拼单</option><option>奶茶拼单</option><option>学习搭子</option><option>运动搭子</option><option>游戏组队</option><option>休闲搭子</option></select></FormField>
          <FormField label="目标人数" :required="true" :error="errors.targetCount" class="half"><input v-model.number="groupBuyFields.targetCount" type="number" class="form-input" placeholder="2" min="2" /></FormField>
        </div>
        <div class="form-row">
          <FormField label="截止时间" :required="true" :error="errors.deadline" class="half"><input v-model="groupBuyFields.deadline" type="text" class="form-input" placeholder="如 今天18:00" /></FormField>
          <FormField label="集合地点" class="half"><input v-model="groupBuyFields.location" type="text" class="form-input" placeholder="如三号楼" /></FormField>
        </div>
      </template>
      <template v-if="publishType === 'errand'">
        <div class="form-row">
          <FormField label="任务类型" class="half"><select v-model="errandFields.taskType" class="form-input"><option>取快递</option><option>代购</option><option>打印</option><option>取餐</option><option>维修</option><option>搬运</option><option>代办</option></select></FormField>
          <FormField label="酬劳 ¥" :required="true" :error="errors.reward" class="half"><input v-model.number="errandFields.reward" type="number" class="form-input" placeholder="5" min="1" /></FormField>
        </div>
        <div class="form-row">
          <FormField label="取件地点" :required="true" :error="errors.pickupLocation" class="half"><input v-model="errandFields.pickupLocation" type="text" class="form-input" placeholder="如菜鸟驿站" /></FormField>
          <FormField label="送达地点" class="half"><input v-model="errandFields.deliveryLocation" type="text" class="form-input" placeholder="如三号楼" /></FormField>
        </div>
        <FormField label="截止时间" :required="true" :error="errors.deadline"><input v-model="errandFields.deadline" type="text" class="form-input" placeholder="如 今天18:00" /></FormField>
      </template>
      <FormField label="校区"><select v-model="form.campus" class="form-input"><option>主校区</option><option>东校区</option><option>西校区</option></select></FormField>
      <FormField label="详细描述" :required="true" :error="errors.description">
        <textarea v-model="form.description" class="form-input" rows="4" placeholder="描述一下详细信息…"></textarea>
      </FormField>
      <p class="publisher-hint">📌 发布人：{{ userStore.displayName }}</p>
      <p v-if="successMsg" class="feedback-msg success">{{ successMsg }}</p>
      <p v-if="errorMsg" class="feedback-msg error">{{ errorMsg }}</p>
      <div class="btn-row">
        <button type="button" class="reset-btn" @click="resetForm">重置</button>
        <button type="submit" class="submit-btn" :disabled="submitting">{{ submitting ? '发布中…' : '发布到集市' }}</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
const typeOptions = [
  { value: 'trade', label: '二手交易', icon: '♻️' },
  { value: 'lostFound', label: '失物招领', icon: '🔍' },
  { value: 'groupBuy', label: '拼单搭子', icon: '👥' },
  { value: 'errand', label: '跑腿委托', icon: '🏃' },
]
</script>

<style scoped>
.publish-view { display: flex; flex-direction: column; gap: 24px; max-width: 600px; }
.page-top { margin-bottom: 4px; }
.page-top h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 4px; }
.page-top p { font-size: 14px; color: var(--color-text-secondary); }
.type-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }
.type-option { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 16px 12px; border: 1px solid var(--color-border); border-radius: var(--radius-lg); cursor: pointer; transition: all var(--transition-fast); position: relative; }
.type-option input { position: absolute; opacity: 0; }
.type-option:hover { border-color: var(--color-primary-soft); }
.type-option.selected { border-color: var(--color-primary); background: var(--color-primary-light); }
.type-icon { font-size: 24px; }
.type-label { font-size: 14px; font-weight: 600; color: var(--color-text); }
.publish-form { display: flex; flex-direction: column; gap: 18px; }
.form-input { padding: 10px 14px; border: 1px solid var(--color-border); border-radius: var(--radius-md); font-size: 14px; font-family: inherit; color: var(--color-text); background: var(--color-surface); transition: border-color var(--transition-fast); outline: none; width: 100%; }
.form-input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.form-input::placeholder { color: var(--color-text-muted); }
textarea.form-input { resize: vertical; min-height: 80px; }
.form-row { display: flex; gap: 12px; }
.half { flex: 1; }
.publisher-hint { font-size: 13px; color: var(--color-text-muted); padding: 8px 12px; background: var(--color-primary-light); border-radius: var(--radius-md); }
.feedback-msg { font-size: 14px; font-weight: 600; text-align: center; padding: 8px; border-radius: var(--radius-md); }
.feedback-msg.success { background: #D1FAE5; color: #059669; }
.feedback-msg.error { background: #FEE2E2; color: #DC2626; }
.btn-row { display: flex; gap: 12px; }
.reset-btn { flex: 1; padding: 14px 24px; border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); font-size: 15px; font-weight: 600; font-family: inherit; cursor: pointer; transition: all var(--transition); }
.reset-btn:hover { background: var(--color-surface-hover); }
.submit-btn { flex: 2; padding: 14px 24px; border: none; border-radius: var(--radius-md); background: var(--color-primary); color: #fff; font-size: 15px; font-weight: 600; font-family: inherit; cursor: pointer; transition: all var(--transition); }
.submit-btn:hover:not(:disabled) { background: var(--color-primary-hover); box-shadow: var(--shadow-md); }
.submit-btn:disabled { opacity: 0.6; cursor: not-allowed; }
@media (max-width: 640px) { .form-row { flex-direction: column; } .type-grid { grid-template-columns: repeat(2, 1fr); } }
</style>
