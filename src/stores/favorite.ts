import { defineStore } from 'pinia'
import { ref, computed, watch } from 'vue'

export interface FavoriteItem {
  id: number
  type: 'trade' | 'lostFound' | 'groupBuy' | 'errand'
  title: string
  price?: number
  campus: string
  addedAt: string
}

const STORAGE_KEY = 'campus_favorites'

function loadFavorites(): FavoriteItem[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch { return [] }
}

function saveFavorites(list: FavoriteItem[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(list))
}

export const useFavoriteStore = defineStore('favorite', () => {
  const favorites = ref<FavoriteItem[]>(loadFavorites())

  watch(favorites, (val) => saveFavorites(val), { deep: true })

  const count = computed(() => favorites.value.length)

  function isFavorited(id: number): boolean {
    return favorites.value.some(f => f.id === id)
  }

  function addFavorite(item: FavoriteItem) {
    if (!isFavorited(item.id)) {
      favorites.value.push({ ...item, addedAt: new Date().toLocaleString() })
    }
  }

  function removeFavorite(id: number) {
    favorites.value = favorites.value.filter(f => f.id !== id)
  }

  function toggleFavorite(item: FavoriteItem) {
    if (isFavorited(item.id)) {
      removeFavorite(item.id)
    } else {
      addFavorite(item)
    }
  }

  function clearAll() {
    favorites.value = []
    localStorage.removeItem(STORAGE_KEY)
  }

  return { favorites, count, isFavorited, addFavorite, removeFavorite, toggleFavorite, clearAll }
})
