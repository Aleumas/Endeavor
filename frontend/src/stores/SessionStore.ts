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
    actions: {
        add(question: Question) {
          this.questions.push(question)
        },
        remove(index: number) {
          const questionToRemove = this.questions[index]
          this.questions = this.questions.filter(
            (question) => question !== questionToRemove
          )
        },
        replace(question: Question, index: number) {
          this.questions[index] = question 
        },
        setCurveBall(question: Question) {
          this.curveBall = question
        }
      },
})