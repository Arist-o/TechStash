<script setup>
import { ref } from "vue";
import AddCardModal from "./AddCardModal.vue";

const showModal = ref(false);

const openModal = () => {
  console.log("СПРАЦЮВАЛО: Кнопка натиснута!"); 
  showModal.value = true; // Змінюємо стан на true
};
</script>

<template>
  <header class="navbar">
    <div class="logo">
      <span class="icon">&lt;/&gt;</span>
      <span class="title">TechStash</span>
    </div>

    <div class="actions">
      <button class="add-btn" @click="openModal">
        + Додати картку
      </button>

      <AddCardModal v-if="showModal" @close="showModal = false" />
      
      <div class="avatar">👤</div>
    </div>
  </header>
</template>

<style scoped>
.navbar { height: 64px; display: flex; align-items: center; padding: 0 24px; border-bottom: 1px solid #e5e7eb; background: #fff; }
.actions { margin-left: auto; display: flex; align-items: center; gap: 16px; position: relative; z-index: 10; }
.add-btn { background: #2563eb; color: white; border: none; padding: 8px 14px; border-radius: 8px; cursor: pointer; }
</style>