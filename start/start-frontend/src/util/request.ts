import axios from "axios"

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 8000, // 可选
})

/* ① 响应拦截器 */
api.interceptors.response.use(
  // 2xx 范围
  (response) => {
    // 只返回业务数据，调用层直接拿到 data
    return response.data
  },

  // 非 2xx 范围
  async (error) => {
    const { response } = error

    // 统一错误提示
    if (response) {
      // 后端返回的错误信息
      const msg = response.data?.message || response.statusText

      // 这里用你项目里的 Toast / Message / ElMessage 等
      console.error(`[${response.status}] ${msg}`)

      // 登录态失效 → 跳登录
      if (response.status === 401 || response.status === 403) {
        // 示例：React-Router v6
        // import { useNavigate } from 'react-router-dom';
        // navigate('/login');
        window.location.href = "/login"
      }

      return Promise.reject({ code: response.status, message: msg })
    }

    // 网络超时 / 断网
    console.error("Network or timeout error")
    return Promise.reject({ code: 0, message: "网络异常，请稍后重试" })
  },
)

export default api
