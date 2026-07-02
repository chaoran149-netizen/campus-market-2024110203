<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createUser, getUsers } from '@/api/user'

const router = useRouter()

const username = ref('')
const password = ref('')
const nickname = ref('')
const college = ref('计算机学院')
const campus = ref('主校区')
const errorMsg = ref('')
const successMsg = ref('')
const loading = ref(false)

async function handleRegister() {
  errorMsg.value = ''
  successMsg.value = ''
  if (!username.value.trim() || !password.value.trim() || !nickname.value.trim()) {
    errorMsg.value = '请填写用户名、密码和昵称'
    return
  }
  loading.value = true
  try {
    // 检查用户名是否已存在
    const check = await getUsers({ username: username.value.trim() })
    if (check.data.length > 0) {
      errorMsg.value = '用户名已被注册'
      return
    }
    await createUser({
      username: username.value.trim(),
      password: password.value,
      nickname: nickname.value.trim(),
      college: college.value,
      campus: campus.value,
    })
    successMsg.value = '注册成功！即将跳转到登录页…'
    setTimeout(() => router.push('/login'), 1000)
  } catch {
    errorMsg.value = '注册失败，请检查 Mock 服务是否启动'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="auth-view">
    <div class="auth-card">
      <h2>注册</h2>
      <p class="auth-sub">加入校园轻集市</p>

      <form class="auth-form" @submit.prevent="handleRegister">
        <div class="form-group">
          <label class="form-label">用户名</label>
          <input v-model="username" type="text" class="form-input" placeholder="登录时使用" />
        </div>
        <div class="form-group">
          <label class="form-label">密码</label>
          <input v-model="password" type="password" class="form-input" placeholder="6位以上" />
        </div>
        <div class="form-group">
          <label class="form-label">昵称</label>
          <input v-model="nickname" type="text" class="form-input" placeholder="在集市中显示的名称" />
        </div>
        <div class="form-row">
          <div class="form-group half">
            <label class="form-label">学院</label>
            <select v-model="college" class="form-input">
              <option>计算机学院</option>
              <option>经济学院</option>
              <option>文学院</option>
              <option>理学院</option>
            </select>
          </div>
          <div class="form-group half">
            <label class="form-label">校区</label>
            <select v-model="campus" class="form-input">
              <option>主校区</option>
              <option>东校区</option>
              <option>西校区</option>
            </select>
          </div>
        </div>

        <p v-if="successMsg" class="success-msg">{{ successMsg }}</p>
        <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>

        <button type="submit" class="submit-btn" :disabled="loading">
          {{ loading ? '注册中…' : '注册' }}
        </button>
      </form>

      <p class="switch-link">
        已有账号？<router-link to="/login">立即登录</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.auth-view {
  display: flex; justify-content: center; padding-top: 40px;
}
.auth-card {
  width: 100%; max-width: 400px; display: flex; flex-direction: column; gap: 20px;
  padding: 32px 28px; border: 1px solid var(--color-border); border-radius: var(--radius-xl);
  background: var(--color-surface);
}
.auth-card h2 { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; text-align: center; }
.auth-sub { text-align: center; font-size: 14px; color: var(--color-text-secondary); }
.auth-form { display: flex; flex-direction: column; gap: 16px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.half { flex: 1; }
.form-label { font-size: 13px; font-weight: 600; color: var(--color-text); }
.form-input {
  padding: 10px 14px; border: 1px solid var(--color-border); border-radius: var(--radius-md);
  font-size: 14px; font-family: inherit; background: var(--color-surface); color: var(--color-text);
  outline: none; transition: border-color var(--transition-fast); width: 100%;
}
.form-input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.form-input::placeholder { color: var(--color-text-muted); }
.form-row { display: flex; gap: 12px; }
.success-msg { font-size: 13px; color: #059669; text-align: center; }
.error-msg { font-size: 13px; color: #DC2626; text-align: center; }
.submit-btn {
  padding: 12px 24px; border: none; border-radius: var(--radius-md); background: var(--color-primary);
  color: #fff; font-size: 15px; font-weight: 600; font-family: inherit;
  cursor: pointer; transition: all var(--transition);
}
.submit-btn:hover:not(:disabled) { background: var(--color-primary-hover); }
.submit-btn:disabled { opacity: 0.6; cursor: not-allowed; }
.switch-link { text-align: center; font-size: 14px; color: var(--color-text-secondary); }
.switch-link a { color: var(--color-primary); text-decoration: none; font-weight: 600; }
</style>
