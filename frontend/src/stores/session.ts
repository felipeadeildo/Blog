import { agent } from "@/lib/utils"
import { User } from "@/types/user"
import { defineStore } from "pinia"

export const useSession = defineStore("session", {
  state: () => ({
    user: null as User | null,
  }),
  actions: {
    setUser(user: User | null) {
      this.user = user
    },

    async login(username: string, password: string) {
      const res = await agent.post("/login", {
        username,
        password,
      })
      if (res.status === 200) {
        this.setUser(res.data.user as User)
      }
    },

    async logout() {
      const res = await agent.get("/logout")
      if (res.status === 200) {
        this.user = null
      }
    },
  },
  getters: {
    isLoggedIn: (state) => {
      return state.user !== null
    },
  },
})
