import http from './http'

export function getGroupBuys() {
  return http.get('/groupBuys')
}

export function getGroupBuyById(id: number) {
  return http.get(`/groupBuys/${id}`)
}
