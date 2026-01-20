import 'bootstrap/dist/css/bootstrap.min.css'


import { createApp } from 'vue'
import App from './App.vue'
import router from '../src/components/routes.js'

const app = createApp(App)
app.use(router)
app.mount('#app')
