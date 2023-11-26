import { defineStore } from 'pinia'
import type { Feedback } from '@/types'

export const useFeedbackStore = defineStore("FeedbackStore", {
    state: () => ({
        feedback: [] as Feedback[],
        id: ""
    }),
    actions: {
        add(feedback: Feedback) {
            this.feedback.push(feedback)
        },
    }
})