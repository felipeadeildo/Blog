import { User } from "@/types/user"
import axios from "axios"
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
// import { camelize, getCurrentInstance, toHandlerKey } from "vue"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const agent = axios.create({
  baseURL: "http://localhost:8866/api",
  withCredentials: true,
})

export const getUser = async () => {
  try {
    const res = await agent.get("/me")
    return res.data as User
  } catch {
    return null
  }
}
