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
                <p class="m-0">
                    response:
                    {{ questions[index].response }}

                    feedback:
                    {{ individualFeedback.value.feedback }}
                </p>
            </Fieldset>
        </div>
    </div>
</template>