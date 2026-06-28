<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const router = useRouter()
const isFavorited = ref(false)

const items: Record<number, { title: string; type: string; campus: string; price: number; emoji: string; desc: string; tags: string[] }> = {
  1: { title: '二手教材 - 高等数学', type: '二手交易', campus: '主校区', price: 25, emoji: '📚', desc: '大二高数教材，几乎全新，只有前两章有笔记。需要自取，主校区3号楼。', tags: ['九成新', '可议价', '自取'] },
  2: { title: '蓝牙耳机 九成新', type: '二手交易', campus: '东校区', price: 80, emoji: '🎧', desc: '用了两个月，充电仓完好，音质很好。附赠一条充电线。', tags: ['九成新', '带配件'] },
  3: { title: '丢失校园卡 - 李**', type: '失物招领', campus: '主校区', price: 0, emoji: '🪪', desc: '在主校区食堂捡到校园卡一张，失主请联系认领。', tags: ['已捡到', '食堂'] },
  4: { title: '奶茶拼单！一点点', type: '拼单搭子', campus: '西校区', price: 0, emoji: '🧋', desc: '满20起送，还差2杯！要喝的dd我～', tags: ['进行中', '差2人'] },
}

const item = items[Number(route.params.id)] || items[1]
</script>

<template>
  <div class="detail-view">
    <button class="back-btn" @click="router.back()">← 回去</button>

    <div class="detail-card">
      <div class="detail-emoji">{{ item.emoji }}</div>
      <h2 class="detail-title">{{ item.title }}</h2>

      <div class="detail-tags">
        <span class="tag tag-type">{{ item.type }}</span>
        <span class="tag tag-campus">{{ item.campus }}</span>
        <span v-if="item.price" class="tag tag-price">￥{{ item.price }}</span>
      </div>

      <div class="detail-meta">
        <span>👤 校园用户</span>
        <span>🕐 2026-06-27</span>
        <span>👁️ {{ Number(route.params.id) * 23 }} 次浏览</span>
      </div>

      <p class="detail-desc">{{ item.desc }}</p>

      <div class="detail-tags-list">
        <span v-for="t in item.tags" :key="t" class="tag-simple">{{ t }}</span>
      </div>

      <div class="detail-actions">
        <button class="action-btn favorite" :class="{ liked: isFavorited }" @click="isFavorited = !isFavorited">
          {{ isFavorited ? '❤️ 已收藏' : '🤍 收藏' }}
        </button>
        <button class="action-btn contact">💬 联系发布者</button>
        <button v-if="item.type === '二手交易'" class="action-btn bargain">💰 砍个价</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-view {
  max-width: 600px;
}

.back-btn {
  background: #FFFDF5;
  border: 2.5px solid var(--doodle-border);
  padding: 8px 18px;
  border-radius: var(--doodle-radius);
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  color: var(--doodle-text);
  margin-bottom: 16px;
  transition: all 0.15s;
}

.back-btn:hover {
  transform: translate(-2px, -2px);
  box-shadow: 3px 3px 0px var(--doodle-border);
}

.detail-card {
  border: 3px solid var(--doodle-border);
  border-radius: 24px;
  padding: 28px 24px;
  background: #FFFDF5;
  box-shadow: 6px 6px 0px var(--doodle-border);
}

.detail-emoji {
  font-size: 56px;
  text-align: center;
  margin-bottom: 12px;
}

.detail-title {
  font-size: 22px;
  font-weight: 900;
  text-align: center;
  margin-bottom: 12px;
  color: var(--doodle-text);
}

.detail-tags {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 16px;
}

.tag {
  font-size: 12px;
  padding: 4px 14px;
  border-radius: 14px;
  font-weight: 700;
}

.tag-type { background: #FEF3C7; color: #A16207; border: 1.5px solid #D97706; }
.tag-campus { background: #E0F2FE; color: #0369A1; border: 1.5px solid #38BDF8; }
.tag-price { background: #FEE2E2; color: #DC2626; border: 1.5px solid #EF4444; font-size: 14px; }

.detail-meta {
  display: flex;
  justify-content: center;
  gap: 16px;
  font-size: 13px;
  color: #A16207;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.detail-desc {
  font-size: 15px;
  line-height: 1.8;
  color: #5C4A2E;
  padding: 16px;
  background: #FFFBEB;
  border-radius: var(--doodle-radius);
  margin-bottom: 16px;
}

.detail-tags-list {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.tag-simple {
  font-size: 12px;
  padding: 4px 12px;
  border: 2px dashed var(--doodle-yellow);
  border-radius: 14px;
  color: #92400E;
  background: #FFFBEB;
}

.detail-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.action-btn {
  flex: 1;
  min-width: 120px;
  padding: 10px 16px;
  border: 2.5px solid var(--doodle-border);
  border-radius: var(--doodle-radius);
  background: #FFFDF5;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
  color: var(--doodle-text);
}

.action-btn:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0px var(--doodle-border);
}

.action-btn.favorite.liked {
  background: #FEE2E2;
  border-color: #EF4444;
  color: #DC2626;
}

.action-btn.contact {
  background: var(--doodle-cream);
}

.action-btn.bargain {
  background: #FFFBEB;
  border-color: var(--doodle-yellow);
}
</style>
