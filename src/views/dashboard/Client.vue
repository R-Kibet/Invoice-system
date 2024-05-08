<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title"> {{ client.name }}</h1>

                <router-link :to="{name: 'UpdateClient', params: { id: client.id }}" class="button is-light mt-4">Update</router-link>

            </div>

            <div class="column is-12">
                <h2 class="subtitle"> Client Details</h2>

                <p><strong> {{ client.name }}</strong></p>

                <p v-if="client.address">{{ client.address }}</p>
                <p v-if="client.add2">{{ client.add2 }}</p>
                <p v-if="client.zipcd">{{ client.zipcd }}</p>
                <p v-if="client.country">{{ client.country }}</p>


            </div>

        </div>
    </div>
    
</template>

<script>
import axios from 'axios';

export default {
    name: 'Client',
    data () {
        return {
            client: {}
        }
    },
    mounted() {
        this.getClient()
    },
    methods : {
        getClient () {
          const clientID = this.$route.params.id

          axios
            .get(`/api/v1/clients/${clientID}`)
            .then(response => {
                this.client = response.data
            })
            .catch(error => {
                console.log(JSON.stringify(error));
            })
        }

    }
}
</script>