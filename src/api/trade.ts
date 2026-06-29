import http from './http'

export function getTrades() {
  return http.get('/trades')
}

export function getTradeById(id: number) {
  return http.get(`/trades/${id}`)
}
