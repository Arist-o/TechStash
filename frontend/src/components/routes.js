import {createWebHistory,createRouter} from 'vue-router'

import LoginPage from '../components/LoginPage.vue'
import MainLayout from '../components/MainLayout.vue'
import MainContent from '../components/MainContent.vue'

const routes = [
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/',
        component: MainLayout,
        children: [
            {
                path: '',
                name: 'home',
                component: MainContent
            }
        ]
    }
]

const router =createRouter({
    history: createWebHistory(),
    routes
})

export default router
