import { defineStore } from 'pinia'
import type { Question } from '@/types'

export const useSessionStore = defineStore("SessionStore", {
    state: () => ({
        title: "",
        subject: "",
        duration: 0,
        objectives: [] as string[],
        questions: [] as Question[],
        curveBall: {
            text: "",
            response: ""
        } as Question
    })
})