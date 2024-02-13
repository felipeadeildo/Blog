<script setup lang="ts">
import { useRouter } from "vue-router"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { onMounted } from "vue"
import { agent } from "@/lib/utils"
const router = useRouter()

onMounted(async () => {
  await agent.get("/logout")
  router.go(0)
})
</script>

<template>
  <Alert>
    <AlertDescription>You have been logged out.</AlertDescription>
  </Alert>
</template>
