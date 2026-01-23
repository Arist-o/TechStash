<script setup>
import { ref } from "vue";
import AddCardModal from "./AddCardModal.vue";


const showModal = ref(false);
</script>


<template>
  <header class="navbar">
    <div class="logo">
      <span class="icon">&lt;/&gt;</span>
      <span class="title">TechStash</span>
    </div>

    <input
        type="text"
        placeholder="Пошук карток документації..."
        class="search"
    />

    <div class="actions">
      <button class="add-btn" @click="showModal = true">
        + Додати картку
      </button>
      <AddCardModal v-if="showModal" @close="showModal = false" />
      <div class="avatar">👤</div>
    </div>
    <div class="logout" title="Вийти">
      <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="30"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
      >
        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
        <polyline points="16 17 21 12 16 7"/>
        <line x1="21" y1="12" x2="9" y2="12"/>
      </svg>
    </div>
  </header>
</template>

<style scoped>
.navbar {
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 24px;
  border-bottom: 1px solid #e5e7eb;
  background: #fff;
  position: relative;
}

.logo {
  display: flex;
  align-items: center;
  font-weight: 700;
  font-size: 18px;
  margin-right: 24px;
}

.icon {
  color: #2563eb;
  margin-right: 6px;
}

.search {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 520px;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid #d1d5db;
}

.actions {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 16px;
}

.add-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  cursor: pointer;
}

.avatar {
  width: 36px;
  height: 36px;
  background: #f3f4f6;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 10px;
}
.logout {
  cursor: pointer;
  color: #6b7280;
  transition: 0.2s;
}

.logout:hover {
  color: #ef4444;
}

</style>
