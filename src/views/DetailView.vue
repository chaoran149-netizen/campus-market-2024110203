<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
</script>

<template>
  <div class="detail-view">
    <button class="back-btn" @click="router.back()">← 返回</button>
    <h2>物品详情 #{{ route.params.id }}</h2>
    <div class="detail-card">
      <p class="detail-type">二手交易 · 主校区</p>
      <p class="detail-price">￥{{ Number(route.params.id) * 10 }}</p>
      <p class="detail-desc">这是物品的详细描述信息。在后续开发中将展示完整的内容、图片、发布人信息等。</p>
      <div class="detail-tags">
        <span class="tag">九成新</span>
        <span class="tag">可议价</span>
      </div>
      <div class="detail-actions">
        <button class="btn">收藏</button>
        <button class="btn">联系发布者</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-view { padding: 16px; }
.back-btn { background: none; border: 1px solid #ccc; padding: 6px 12px; border-radius: 4px; cursor: pointer; margin-bottom: 16px; }
.detail-card { border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; }
.detail-type { color: #666; font-size: 14px; }
.detail-price { font-size: 24px; font-weight: bold; color: #e74c3c; }
.detail-desc { margin: 12px 0; line-height: 1.6; }
.detail-tags { display: flex; gap: 8px; margin-bottom: 16px; }
.tag { background: #f0f0f0; padding: 4px 10px; border-radius: 12px; font-size: 12px; }
.detail-actions { display: flex; gap: 12px; }
.btn { padding: 8px 20px; border: 1px solid #409eff; background: #409eff; color: #fff; border-radius: 4px; cursor: pointer; }
</style>
