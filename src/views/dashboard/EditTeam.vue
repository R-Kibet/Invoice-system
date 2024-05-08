<template>
   <div class="page-edit-team">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit Team</h1>
            </div>

            <div class="column is-12">
                <div class="field">
                    <label>Name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.name">
                    </div>

                </div>

                <div class="field">
                    <label>Org. number</label>
                    <div class="control">
                        <input type="text" class="input" v-model="team.org_id">
                    </div>

                </div>

                <div class="field">
                    <label>Invoice </label>
                    <div class="control">
                        <input type="number" class="input" v-model="team.invoice_1">
                    </div>

                </div>

                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm" >Save</button>
                    </div>

                </div>

            </div>

        </div>
    </div>
</template>

<script>

import axios from 'axios';
import { toast } from "bulma-toast"

export default {
    name: "EditTeam",
    data() {
        return {
            team: {}
        }
    },
    async mounted() {
        await this.getOrCreateTea()
    },
    methods: {
        getOrCreateTea() {
            axios
                .get('/api/v1/teams/')
                .then(response => {
                    toast ({
                        message: "updated",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover:true,
                        duration: 20000,
                        position:'bottom-right'
                    })
                    this.team = response.data[0]
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                })
        },
        submitForm(){
            axios
                .patch(`/api/v1/teams/${this.team.id}/`, this.team)
                .then(response => {
                    this.$router.push('/dashboard/account')
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                })
        }
        
    }
}
</script>