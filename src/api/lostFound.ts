import http from './http'

export function getLostFounds() {
  return http.get('/lostFounds')
}

export function getLostFoundById(id: number) {
  return http.get(`/lostFounds/${id}`)
}

export function createLostFound(data: {
  title: string; type: string; itemName: string;
  location: string; time: string; description: string;
  contact: string; status: string; campus: string; image?: string;
}) {
  return http.post('/lostFounds', data)
}
