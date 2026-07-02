import http from './http'

export function getGroupBuys() {
  return http.get('/groupBuys')
}

export function getGroupBuyById(id: number) {
  return http.get(`/groupBuys/${id}`)
}

export function createGroupBuy(data: {
  title: string; type: string; targetCount: number;
  deadline: string; location: string; description: string;
  campus: string; publisher: string; status: string;
  currentCount: number; image?: string;
}) {
  return http.post('/groupBuys', data)
}

export function deleteGroupBuy(id: number) {
  return http.delete(`/groupBuys/${id}`)
}
