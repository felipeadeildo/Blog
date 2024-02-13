import { createRouter, createWebHistory } from "vue-router"

import { getUser } from "./lib/utils"

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
