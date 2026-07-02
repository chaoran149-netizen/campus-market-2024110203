import http from './http'

export function getErrands() {
  return http.get('/errands')
}

export function getErrandById(id: number) {
  return http.get(`/errands/${id}`)
}

export function createErrand(data: {
  title: string; taskType: string; reward: number;
  pickupLocation: string; deliveryLocation: string;
  deadline: string; description: string;
  campus: string; publisher: string; status: string; image?: string;
}) {
  return http.post('/errands', data)
}
