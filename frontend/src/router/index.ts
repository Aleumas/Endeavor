import { createRouter, createWebHistory } from 'vue-router'
import SessionForm from '../views/session/SessionForm.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'session-form',
      component: SessionForm
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: () => import('../views/session/Quiz.vue')
    }, 
    {
      path: '/questions',
      name: 'questions',
      component: () => import('../views/session/Questions.vue')
    },
    {
      path: '/begin',
      name: 'begin',
      component: () => import('../views/session/Begin.vue')
    },
    {
      path: '/feedback',
      name: 'feedback',
      component: () => import('../views/feedback/Feedback.vue')
    }
  ]
})

export default router
