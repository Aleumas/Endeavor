<script setup lang="ts">
import router from '@/router';
import { useSessionStore } from '@/stores/SessionStore';
import axios from 'axios';
import Button from 'primevue/button'
import ToggleButton from 'primevue/togglebutton';
import { ref } from 'vue';

const wantsCurveBall = ref(false)
const sessionStore = useSessionStore()
const generateCurveBall = async () => {
    const questionList = sessionStore.questions.map(question => encodeURIComponent(question.text)).toString()
    axios.get<string>(`http://localhost:8000/curve-ball/${sessionStore.subject}/${questionList}`)
    .then((response) => {
        if (response.data != "") {
            const question = {
                text: response.data,
                response: ""
            }
            sessionStore.setCurveBall(question)
        }
        router.push("/quiz")
    })
    .catch((error) => { 
        console.log(error) 
    }) 
}

function go() {
    if (wantsCurveBall.value) {
        generateCurveBall()
    }
    router.push("/quiz")
}
</script>

<template>
    <div class="flex flex-column gap-5 ">
        <h1>Do you want a curveball?</h1>
        <ToggleButton v-model="wantsCurveBall" onLabel="Give it to me! 💪" offLabel="I'm good. 👋" class="w-9rem" />

        <h1>Are you ready to begin your study session?</h1>
        <Button label="Lets go!" @click="go"/>
    </div>
</template>