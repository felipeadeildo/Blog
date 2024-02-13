<script setup lang="ts">
import { RouterView, RouterLink } from "vue-router"
import { Button } from "./components/ui/button"
import ThemeToggle from "./components/ThemeToggle.vue"
import { Home, LogIn } from "lucide-vue-next"
import { onMounted, ref } from "vue"
import { getUser } from "./lib/utils"
import { User } from "./types/user"

const user = ref<User | null>(null)

onMounted(async () => {
  user.value = await getUser()
})
</script>

<template>
  <div class="flex gap-3 justify-end items-center rounded-b-md h-12 bg-accent px-4">
    <Button as-child variant="link" v-if="user">
      <RouterLink to="/home">
        Home
        <Home class="ml-2" />
      </RouterLink>
    </Button>
    <Button as-child variant="link">
      <RouterLink to="/login" v-if="!user">
        Login
        <LogIn class="ml-2" />
      </RouterLink>

      <RouterLink to="/logout" v-else>
        Leave
        <LogIn class="ml-2" />
      </RouterLink>
    </Button>
    <ThemeToggle />
  </div>
  <div class="container">
    <RouterView />
  </div>
</template>
