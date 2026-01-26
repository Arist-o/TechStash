<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isLogin = ref(true);

const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const errorMessage = ref('');

const submitButtonText = computed(() => isLogin.value ? 'Увійти' : 'Створити акаунт');
const toggleLinkText = computed(() => isLogin.value ? 'Немає акаунту? Створіть новий' : 'Вже є акаунт? Увійдіть');

const toggleAuthMode = () => {
  isLogin.value = !isLogin.value;
  email.value = '';
  password.value = '';
  confirmPassword.value = '';
  errorMessage.value = '';
};

const handleSubmit = async () => {
  errorMessage.value = '';

  // Перевірка співпадіння паролів лише при реєстрації
  if (!isLogin.value && password.value !== confirmPassword.value) {
    errorMessage.value = 'Паролі не співпадають!';
    return;
  }

  // Визначаємо правильний шлях: login або register
  const endpoint = isLogin.value ? 'login' : 'register';

  try {
    const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    });

    const data = await response.json();

    if (response.ok) {
      if (isLogin.value) {
        // Логіка входу
        localStorage.setItem('token', data.access_token);
        console.log('Успішний вхід!');
        router.push('/maincontent');
      } else {
        // Логіка після реєстрації
        alert('Акаунт створено! Тепер увійдіть у систему.');
        isLogin.value = true; // Перемикаємо на вхід
        confirmPassword.value = '';
      }
    } else {
      // Виведення помилки від FastAPI (наприклад, "Користувач вже існує")
      errorMessage.value = data.detail || 'Помилка авторизації';
    }
  } catch (error) {
    errorMessage.value = 'Сервер бекенду не відповідає. Перевір консоль Python.';
  }
}
</script>

<template>
  <div class="container-fluid d-flex justify-content-center align-items-center min-vh-100 bg-light-gray">
    <div class="card shadow border-0 p-4" style="max-width: 420px; width: 100%;">
      
      <div class="text-center mb-3">
        <div class="logo-icon d-inline-flex align-items-center justify-content-center">
          <span>&lt;/&gt;</span>
        </div>
      </div>

      <div class="text-center mb-4">
        <h1 class="h4 fw-bold text-dark">
          {{ isLogin ? 'Ласкаво просимо до' : 'Реєстрація в' }} 
          <span class="text-primary-custom">TechStash</span>
        </h1>
        <p class="text-muted small">Керуйте документацією для розробників</p>
      </div>

      <div v-if="errorMessage" class="alert alert-danger small p-2 text-center fade-in">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label for="email" class="form-label fw-semibold text-secondary small">Email</label>
          <input
              type="email"
              class="form-control"
              id="email"
              v-model="email"
              placeholder="test@example.com"
              required
          >
        </div>

        <div class="mb-3">
          <label for="password" class="form-label fw-semibold text-secondary small">Пароль</label>
          <input
              type="password"
              class="form-control"
              id="password"
              v-model="password"
              placeholder="••••••••"
              required
          >
        </div>

        <div v-if="!isLogin" class="mb-3 fade-in">
          <label for="confirmPassword" class="form-label fw-semibold text-secondary small">Підтвердіть пароль</label>
          <input
              type="password"
              class="form-control"
              id="confirmPassword"
              v-model="confirmPassword"
              placeholder="••••••••"
              required
          >
        </div>

        <button type="submit" class="btn btn-teal w-100 py-2 fw-bold text-white mt-2">
          {{ submitButtonText }}
        </button>
      </form>

      <div class="text-center mt-3">
        <a href="#" @click.prevent="toggleAuthMode" class="text-decoration-none text-muted small hover-link">
          {{ toggleLinkText }}
        </a>
      </div>

      <div v-if="isLogin" class="alert alert-secondary mt-4 d-flex align-items-start small mb-0" role="alert">
        <span class="me-2 fs-5">💡</span>
        <div>
          <p class="mb-1">Для тесту:</p>
          <div class="d-flex flex-column">
            <span>Email: <strong>test@example.com</strong></span>
            <span>Пароль: <strong>password123</strong></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Стилі залишаються без змін, вони у вас чудові */
.bg-light-gray { background-color: #f8f9fa; }
.btn-teal { background-color: #00b894; border: none; transition: background-color 0.2s ease-in-out; }
.btn-teal:hover { background-color: #00a182; color: white; }
.logo-icon { width: 50px; height: 50px; background-color: #0ea5e9; color: white; border-radius: 8px; font-family: monospace; font-size: 1.2rem; font-weight: bold; }
.text-primary-custom { color: #0ea5e9; }
.form-control:focus { border-color: #0ea5e9; box-shadow: 0 0 0 0.25rem rgba(14, 165, 233, 0.15); }
.hover-link:hover { color: #0ea5e9 !important; }
.fade-in { animation: fadeIn 0.3s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
</style>