import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export interface User {
  id: number
  username: string
  nickname: string
  college: string
  campus: string
}

const STORAGE_KEY = 'campus_user'

function loadFromStorage(): User | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : null
  } catch {
    return null
  }
}

function saveToStorage(user: User) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(user))
}

function clearStorage() {
  localStorage.removeItem(STORAGE_KEY)
}

export const useUserStore = defineStore('user', () => {
  const currentUser = ref<User | null>(loadFromStorage())

  const isLoggedIn = computed(() => currentUser.value !== null)
  const displayName = computed(() => currentUser.value?.nickname ?? '')
  const initial = computed(() => currentUser.value?.nickname?.charAt(0) ?? '?')

  function login(user: User) {
    currentUser.value = user
    saveToStorage(user)
  }

  function logout() {
    currentUser.value = null
    clearStorage()
  }

  function restoreLogin() {
    const saved = loadFromStorage()
    if (saved) currentUser.value = saved
  }

  return { currentUser, isLoggedIn, displayName, initial, login, logout, restoreLogin }
})
