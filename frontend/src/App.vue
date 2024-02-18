<script setup lang="ts">
import { RouterView, RouterLink } from "vue-router"
import { Button } from "./components/ui/button"
import ThemeToggle from "./components/ThemeToggle.vue"
import { Home, LogIn } from "lucide-vue-next"
import { useSession } from "./stores/session"

const session = useSession()
</script>

<template>
  <div class="flex justify-between gap-3 items-center rounded-b-md bg-accent px-4 py-1">
    <div class="justify-start text-primary">
      <span v-if="session.isLoggedIn"> Welcome, {{ session.user?.username }}! </span>
      <span v-else> Welcome! </span>
    </div>
    <div class="flex justify-end items-center">
      <Button as-child variant="link" v-if="session.isLoggedIn">
        <RouterLink to="/home">
          Home
          <Home class="ml-2" />
        </RouterLink>
      </Button>
      <Button as-child variant="link">
        <RouterLink to="/login" v-if="!session.isLoggedIn">
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
  </div>
  <div class="container">
    <RouterView />
  </div>
</template>
