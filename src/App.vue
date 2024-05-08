<template>
  <div id="collapse">
    <nav class="navbar is-dark">
        <div class='navbar-brand'>
          <router-link to='/' class='navbar-item'><strong>Invoice</strong></router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if='$store.state.isAuthenticated'>
                    <router-link to='/dashboard' class='navbar-item'>Dashboard</router-link>
                    <router-link to='/dashboard/clients' class='navbar-item'>Clients</router-link>
                    <router-link to='/dashboard/invoices' class='navbar-item'>Invoices</router-link>

                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/dashboard/account" class="button is-light">My Account</router-link>
                        </div>
                    </div>
                
                
                </template>

                <template v-else>
                     <router-link to='/' class='navbar-item'>Home</router-link>

                     <div class="navbar-item">
                        <div class="buttons">
                            <router-link to='/sign-up' class="button is-success"><strong>Sign Up</strong></router-link>
                            <router-link to='/log-in' class="button is-light">Log in</router-link>
                        </div>
                     </div>
                </template> 
            </div>
        </div>
    </nav>

    <section class="section">
        <router-view/>
    </section>

    <footer class='footer'>
        <p class='has-text-centered'>Copyrights (c) 2024</p>
    </footer>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'App',
    beforeCreate() {
        this.$store.commit('initializeStore')

        const token = this.$store.state.token

        if (token) {
            axios.defaults.headers.common['Authorization'] = "Token " + token
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }
    }
}

</script>
<style lang="scss">
@import '/home/hasla/Desktop/Gchic/node_modules/bulma'
</style>
