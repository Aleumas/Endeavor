<script setup lang="ts">
import Button from 'primevue/button'
import { useConceptStore } from "@/stores/ConceptStore.js";
import router from '@/router';

const conceptStore = useConceptStore()

const handleConcept = (concept: string) => {
  router.push(`questions/${concept}`)
}
</script>

<template>
  <div class="flex flex-column justify-content-center gap-5">
    <h2>Select a concept</h2>
    <div class="grid">
      <div class="col-fixed " v-for="concept in conceptStore.concepts">
        <Button @click="() => handleConcept(concept)"  class="text-center p-3 border-round-sm bg-primary font-bold">{{ concept }}</Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  text-align: center;
  font-weight: bold;
}
</style>
