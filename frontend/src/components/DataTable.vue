<template>
  <div class="table-container">
    <table class="data-table" v-if="tableData.length">
      <thead>
        <tr>
          <th v-for="col in columns" :key="col.field">{{ col.label }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in tableData" :key="item.id">
          <td v-for="col in columns" :key="col.field">
            {{ formatCell(item[col.field], col.field) }}
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else class="no-data">No data available</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  props: ['serviceName'],
  data() {
    return {
      tableData: [],
      columns: []
    }
  },
  async mounted() {
    try {
      const response = await axios.get(`http://localhost:8000/api/${this.serviceName}/`)
      this.tableData = response.data

      // Настраиваемые колонки по типу данных
      if (this.serviceName === 'products') {
        this.columns = [
          { field: 'id', label: 'ID' },
          { field: 'name', label: 'Название' },
          { field: 'description', label: 'Описание' },
          { field: 'price', label: 'Цена' },
          { field: 'quantity', label: 'Кол-во' },
          { field: 'created_at', label: 'Создано' },
          { field: 'updated_at', label: 'Обновлено' }
        ]
      } else if (this.serviceName === 'orders') {
        this.columns = [
          { field: 'id', label: 'ID' },
          { field: 'customer_name', label: 'Клиент' },
          { field: 'customer_email', label: 'Email' },
          { field: 'total_amount', label: 'Сумма' },
          { field: 'status', label: 'Статус' },
          { field: 'created_at', label: 'Создано' }
        ]
      } else {
        // fallback на все ключи
        if (this.tableData.length) {
          this.columns = Object.keys(this.tableData[0]).map(key => ({
            field: key,
            label: key.charAt(0).toUpperCase() + key.slice(1)
          }))
        }
      }
    } catch (err) {
      console.error("Ошибка при загрузке данных:", err)
    }
  },
  methods: {
    formatCell(value, field) {
      if (field.includes('date') || field.includes('created_at') || field.includes('updated_at')) {
        return new Date(value).toLocaleString('ru-RU')
      }
      if (field === 'price' || field === 'total_amount') {
        return Number(value).toLocaleString('ru-RU', {
          style: 'currency',
          currency: 'KZT'
        })
      }
      return value
    }
  }
}
</script>

<style scoped>
.table-container {
  max-width: 1200px;
  margin: 2rem auto;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.data-table th,
.data-table td {
  border: 1px solid #ccc;
  padding: 0.6rem 1rem;
  text-align: left;
}

.data-table th {
  background-color: #f5f5f5;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.85rem;
}

.no-data {
  text-align: center;
  margin-top: 2rem;
  color: #999;
}
</style>
