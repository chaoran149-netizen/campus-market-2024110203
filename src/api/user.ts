import http from './http'

export function getUsers(params?: { username?: string }) {
  return http.get('/users', { params })
}

export function createUser(data: {
  username: string
  password: string
  nickname: string
  college: string
  campus: string
}) {
  return http.post('/users', data)
}
