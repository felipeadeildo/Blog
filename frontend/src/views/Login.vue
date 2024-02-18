<script setup lang="ts">
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { AlertCircle, LogIn } from "lucide-vue-next"
import { ref } from "vue"
import { useRouter } from "vue-router"
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"
import { useSession } from "@/stores/session"

const username = ref("")
const password = ref("")
const isLoading = ref(false)
const error = ref("")
const router = useRouter()

const user = useSession()

if (user.isLoggedIn) {
  router.push("/")
}

const handleSubmit = async () => {
  isLoading.value = true
  try {
    await user.login(username.value, password.value)
    if (user.isLoggedIn) router.push("/")
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
