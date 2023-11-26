<script setup lang="ts">
import { useFeedbackStore } from '@/stores/FeedbackStore';
import { useSessionStore } from '@/stores/SessionStore';
import axios from 'axios';
import { computed, ref, watch } from 'vue'
import { useTime } from 'vue-timer-hook'
import type { Feedback, FeedbackWrapper } from '@/types'
import router from '@/router';

const loadingMessages = ["Generating feedback", "Hold on tight", "Almost there", "😔"]

const messageIndex = ref(0)

const time = useTime('12-hour')

const feedbackStore = useFeedbackStore()

watch(time.seconds, async (newValue, _) => {
    if (newValue % 5 == 0) {
        messageIndex.value = (messageIndex.value + 1) % loadingMessages.length
    }
})

const sessionStore = useSessionStore()

const apiRequests = [] as Promise<void>[]

sessionStore.questions.forEach(question => {
    const requestPromise = axios.get<Feedback>(`http://localhost:8000/feedback/${encodeURIComponent(question.text)}/${encodeURIComponent(question.response)}`)
    .then((response) => {
        console.log(response.data)
      feedbackStore.add(response.data);
    })
    .catch(() => { 
      router.push("/questions");
    });

    apiRequests.push(requestPromise)
})

Promise.all(apiRequests)
  .then(() => {
    router.push("/feedback");
  })
  .catch((error) => {
    console.error("Error during API calls:", error);
  });
</script>

<template>
    <div class="flex justify-content-center align-items-center">
        <div class="flex flex-column gap-4 align-items-center">
            <div>
                <i class="pi pi-spin pi-cog" style="font-size: 5rem"></i>
            </div>
            <h2>{{ loadingMessages[messageIndex] }}</h2>
        </div>
    </div>
</template>