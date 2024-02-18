import { createRouter, createWebHistory } from "vue-router"

import { getUser } from "./lib/utils"
import { useSession } from "./stores/session"

const routes = [
  { path: "/login", component: () => import("./views/Login.vue") },
  {
    path: "/",
    component: () => import("./views/Home.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/logout",
    component: () => import("./views/LogOut.vue"),
    meta: { requiresAuth: true },
  },
  { path: "/:catchAll(.*)", redirect: "/" },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, _from, next) => {
  const session = useSession()
  session.setUser(await getUser())

  if (to.meta.requiresAuth) {
    if (!session.isLoggedIn) {
      next({ path: "/login" })
    } else {
      next()
    }
  } else {
    next()
  }
})
