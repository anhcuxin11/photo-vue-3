import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/LoginPage.vue';
import Register from '../components/Register.vue';
import Home from '../components/Home.vue';
import Notification from '../components/Notification.vue';
import Chat from '../components/Chat.vue';

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/notification',
    name: 'notification',
    component: Notification,
  },
  {
    path: '/chat',
    name: 'chat',
    component: Chat,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
