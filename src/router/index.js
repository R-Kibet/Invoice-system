import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from "../views/SignUp.vue"
import Dashboard from "../views/dashboard/Dashboard.vue"
import Login from "../views/Login.vue"
import Account from "../views/dashboard/Account.vue"
import Clients from "../views/dashboard/Clients.vue"
import Client from "../views/dashboard/Client.vue"
import AddClient from "../views/dashboard/AddClient.vue"
import UpdateClient from "../views/dashboard/UpdateClient.vue"
import EditTeam from "../views/dashboard/EditTeam.vue"
import Invoices from "../views/dashboard/Invoices.vue"
import Invoice from "../views/dashboard/Invoice.vue"



import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },

  {
    path: '/sign-up',
    name: 'SignUP',
    component:SignUp 
  },

  {
    path: '/log-in',
    name: 'Login',
    component:Login 
  },

  {
    path: '/dashboard',
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/account',
    name: "Account",
    component: Account,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/account/edit-team',
    name: "EditTeam",
    component: EditTeam,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/clients',
    name: "Clients",
    component: Clients,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/Invoices',
    name: "Invoices",
    component: Invoices,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/Invoices/:id',
    name: "Invoice",
    component: Invoice,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/clients/:id',
    name: "Client",
    component: Client,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/clients/add',
    name: "AddClient",
    component: AddClient,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/dashboard/clients/:id/update',
    name: "UpdateClient",
    component: UpdateClient,
    meta: {
      requireLogin: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from , next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
