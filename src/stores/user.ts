import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface User {
  nickname: string
  college: string
  campus: string
  role: string
  creditScore: number
  avatar: string
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User>({
    nickname: '校园用户',
    college: '计算机学院',
    campus: '主校区',
    role: '学生',
    creditScore: 85,
    avatar: '',
  })

  const isLoggedIn = computed(() => user.value.nickname.trim().length > 0)
  const displayName = computed(() => user.value.nickname)
  const initial = computed(() => user.value.nickname.charAt(0))

  function updateUser(partial: Partial<User>) {
    user.value = { ...user.value, ...partial }
  }

  function resetUser() {
    user.value = {
      nickname: '校园用户',
      college: '计算机学院',
      campus: '主校区',
      role: '学生',
      creditScore: 85,
      avatar: '',
    }
  }

  return { user, isLoggedIn, displayName, initial, updateUser, resetUser }
})
