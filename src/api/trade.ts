import http from './http'

export function getTrades() {
  return http.get('/trades')
}

export function getTradeById(id: number) {
  return http.get(`/trades/${id}`)
}

export function createTrade(data: {
  title: string; price: number; category: string; condition: string;
  location: string; campus: string; description: string;
  publisher: string; publishTime: string; status: string; image?: string;
}) {
  return http.post('/trades', data)
}
