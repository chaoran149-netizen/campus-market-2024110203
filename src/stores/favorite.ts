import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface FavoriteItem {
  id: number
  type: 'trade' | 'lostFound' | 'groupBuy' | 'errand'
  title: string
  price?: number
  campus: string
  addedAt: string
}

export const useFavoriteStore = defineStore('favorite', () => {
  const favorites = ref<FavoriteItem[]>([])

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
  }

  return { favorites, count, isFavorited, addFavorite, removeFavorite, toggleFavorite, clearAll }
})
