<script setup lang="ts">
import { useFeedbackStore } from '@/stores/FeedbackStore';
import { useSessionStore } from '@/stores/SessionStore';
import axios from 'axios';
import { computed, ref, watch } from 'vue'
import { useTime } from 'vue-timer-hook'
import type { Feedback } from '@/types'
import router from '@/router';

const loadingMessages = ["Giving feedback", "Hold on tight", "Almost there", "😔"]

const messageIndex = ref(0)

const time = useTime('12-hour')

const feedbackStore = useFeedbackStore()

watch(time.seconds, async (newValue, _) => {
    if (newValue % 5 == 0) {
        messageIndex.value = (messageIndex.value + 1) % loadingMessages.length
    }
})

const sessionStore = useSessionStore()

const questions = computed(() => {
    return sessionStore.questions.map(question => question.text)
})

const responses = computed(() => {
    return sessionStore.questions.map(question => question.response) 
})


axios.get<Feedback>(`http://localhost:8000/feedback/${questions.value.toString()}/${responses.value.toString()}`)
    .then((response) => {
        feedbackStore.add(response.data)
        router.push("/feedback")
    })
    .catch((error) => { 
        router.push("/questions")
    })
</script>

<template>
    <div class="flex justify-content-center align-items-center">
        <i class="pi pi-spin pi-cog" style="font-size: 10rem"></i>
        <h2>{{ loadingMessages[messageIndex] }}</h2>
    </div>
</template>