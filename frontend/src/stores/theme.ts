import { defineStore } from "pinia"

export const useTheme = defineStore("theme", {
  state: () => {
    const isDark = localStorage.getItem("dark") === "true"
    if (isDark) document.documentElement.classList.add("dark")
    return {
      dark: localStorage.getItem("dark") === "true",
    }
  },
  actions: {
    toggle() {
      this.dark = !this.dark
      localStorage.setItem("dark", String(this.dark))
      document.documentElement.classList.toggle("dark")
    },
  },
  getters: {
    isDark: (state) => {
      return state.dark
    },
  },
})
