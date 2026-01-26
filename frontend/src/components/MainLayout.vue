<template>
  <div class="layout-wrapper">
    <Navigationbar />

    <div class="main-body">
      <Sidebar />
      
      <main class="content-view">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import Navigationbar from "./Navigationbar.vue";
import Sidebar from "./Sidebar.vue";
</script>

<style scoped>
.layout-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main-body {
  display: flex;
  flex: 1;
  overflow: hidden; /* Щоб не було зайвих скролів */
}

.content-view {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background-color: #f9fafb; /* Твій світло-сірий фон */
}
</style>