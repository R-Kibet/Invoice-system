<template>
    <div class="page-clients">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Invoice {{ invoice.invoice_no }}</h1>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "Invoice",
    data () {
        return {
            invoice: {}
        }
    }, 
    async mounted () {
        await this,getInvoice()
    },
    methods: {
        getInvoice() {
            const invoiceID = this.$route.params.id

            axios
            .get(`/api/v1/invoices/${clientID}`)
            .then(response => {
                this.invoice = response.data
            })
            .catch(error => {
                console.log(JSON.stringify(error));
            })
        }
    }
}
</script>