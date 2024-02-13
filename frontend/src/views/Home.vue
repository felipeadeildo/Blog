<script setup lang="ts">
import { agent } from "@/lib/utils"
import { onMounted, ref } from "vue"
import { Button } from "@/components/ui/button"
import {
  TooltipProvider,
  Tooltip,
  TooltipTrigger,
  TooltipContent,
} from "@/components/ui/tooltip"
import { Input } from "@/components/ui/input"
import { Dialog, DialogContent, DialogTitle, DialogFooter } from "@/components/ui/dialog"
import { Textarea } from "@/components/ui/textarea"
import { Plus } from "lucide-vue-next"
import { AxiosError } from "axios"
import { Post } from "@/types/post"
import PostCard from "@/components/PostCard.vue"
import { AlertCircle } from "lucide-vue-next"
import { Alert, AlertDescription } from "@/components/ui/alert"

const posts = ref<Post[]>([])

onMounted(async () => {
  const res = await agent.get("/post")
  posts.value = res.data.posts as Post[]
})

const openDialog = ref(false)
const isLoading = ref(false)
const post = ref<Omit<Post, "user" | "id">>({
  title: "",
  content: "",
  banner: "",
})

const handleAddPost = async () => {
  isLoading.value = false
  try {
    const res = await agent.post("/post", {
      title: post.value.title,
      content: post.value.content,
      banner: post.value.banner,
    })
    if (res.status === 200) {
      openDialog.value = false
      posts.value.push(res.data as Post)
    } else throw new Error()
  } catch (err: unknown) {
    if (err instanceof Error) console.error(err.message)
    else if (err instanceof AxiosError) console.error(err.response?.data.message)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="text-3xl font-bold mb-4 text-center my-3">Posts</div>

  <Alert variant="warning" v-if="posts.length === 0">
    <AlertCircle class="w-4 h-4" />
    <AlertDescription>No posts found</AlertDescription>
  </Alert>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 justify-center">
    <PostCard v-for="post in posts" :key="post.id" :post="post" />
  </div>

  <Dialog :open="openDialog" @update:open="openDialog = $event">
    <DialogContent class="w-full max-w-xl">
      <DialogTitle>Add new Post</DialogTitle>
      <div class="grid gap-4 py-4">
        <Input placeholder="Title" v-model="post.title" />
        <Textarea placeholder="Content" v-model="post.content" />
        <Input placeholder="Banner URL" v-model="post.banner" />
      </div>
      <DialogFooter class="gap-2">
        <Button @click="openDialog = false" variant="destructive"> Cancel </Button>
        <Button @click="handleAddPost()"> Create </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>

  <TooltipProvider :delay-duration="100">
    <Tooltip>
      <TooltipTrigger as-child>
        <Button
          @click="openDialog = true"
          variant="default"
          size="icon"
          class="absolute right-7 bottom-5"
        >
          <Plus />
        </Button>
      </TooltipTrigger>
      <TooltipContent>
        <p>Add new Post</p>
      </TooltipContent>
    </Tooltip>
  </TooltipProvider>
</template>
