import { defineStore } from 'pinia'
import type { Question } from '@/types'
import {v4 as uuidv4} from 'uuid'

export const useSessionStore = defineStore("SessionStore", {
    state: () => ({
        title: "",
        subject: "",
        duration: { name: "", code: 0 },
        objectives: [] as string[],
        questions: [] as Question[],
        curveBall: {
            text: "",
            response: ""
        } as Question,
        id: uuidv4()
    }),
})