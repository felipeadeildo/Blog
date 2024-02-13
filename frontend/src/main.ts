import "@/assets/index.css"
import { createPinia } from "pinia"
import { createApp } from "vue"
import App from "./App.vue"
import { router } from "./routes"

const pinia = createPinia()

const app = createApp(App)

app.use(pinia)
app.use(router)

app.mount("#app")
