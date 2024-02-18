<script setup lang="ts">
import { Alert, AlertDescription } from "@/components/ui/alert"
import { useSession } from "@/stores/session"
import { onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()

const session = useSession()
onMounted(async () => {
  await session.logout()
  router.push("/login")
})
</script>

<template>
  <Alert>
    <AlertDescription>You have been logged out.</AlertDescription>
  </Alert>
</template>
