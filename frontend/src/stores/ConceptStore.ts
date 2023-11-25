import { defineStore } from 'pinia'
import type { Concepts } from '@/types'

export const useConceptStore = defineStore("ConceptStore", {
    state: () => ({
        concepts: [] as string[],
        tags: [] as string[]
      }),
    actions: {
        fill(concepts: Concepts) {
            this.concepts = concepts.value
            this.tags = concepts.tags 
        }
    }
})