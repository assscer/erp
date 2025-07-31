<template>
  <div>
    <h2>Orders</h2>
    <DataTable :service-name="'orders'" />
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import DataTable from '/src/components/DataTable.vue'

export default defineComponent({
  name: 'OrdersView',
  components: {
    DataTable
  }
})
</script>