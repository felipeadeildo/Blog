import { User } from "./user"

export type Post = {
  id: number
  title: string
  content: string
  banner: string
  user: User
}
