<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { getUsers } from '@/api/user'

const router = useRouter()
const userStore = useUserStore()

const username = ref('')
const password = ref('')
const errorMsg = ref('')
const loading = ref(false)

async function handleLogin() {
  errorMsg.value = ''
  if (!username.value.trim() || !password.value.trim()) {
    errorMsg.value = '请输入用户名和密码'
    return
  }
  loading.value = true
  try {
    const res = await getUsers({ username: username.value.trim() })
    const users = res.data
    const matched = users.find(
      (u: { username: string; password: string }) =>
        u.username === username.value.trim() && u.password === password.value
    )
    if (!matched) {
      errorMsg.value = '用户名或密码错误'
      return
    }
    userStore.login({
      id: matched.id,
      username: matched.username,
      nickname: matched.nickname,
      college: matched.college,
      campus: matched.campus,
    })
    router.push('/')
  } catch {
    errorMsg.value = '登录失败，请检查 Mock 服务是否启动'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="auth-view">
    <div class="auth-card">
      <h2>登录</h2>
      <p class="auth-sub">欢迎回到校园轻集市</p>

      <form class="auth-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label class="form-label">用户名</label>
          <input v-model="username" type="text" class="form-input" placeholder="请输入用户名" />
        </div>
        <div class="form-group">
          <label class="form-label">密码</label>
          <input v-model="password" type="password" class="form-input" placeholder="请输入密码" />
        </div>

        <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>

        <button type="submit" class="submit-btn" :disabled="loading">
          {{ loading ? '登录中…' : '登录' }}
        </button>
      </form>

      <p class="switch-link">
        还没有账号？<router-link to="/register">立即注册</router-link>
      </p>
      <p class="test-hint">测试账号：test / 123456</p>
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
.auth-card h2 {
  font-size: 24px; font-weight: 700; letter-spacing: -0.02em; text-align: center;
}
.auth-sub { text-align: center; font-size: 14px; color: var(--color-text-secondary); }
.auth-form { display: flex; flex-direction: column; gap: 16px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-label { font-size: 13px; font-weight: 600; color: var(--color-text); }
.form-input {
  padding: 10px 14px; border: 1px solid var(--color-border); border-radius: var(--radius-md);
  font-size: 14px; font-family: inherit; background: var(--color-surface); color: var(--color-text);
  outline: none; transition: border-color var(--transition-fast);
}
.form-input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }
.form-input::placeholder { color: var(--color-text-muted); }
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
.test-hint { text-align: center; font-size: 12px; color: var(--color-text-muted); }
</style>
