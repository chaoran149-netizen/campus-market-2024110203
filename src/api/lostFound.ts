import http from './http'

export function getLostFounds() {
  return http.get('/lostFounds')
}

export function getLostFoundById(id: number) {
  return http.get(`/lostFounds/${id}`)
}
