<template>
    <div class="page-account">
        <h1 class="title">Account</h1>

        <div class="buttons">

            <router-link to="/dashboard/account/edit-team" class="button is-light">Edit team</router-link>

            <button @click="logout()" class="button is-danger">Log out</button>

        </div>

    </div>
    
</template>

<script>
import axios from "axios"

export default {
    name: 'Account',
    methods: {
        logout() {
            axios
                .post("/api/v1/token/logout/")
                .then(response => {
                    axios.defaults.headers.common['Authorization'] = ''

                    localStorage.removeItem('token')

                    this.$store.commit('removeToken')

                    this.$router.push('/')
                })
        }
    },
}
</script>
