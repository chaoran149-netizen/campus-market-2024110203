import http from './http'

export function getErrands() {
  return http.get('/errands')
}

export function getErrandById(id: number) {
  return http.get(`/errands/${id}`)
}
