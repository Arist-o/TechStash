<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Нова картка</h2>
        <button class="close-btn" @click="$emit('close')">✕</button>
      </div>

      <div class="modal-body">
        <div class="field">
          <label>Назва</label>
          <input type="text" placeholder="Назва..." />
        </div>
        <div class="field">
          <label>URL</label>
          <input type="text" placeholder="URL..." />
        </div>
        <div class="field">
          <label>Опис</label>
          <textarea placeholder="Опис..."></textarea>
        </div>
      </div>

      <div class="modal-actions">
        <button class="cancel-btn" @click="$emit('close')">Закрити</button>
        <button class="save-btn">Зберегти</button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['close']);
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000; /* Вікно поверх усього */
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 12px;
  width: 450px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-body {
  display: flex;
  flex-direction: column;
  gap: 15px;
  text-align: left;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

input, textarea {
  padding: 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  width: 100%;
  box-sizing: border-box; /* Щоб написи не плили */
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 25px;
}

.save-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
}
</style>