<script setup lang="ts">
import { Post } from "@/types/post"
import { defineProps } from "vue"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

const props = defineProps<{ post: Post }>()
const { post } = props
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>{{ post.title }}</CardTitle>
      <CardDescription>
        <img :src="post.banner" alt="Post Banner" />
      </CardDescription>
    </CardHeader>
    <CardContent>
      <p>{{ post.content }}</p>
    </CardContent>
    <CardFooter class="justify-end">
      <p>{{ `${post.user.username} (${post.user.email})` }}</p>
    </CardFooter>
  </Card>
</template>
