import { createRouter, createWebHistory } from "vue-router"

import { getUser } from "./lib/utils"
import HomeVue from "./views/Home.vue"
import LoginVue from "./views/Login.vue"

const routes = [
  { path: "/login", component: LoginVue },
  { path: "/", component: HomeVue, meta: { requiresAuth: true } },
  { path: "/:catchAll(.*)", redirect: "/" },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, _from, next) => {
  const user = await getUser()
  if (to.meta.requiresAuth) {
    if (!user) {
      next({ path: "/login" })
    } else {
      next()
    }
  } else {
    next()
  }
})
