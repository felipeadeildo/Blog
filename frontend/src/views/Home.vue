<script setup lang="ts">
import { getUser } from "@/lib/utils"
import { User } from "@/types/user"
import { onMounted, ref } from "vue"

const user = ref<User | null>(null)
onMounted(async () => {
  user.value = await getUser()
})
</script>

<template>
  <h1>Bem vindo {{ user?.username }}</h1>
</template>
