<template>
  <div class="layout">
    <Navigationbar />

    <div class="content">
      <Sidebar />
      <router-view />
    </div>
  </div>
</template>

<script setup>
import Navigationbar from "./Navigationbar.vue";
import Sidebar from "./Sidebar.vue";
</script>

<style scoped>
.layout {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1;
  display: flex;
  background: #f9fafb;
}
</style>
