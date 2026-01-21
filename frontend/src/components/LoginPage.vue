<script setup>
import { ref,computed } from 'vue';

const isLogin = ref(true);

const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const submitButtonText = computed(() => isLogin.value ? 'Увійти' : 'Створити акаунт');
const toggleLinkText = computed(() => isLogin.value ? 'Немає акаунту? Створіть новий' : 'Вже є акаунт? Увійдіть');

const toggleAuthMode = () => {
  isLogin.value = !isLogin.value;
  password.value = '';
  confirmPassword.value = '';
};
const handleSubmit = () => {
  if (!isLogin.value && password.value !== confirmPassword.value) {
    alert('Паролі не співпадають!');
    return;
  }
  const payload = {
    email: email.value,
    password: password.value,
    ...(isLogin.value ? {} : { confirmPassword: confirmPassword.value })
  };
  console.log('Дані форми:', payload);
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
        <h1 class="h4 fw-bold text-dark">Ласкаво просимо до <span class="text-primary-custom">TechStash</span></h1>
        <p class="text-muted small">Керуйте документацією для розробників</p>
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

      <div class="alert alert-secondary mt-4 d-flex align-items-start small mb-0" role="alert">
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
  /* 1. Фон сторінки */
.bg-light-gray {
  background-color: #f8f9fa;
}

/* 2. Кастомний колір для кнопки (Виправляє "зниклу" кнопку) */
.btn-teal {
  background-color: #00b894; /* Зелений колір як на макеті */
  border: none;
  transition: background-color 0.2s ease-in-out;
}

.btn-teal:hover {
  background-color: #00a182; /* Темніший відтінок при наведенні */
  color: white;
}

/* 3. Логотип */
.logo-icon {
  width: 50px;
  height: 50px;
  background-color: #0ea5e9;
  color: white;
  border-radius: 8px;
  font-family: monospace;
  font-size: 1.2rem;
  font-weight: bold;
}

/* 4. Колір бренду (TechStash) */
.text-primary-custom {
  color: #0ea5e9;
}

/* 5. Перезапис стилів Bootstrap для інпутів (щоб рамка була блакитною, а не синьою) */
.form-control:focus {
  border-color: #0ea5e9;
  box-shadow: 0 0 0 0.25rem rgba(14, 165, 233, 0.15);
}

/* 6. Посилання "Створити акаунт" */
.hover-link:hover {
  color: #0ea5e9 !important; /* !important потрібен, щоб перебити клас text-muted */
}

/* 7. Анімація появи поля (fade-in) */
.fade-in {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>