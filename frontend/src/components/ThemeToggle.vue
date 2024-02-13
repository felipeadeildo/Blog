<script setup lang="ts">
import { Button } from "./ui/button"
import { useTheme } from "@/stores/theme"
import { Sun, Moon } from "lucide-vue-next"

const theme = useTheme()
</script>

<template>
  <Button @click="theme.toggle()" size="icon" variant="outline" class="rounded-full">
    <component :is="theme.isDark ? Sun : Moon" />
  </Button>
</template>
