<script setup lang="ts">
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import ProgressBar from 'primevue/progressbar'
import { computed, ref, watch } from 'vue'
import { useSessionStore } from '@/stores/SessionStore'
import { storeToRefs } from 'pinia'
import { useTimer } from 'vue-timer-hook'

const isQuestionAnswered = ref(false)
const sessionStore = useSessionStore()
const { questions: questions, curveBall: curveBall } = storeToRefs(sessionStore)
const capitalize = (s: string) => s && s[0].toUpperCase() + s.slice(1)

const isOnFinalQuestion = computed(() => {
    return questionIndex.value == questions.value.length - 1
})
const isOnFirstQuestion = computed(() => {
    return questionIndex.value == 0
})
const sessionHasCurveBall = computed(() => {
    return curveBall.value.text.length != 0
})

const questionIndex = ref(0)
const progress = computed(() => {
    if (questions.value.length == 0) { return 0} 
    return Math.floor(((questionIndex.value + 1) / questions.value.length) * 100)
})
const next = () => {
    questionIndex.value += 1
}

const back = () => {
    questionIndex.value -= 1
}

const submit = () => {
    isQuestionAnswered.value = true
}

const time = new Date();
time.setSeconds(time.getSeconds() + sessionStore.duration.code); 
const timer = useTimer(time)
timer.start()

watch(timer.isExpired, async (isExpired, _) => {
    if (isExpired) {
        console.log('done')
        submit()
    }
})

</script>

<template>
    <div class="flex flex-column justify-content-center gap-5">
        <h2>{{ capitalize(questions[questionIndex].text) }}</h2>
        <div class="flex flex-column justify-content-center gap-3">
            <InputText id="answer" v-model="questions[questionIndex].response"/>
            <Button type="button" @click="() => isOnFinalQuestion && !sessionHasCurveBall ? submit() : next()" >{{ !isOnFinalQuestion ? "Next" : "Finish" }}</Button>
            <Button v-if="!isOnFirstQuestion" @click="back">Back</Button>
            <div v-if="isQuestionAnswered">
                
            </div>
        </div>
        <ProgressBar :value="progress" />
        <h1>{{ timer.hours.value + ":" + timer.minutes.value + ":" + timer.seconds.value }}</h1>
    </div>
</template>

<style scoped>
h2 {
    font-weight: bold;
}
</style>