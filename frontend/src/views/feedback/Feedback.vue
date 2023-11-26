<script setup lang="ts">
import Fieldset from 'primevue/fieldset'
import { useFeedbackStore } from '@/stores/FeedbackStore'
import { useSessionStore } from '@/stores/SessionStore';

const { feedback: feedback } = useFeedbackStore()
const { questions: questions } = useSessionStore()

const getColorForRating = (rating: number):string => {
    switch(rating) {
        case 1:
            return "-red-500"
        case 2:
            return "-orange-400"
        case 3: 
            return "-orange-500"
        case 4:
            return "-teal-500"
        case 5:
            return "-green-500"
        default:
            return ""
    }
}
console.log(feedback[0].value)
</script>

<template>
    <div class="flex flex-column gap-5">
        <div v-for="(individualFeedback, index) in feedback">
            <Fieldset 
            :pt="{
                    toggleableContent: { class: 'border' + getColorForRating(individualFeedback.rating) },
                    legend: { class: 'bg' + getColorForRating(individualFeedback.rating) },
                    legendTitle: { class: 'text-white' },
                    togglerIcon: { class: 'text-white' }
                }"
            :legend="individualFeedback.value.question">
            <div class="flex flex-column gap-3">
                <div>
                    <h4 class="font-bold">response:</h4>
                    <p class="m-0">
                        {{ individualFeedback.value.response }}
                    </p>
                </div>
                <div>
                    <h4 class="font-bold">feedback:</h4>
                    <p class="m-0">
                        {{ individualFeedback.value.feedback }}
                    </p>
                </div>
            </div>
            </Fieldset>
        </div>
    </div>
</template>