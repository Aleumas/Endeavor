<script setup lang="ts">
import { ref } from 'vue'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Dropdown from 'primevue/dropdown'
import router from '@/router'
import { useSessionStore } from '@/stores/SessionStore'
import axios from 'axios';
import { storeToRefs } from 'pinia'

const loading = ref(false)
const sessionStore = useSessionStore()
const { title: title, subject: subject, duration: duration, objectives: objectives } = storeToRefs(sessionStore);
const index = ref(0)
const durationOptions = ref([
    {name: '5 sec', code: 5},
    { name: '10 mins', code: 600 },
    { name: '30 mins', code: 1800 },
    { name: '1 hour', code: 3600 },
]);

const next = () => {
  if (index.value == 2) {
    router.push('/questions')
    return 
  }

  index.value += 1
}
const back = () => {
  index.value -= 1
}
</script>

<template>
  <h1>Session</h1>
  <div class="flex flex-column gap-2">
  <div v-if="index == 0" class="flex flex-column gap-2">
    <label for="subject">Title</label>
    <InputText id="subject" v-model="title" placeholder="e.g., Learing"/>
    <small id="subject-hint">Enter a title for the session.</small>
  </div>
  <div v-if="index == 1" class="flex flex-column gap-2">
    <label for="subject">Subject</label>
    <InputText id="subject" v-model="subject" placeholder="e.g., Calculus"/>
    <small id="subject-hint">Enter a subject for the session.</small>
  </div>
  <div v-if="index == 2" class="flex flex-column gap-2">
    <label for="subject">Duration</label>
    <Dropdown v-model:model-value="duration" :options="durationOptions" optionLabel="name" placeholder="e.g., 30 mins"/>
    <small id="subject-hint">Enter a duration for the session.</small>
  </div>
  <div class="flex flex-column gap-2">
    <div class="flex flex-row gap-2">
      <Button v-if="index != 0" type="button" label="Back" :loading="loading" @click="back" />
      <Button type="button" label="Next" :loading="loading" @click="next" />
    </div>
  </div>
  </div>
</template>