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
          <input 
            v-model="newCard.title" 
            type="text" 
            placeholder="Назва..." 
          />
        </div>
        <div class="field">
          <label>URL</label>
          <input 
            v-model="newCard.link" 
            type="text" 
            placeholder="URL..." 
          />
        </div>
        <div class="field">
          <label>Опис</label>
          <textarea 
            v-model="newCard.description" 
            placeholder="Опис..."
          ></textarea>
        </div>
      </div>

      <div class="modal-actions">
        <button class="cancel-btn" @click="$emit('close')">Закрити</button>
        <button class="save-btn" @click="saveCard">Зберегти</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['close', 'card-added']);

const newCard = ref({
  title: '',
  description: '',
  link: '',
  tags: []
});

async function saveCard() {
  if (!newCard.value.title || !newCard.value.link) {
    alert('Назва та URL обов\'язкові!');
    return;
  }

  try {
    console.log('Відправка картки:', newCard.value);
    
    const response = await fetch('http://127.0.0.1:8000/api/cards', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        title: newCard.value.title,
        description: newCard.value.description || '',
        link: newCard.value.link,
        tags: []
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Помилка від сервера:', errorData);
      throw new Error('Помилка збереження');
    }

    const savedCard = await response.json();
    console.log('Картка збережена успішно:', savedCard);
    
    // Спочатку викликаємо card-added (щоб оновити список)
    emit('card-added');
    
    // Потім закриваємо модалку (з невеликою затримкою)
    setTimeout(() => {
      emit('close');
    }, 100);
    
  } catch (error) {
    console.error('Помилка:', error);
    // Прибираємо alert, щоб не блокувати виконання
    console.error('Не вдалося зберегти картку');
  }
}
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
  z-index: 1000;
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

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6b7280;
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

.field label {
  font-weight: 500;
  color: #374151;
}

input, textarea {
  padding: 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  width: 100%;
  box-sizing: border-box;
  font-family: inherit;
}

textarea {
  min-height: 100px;
  resize: vertical;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 25px;
}

.cancel-btn {
  background: white;
  border: 1px solid #d1d5db;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
}

.save-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
}

.save-btn:hover {
  background: #1d4ed8;
}

.cancel-btn:hover {
  background: #f3f4f6;
}
</style>