import './assets/main.css'
import "/node_modules/primeflex/primeflex.css"
import "primevue/resources/themes/viva-light/theme.css";
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import Ripple from 'primevue/ripple'
import Colada, { PiniaColadaPlugin } from 'colada-plugin'

const pinia = createPinia()
const app = createApp(App)

app.use(router)
app.use(pinia)
pinia.use(PiniaColadaPlugin)
app.use(Colada)
app.use(PrimeVue, { ripple: true })

app.directive('ripple', Ripple);

app.mount('#app')
