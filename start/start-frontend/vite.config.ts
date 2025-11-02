// https://vite.dev/config/
import {defineConfig, loadEnv} from "vite"
import react from "@vitejs/plugin-react-swc";
import { resolve } from "path";

export default defineConfig(({mode}) => {
    const env = loadEnv(mode, process.cwd(), '')
    return {
        plugins: [react()],
        // 路径别名
        resolve: {
          alias: {
            '@': resolve(__dirname, 'src'),
          },
        },

        // 本地 dev 代理
        server: {
          proxy: {
            '/api': {
              target: env.VITE_API_BASE || 'http://127.0.0.1:8000',
              changeOrigin: true,
              rewrite: (p) => p.replace(/^\/api/, ''),
            },
          },
        },

        // 构建配置
        build: {
          outDir: resolve(__dirname, '../templates'), // index.html 放这里
          assetsDir: '../static',                     // js/css 放 <root>/static/
          emptyOutDir: true,
        },


    }

})