<template>
  <div class="app-container">
    <header>
      <h1>ERP System</h1>
    </header>
    <nav>
      <router-link to="/products">Products</router-link>
      <router-link to="/orders">Orders</router-link>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.app-container {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

nav {
  margin: 20px 0;
}

nav a {
  margin-right: 15px;
  text-decoration: none;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
  font-weight: bold;
}
</style>