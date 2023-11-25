<script setup lang="ts">
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import ProgressBar from 'primevue/progressbar'
import { computed, ref } from 'vue'
import { useQuestionStore } from '@/stores/QuestionStore'
import { storeToRefs } from 'pinia'

const isQuestionAnswered = ref(false)
const questionStore = useQuestionStore()
const { questions: questions } = storeToRefs(questionStore)
const capitalize = (s: string) => s && s[0].toUpperCase() + s.slice(1)

const isOnFinalQuestion = computed(() => {
    return questionIndex.value == questions.value.length - 1
})
const isOnFirstQuestion = computed(() => {
    return questionIndex.value == 0
})

const questionIndex = ref(0)
const progress = computed(() => {
    if (questions.value.length == 0) { return 0} 
    console.log("questions: ", questions.value.length)
    console.log("index: ", questionIndex.value)
    return Math.floor(((questionIndex.value + 1) / questions.value.length) * 100)
})
const next = () => {
    questionIndex.value += 1
}

const back = () => {
    questionIndex.value -= 1
}

const submit = () => {
    console.log(questions.value)
    console.log(questionStore.curveBall)
    isQuestionAnswered.value = true
}
</script>

<template>
    <div class="flex flex-column justify-content-center gap-5">
        <h2>{{ capitalize(questions[questionIndex].text) }}</h2>
        <div class="flex flex-column justify-content-center gap-3">
            <InputText id="answer" v-model="questions[questionIndex].response"/>
            <Button type="button" @click="() => isOnFinalQuestion ? submit() : next()" >{{ !isOnFinalQuestion ? "Next" : "Finish" }}</Button>
            <Button v-if="!isOnFirstQuestion" @click="back">Back</Button>
            <div v-if="isQuestionAnswered">
                
            </div>
        </div>
        <ProgressBar :value="progress" />
    </div>
</template>

<style scoped>
h2 {
    font-weight: bold;
}
</style>