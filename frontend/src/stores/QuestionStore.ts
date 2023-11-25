import type { Question } from '@/types'
import { defineStore } from 'pinia'

export const useQuestionStore = defineStore("QuestionStore", {
    state: () => ({
      questions: [] as Question[],
      curveBall: {
        text: "",
        response: ""
      } as Question
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
  