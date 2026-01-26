import { createWebHistory, createRouter } from 'vue-router'
import LoginPage from './LoginPage.vue'
import MainLayout from './MainLayout.vue'
import MainContent from './MainContent.vue'

const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/maincontent',
        component: MainLayout, // Головний каркас
        children: [
            {
                path: '', // Порожній шлях всередині /maincontent
                name: 'main',
                component: MainContent // Ваші картки
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router