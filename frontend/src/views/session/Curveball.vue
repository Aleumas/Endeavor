<script setup lang="ts">
import router from '@/router';
import { useSessionStore } from '@/stores/SessionStore'
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { storeToRefs } from 'pinia';

const capitalize = (s: string) => s && s[0].toUpperCase() + s.slice(1)
const sessionStore = useSessionStore()
const { curveBall: curveBall } = storeToRefs(sessionStore)
const back = () => {
    router.push('/questions')
}

const submit = () => {
   router.push('/feedback-loader') 
}

</script>

<template>
    <div class="flex flex-column justify-content-center gap-5">
        <h2>{{ capitalize(curveBall.text) }}</h2>
        <div class="flex flex-column justify-content-center gap-3">
            <InputText id="answer" v-model="curveBall.response"/>
            <Button type="button" @click="submit"> Finish </Button>
            <Button type="button" @click="back">Back</Button>
        </div>
    </div>
</template>