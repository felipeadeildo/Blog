<script setup lang="ts">
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { AlertCircle, LogIn } from "lucide-vue-next"
import { onMounted, ref } from "vue"
import { useRouter } from "vue-router"
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"
import { agent, getUser } from "@/lib/utils"
import { User } from "@/types/user"

const username = ref("")
const password = ref("")
const isLoading = ref(false)
const error = ref("")
const router = useRouter()

const user = ref<User | null>(null)

onMounted(async () => {
  user.value = await getUser()
})

if (user) {
  router.push("/")
}

const handleSubmit = async () => {
  isLoading.value = true
  try {
    const res = await agent.post("/login", {
      username: username.value,
      password: password.value,
    })
    if (res.status === 200) {
      error.value = ""
      router.go(0)
      router.push("/")
    } else throw new Error()
  } catch {
    error.value = "Invalid username or password"
  }
  isLoading.value = false
}
</script>

<template>
  <div class="flex items-center justify-center flex-col mx-auto mt-40 gap-4 max-w-sm">
    <h1 class="text-3xl">Login</h1>

    <Alert v-if="error" variant="destructive">
      <AlertCircle class="h-4 w-4" />
      <AlertTitle>Error</AlertTitle>
      <AlertDescription>{{ error }}</AlertDescription>
    </Alert>

    <Input placeholder="Username" v-model="username" :disabled="isLoading" />
    <Input
      type="password"
      placeholder="Password"
      v-model="password"
      :disabled="isLoading"
      @keyup.enter="handleSubmit"
    />

    <Button @click="handleSubmit" :disabled="isLoading">
      <LogIn class="mr-2" />
      Entrar
    </Button>
  </div>
</template>
