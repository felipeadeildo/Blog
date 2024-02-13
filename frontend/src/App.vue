<script setup lang="ts">
import { RouterView, RouterLink } from "vue-router"
import { Button } from "./components/ui/button"
import ThemeToggle from "./components/ThemeToggle.vue"
import { Home, LogIn } from "lucide-vue-next"
</script>

<template>
  <div class="flex gap-3 justify-end items-center rounded-b-md h-12 bg-accent px-4">
    <Button as-child variant="link">
      <RouterLink to="/home">
        Home
        <Home class="ml-2" />
      </RouterLink>
    </Button>
    <Button as-child variant="link">
      <RouterLink to="/login">
        Login
        <LogIn class="ml-2" />
      </RouterLink>
    </Button>
    <ThemeToggle />
  </div>
  <div class="container">
    <RouterView />
  </div>
</template>
