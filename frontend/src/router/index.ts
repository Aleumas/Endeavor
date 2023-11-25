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
      path: '/selection',
      name: 'topic-selection',
      component: () => import('../views/ConceptSelection.vue')
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: () => import('../views/Quiz.vue')
    }, 
    {
      path: '/questions',
      name: 'questions',
      component: () => import('../views/session/Questions.vue')
    }
  ]
})

export default router
