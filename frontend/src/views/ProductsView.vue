<template>
  <div>
    <h2>Products</h2>
    <DataTable :service-name="'products'" />
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import DataTable from '/src/components/DataTable.vue'

export default defineComponent({
  name: 'ProductsView',
  components: {
    DataTable
  }
})
</script>