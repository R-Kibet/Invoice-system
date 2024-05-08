<template>
    <div class="page-add-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add client</h1>
            </div>
             
            <div class="column is-6">
                <div class="field">
                    <label>Name</label>
                    <div class="control"> 
                        <input type="text" name="name" class="input" v-model="client.name">
                    </div>

                </div>

            
                <div class="field">
                    <label>Email</label>
                    <div class="control"> 
                        <input type="email" name="email" class="input" v-model="client.email">
                    </div>

                </div>

                <div class="field">
                    <label>Org</label>
                    <div class="control"> 
                        <input type="text" name="org_id" class="input" v-model="client.org_id">
                    </div>

                </div>

                <div class="field">
                    <label>Address 1</label>
                    <div class="control"> 
                        <input type="text" name="address" class="input" v-model="client.address">
                    </div>

                </div>


                <div class="field">
                    <label>Address 2</label>
                    <div class="control"> 
                        <input type="text" name="add2" class="input" v-model="client.add2">
                    </div>

                </div>

            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Contact</label>
                    <div class="control"> 
                        <input type="text" name="contact" class="input" v-model="client.contact">
                    </div>

                </div>

                <div class="field">
                    <label>Contact Ref</label>
                    <div class="control"> 
                        <input type="text" name="contact_ref" class="input" v-model="client.contact_ref">
                    </div>

                </div>
                <div class="field">
                    <label>Zipcode</label>
                    <div class="control"> 
                        <input type="text" name="zipcd" class="input" v-model="client.zipcd">
                    </div>

                </div>

                <div class="field">
                    <label>Country</label>
                    <div class="control"> 
                        <input type="text" name="country" class="input" v-model="client.country">
                    </div>

                </div>


                <div class="field">
                    <label>Place</label>
                    <div class="control"> 
                        <input type="text" name="place" class="input" v-model="client.place">
                    </div>

                </div>



            </div>


            <div class="column is-12"  >
                <div class="field" >
                    <div class="control"> 
                        <button  class="button is-success" @click="submitForm">Submit</button>
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
    name: 'AddClient',
    data () {
        return {
            client: {}
        }
    },
    methods : {
        submitForm() {
            axios
                .post("/api/v1/clients/", this.client)
                .then(response => {
                    toast ({
                        message: "updated",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover:true,
                        duration: 20000,
                        position:'bottom-right'
                    })
                    this.$router.push('/dashboard/clients')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>