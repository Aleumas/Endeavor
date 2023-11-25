<script setup lang="ts">
import router from '@/router';
import Button from 'primevue/button'
import ToggleButton from 'primevue/togglebutton';
import { ref } from 'vue';

const wantsCurveBall = ref(false)
const generateCurveBall = async () => {

}

function go() {
    if (wantsCurveBall) {
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