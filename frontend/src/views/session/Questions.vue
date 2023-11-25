<script setup lang="ts">
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Inplace from 'primevue/inplace'
import { computed, ref } from 'vue'
import { storeToRefs } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { useSessionStore } from '@/stores/SessionStore'

const sessionStore = useSessionStore()
const { questions: questions } = storeToRefs(sessionStore);
const newQuestion = ref("")
const editQuestion = ref("")
const isLoadingSuggestion = ref(false)
const isLoadingCurveBall = ref(false)
const editQuestionPT = computed(() => {
    return editQuestion.value != "" ? {} : {
        root: { class: 'border-red-400' }
    }
}) 
const areNoQuestions = computed(() => {
    return sessionStore.questions.length == 0
})
const inplacePT = computed(() => {
  return editQuestion.value != ""  ? {
    closeButton: {
        root: { class: 'ml-2' } 
    },
    display: { class: 'bg-gray-800' }
  } : {
    closeButton: {
        root: { class: 'bg-red-400 border-red-400 ml-3' } 
    },
    display: { class: 'bg-gray-800' }
  }
})

const addSuggestion = (concept: string) => {
    isLoadingSuggestion.value = true
    const questionList = questions.value.map(question => question.text).toString()
    axios.get<string>(`http://localhost:8000/suggestion/${concept}/${questionList}`)
    .then((response) => {
        if (response.data != "") {
            const question = {
                text: response.data,
                response: ""
            }
            sessionStore.add(question)
        }
        isLoadingSuggestion.value = false
    })
    .catch((error) => { 
        console.log(error) 
        isLoadingSuggestion.value = false
    })

    // axios.get<string>(`http://localhost:8000/test`)
    // .then((response) => {
    //     if (response.data != "") {
    //         console.log(response.data)
    //     }
    //     isLoadingSuggestion.value = false
    // })
    // .catch((error) => { 
    //     console.log(error) 
    //     isLoadingSuggestion.value = false
    // })
}

const addNewQuestion = () => {
    if (newQuestion.value != "") {
        const question = {
            text: newQuestion.value,
            response: ""
        }
        sessionStore.add(question)
        newQuestion.value = ""
    }
}

const handleQuestionEditClose = (index: number) => {
    if (editQuestion.value == "") {
        sessionStore.remove(index)
    } else {
        const newQuestion = {
            text: editQuestion.value,
            response: ""
        }
        sessionStore.replace(newQuestion, index)
    }
    editQuestion.value = ""
}

const handleQuestionEditOpen = (question: string) => {
    editQuestion.value = question
}

const done = (concept: string) => {
    router.push("/begin")
    // isLoadingCurveBall.value = true
    // const questionList = questions.value.map(question => question.text).toString()
    // axios.get<string>(`http://localhost:8000/curve-ball/${concept}/${questionList}`)
    // .then((response) => {
    //     if (response.data != "") {
    //         const question = {
    //             text: response.data,
    //             response: ""
    //         }
    //         sessionStore.setCurveBall(question)
    //     }
    //     isLoadingCurveBall.value = false
    //     router.push("/quiz")
    // })
    // .catch((error) => { 
    //     console.log(error) 
    //     isLoadingCurveBall.value = false
    // }) 
}

const back = () => {
    router.push("/")
}
</script>

<template>
    <div class="flex flex-column justify-content-center gap-3">
        <div>
            <h2>Questions on {{ sessionStore.subject }}</h2>
            <p>add questions that you would like to review.</p>
        </div>
        <div class="flex flex-column gap-4">
            <div v-for="(question, index) in questions" :key="index">
                <div class="flex flex-column justify-content-center gap-3">
                    <label :for="index.toString()">Question {{ index + 1 }}</label>
                    <div class="flex flex-row gap-4">
                        <Inplace 
                        :pt="inplacePT"
                        :closable="true" 
                        @close="() => handleQuestionEditClose(index)" 
                        @open="() => handleQuestionEditOpen(question.text)">
                            <template #display> {{ question.text }} </template>
                            <template #content>
                                <InputText 
                                :id="index.toString()" 
                                v-model="editQuestion"
                                :pt="editQuestionPT"
                                />
                            </template>
                        </Inplace>
                    </div>
                </div>
            </div>
            <div>
                <InputText id="newQuestion" v-model="newQuestion" placeholder="enter a question 🫵"/>
            </div>
            <Button @click="addNewQuestion">Add Question</Button>
            <Button v-if="!areNoQuestions" @click="() => addSuggestion($route.params.topic as string)" :loading="isLoadingSuggestion">Suggest Question ✨</Button>
            <Button @click="back">Back</Button>
            <Button :loading="isLoadingCurveBall" @click="() => done($route.params.topic as string)">Done</Button>
        </div>
    </div>
</template>

<style scoped>
    h2, label {
        font-weight: bold;
    }
</style>