<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <!-- Notification -->
      <transition name="notification">
        <div v-if="showNotification" :class="['notification', notificationType]">
          {{ notificationMessage }}
        </div>
      </transition>

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
        <div class="field">
          <label>Теги</label>
          <input 
            v-model="tagsInput" 
            type="text" 
            placeholder="Введіть теги через кому (наприклад: react, javascript, frontend)" 
          />
          <div v-if="parsedTags.length > 0" class="tags-preview">
            <span v-for="tag in parsedTags" :key="tag" class="tag-chip">
              #{{ tag }}
            </span>
          </div>
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
import { ref, computed } from 'vue';

const emit = defineEmits(['close', 'card-added']);

// URL API - змініть на свій якщо потрібно
const API_URL = 'http://127.0.0.1:8000/api/cards';

const newCard = ref({
  title: '',
  description: '',
  link: '',
  tags: []
});

const tagsInput = ref('');

// Обчислюємо масив тегів з введеного тексту
const parsedTags = computed(() => {
  if (!tagsInput.value.trim()) return [];
  
  return tagsInput.value
    .split(',')
    .map(tag => tag.trim().toLowerCase().replace(/^#/, ''))
    .filter(tag => tag.length > 0);
});

const showNotification = ref(false);
const notificationMessage = ref('');
const notificationType = ref('success'); // 'success' or 'error'

function displayNotification(message, type = 'success') {
  notificationMessage.value = message;
  notificationType.value = type;
  showNotification.value = true;
  
  setTimeout(() => {
    showNotification.value = false;
  }, 3000);
}

async function saveCard() {
  if (!newCard.value.title || !newCard.value.link) {
    displayNotification('Назва та URL обов\'язкові!', 'error');
    return;
  }

  try {
    console.log('Відправка картки:', {
      title: newCard.value.title,
      description: newCard.value.description || '',
      link: newCard.value.link,
      tags: parsedTags.value
    });
    
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        title: newCard.value.title,
        description: newCard.value.description || '',
        link: newCard.value.link,
        tags: parsedTags.value
      })
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      console.error('Помилка від сервера:', errorData);
      
      // Показуємо детальну помилку якщо є
      const errorMessage = errorData.detail || errorData.message || 'Помилка збереження';
      displayNotification(`✗ ${errorMessage}`, 'error');
      return;
    }

    const savedCard = await response.json();
    console.log('Картка збережена успішно:', savedCard);
    
    // Показуємо повідомлення про успіх
    displayNotification('✓ Картка успішно збережена!', 'success');
    
    // Передаємо створену картку в батьківський компонент
    emit('card-added', savedCard);
    
    // Потім закриваємо модалку (з невеликою затримкою)
    setTimeout(() => {
      emit('close');
    }, 1500);
    
  } catch (error) {
    console.error('Помилка:', error);
    displayNotification('✗ Не вдалося підключитися до сервера', 'error');
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
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  position: relative;
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

.tags-preview {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.tag-chip {
  display: inline-block;
  padding: 4px 12px;
  background: #e0f2fe;
  color: #0369a1;
  border-radius: 16px;
  font-size: 0.875rem;
  font-weight: 500;
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

/* Notification styles */
.notification {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 500;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1001;
}

.notification.success {
  background: #10b981;
  color: white;
}

.notification.error {
  background: #ef4444;
  color: white;
}

/* Notification animation */
.notification-enter-active,
.notification-leave-active {
  transition: all 0.3s ease;
}

.notification-enter-from {
  opacity: 0;
  transform: translateX(-50%) translateY(-20px);
}

.notification-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-20px);
}
</style>