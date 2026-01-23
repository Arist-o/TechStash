<template>
  <div class="overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="header">
        <h3>Додати нову картку</h3>
        <button class="close" @click="$emit('close')">✕</button>
      </div>

      <div class="form">
        <label>Назва *</label>
        <input placeholder="React Documentation" />

        <label>URL *</label>
        <input placeholder="https://react.dev" />

        <label>Опис *</label>
        <textarea placeholder="Офіційна документація React..." />

        <label>Теги</label>
        <div class="tags-input">
          <input placeholder="react, javascript, frontend" />
          <button>Додати</button>
        </div>
      </div>

      <div class="actions">
        <button class="cancel" @click="$emit('close')">Скасувати</button>
        <button class="create">Створити картку</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  width: 520px;
  background: white;
  border-radius: 12px;
  padding: 24px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 16px;
}

input, textarea {
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #d1d5db;
}

textarea {
  resize: none;
  height: 80px;
}

.tags-input {
  display: flex;
  gap: 8px;
}

.tags-input button {
  padding: 0 12px;
}

.actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 20px;
}

.cancel {
  padding: 10px 16px;
}

.create {
  padding: 10px 16px;
  background: #0ea5e9;
  color: white;
  border: none;
  border-radius: 8px;
}
</style>
