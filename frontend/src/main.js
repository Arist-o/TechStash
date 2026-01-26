import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './components/routes.js' // Перевірте шлях до файлу routes.js

const app = createApp(App)
app.use(router)
app.mount('#app')