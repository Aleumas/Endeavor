<script setup lang="ts">
import { ref, watch } from 'vue'
import { useTime } from 'vue-timer-hook'

const loadingMessages = ["Giving feedback", "Hold on tight", "Almost there", "😔"]

const messageIndex = ref(0)

const time = useTime('12-hour')

watch(time.seconds, async (newValue, _) => {
    if (newValue % 5 == 0) {
        messageIndex.value = (messageIndex.value + 1) % loadingMessages.length
    }
})

</script>

<template>
    <div class="flex justify-content-center align-items-center">
        <i class="pi pi-spin pi-cog" style="font-size: 10rem"></i>
        <h2>{{ loadingMessages[messageIndex] }}</h2>
    </div>
</template>