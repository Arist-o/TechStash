import {createWebHistory,createRouter} from 'vue-router'

import login from '../components/LoginPage.vue'

const routes = [
    {
        path: '/',
        name: 'login',
        component: login
    }
]

const router =createRouter({
    history: createWebHistory(),
    routes
})

export default router
