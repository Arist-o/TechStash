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
}


</script>

<template>
  <div class="login-container">
    <div class="login-card">

      <div class="logo-wrapper">
        <div class="logo-icon"><span>&lt;/&gt;</span></div>
      </div>

      <h1 class="title">Ласкаво просимо до <span class="brand-name">TechStash</span></h1>
      <p class="subtitle">Керуйте документацією для розробників</p>

      <form @submit.prevent="handleSubmit" class="login-form">
        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" v-model="email" type="email" placeholder="test@example.com" required />
        </div>

        <div class="form-group">
          <label for="password">Пароль</label>
          <input id="password" v-model="password" type="password" placeholder="••••••••" required />
        </div>

        <div v-if="!isLogin" class="form-group fade-in">
          <label for="confirmPassword">Підтвердіть пароль</label>
          <input
              id="confirmPassword"
              v-model="confirmPassword"
              type="password"
              placeholder="••••••••"
              required
          />
        </div>

        <button type="submit" class="submit-btn">
          {{ submitButtonText }}
        </button>
      </form>

      <div class="card-footer">
        <a href="#" @click.prevent="toggleAuthMode" class="create-account-link">
          {{ toggleLinkText }}
        </a>
      </div>

      <div class="info-box">
        <span class="bulb-icon">💡</span>
        <div class="info-text">
          <p>Для тесту:</p>
          <p>Email: <strong>test@example.com</strong></p>
          <p>Пароль: <strong>password123</strong></p>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fa;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.login-card {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  width: 100%;
  max-width: 420px;
  text-align: center;
}

.logo-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.logo-icon {
  width: 50px;
  height: 50px;
  background-color: #0ea5e9;
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
  font-family: monospace;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.brand-name {
  color: #0ea5e9;
}

.subtitle {
  color: #6b7280;
  font-size: 0.95rem;
  margin-bottom: 2rem;
}

.login-form {
  text-align: left;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.95rem;
  outline: none;
  transition: border-color 0.2s;
  box-sizing: border-box;
}

.form-group input:focus {
  border-color: #0ea5e9;
  box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
}

.submit-btn {
  width: 100%;
  padding: 0.875rem;
  background-color: #00b894;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-top: 0.5rem;
}

.submit-btn:hover {
  background-color: #00a182;
}

.card-footer {
  margin-top: 1.5rem;
  font-size: 0.9rem;
}

.create-account-link {
  color: #6b7280;
  text-decoration: none;
  transition: color 0.2s;
}

.create-account-link:hover {
  color: #0ea5e9;
}

.info-box {
  margin-top: 2rem;
  background-color: #eef2f6;
  padding: 1rem;
  border-radius: 8px;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  text-align: left;
  font-size: 0.8rem;
  color: #4b5563;
}

.bulb-icon {
  font-size: 1.2rem;
}

.info-text p {
  margin: 0.2rem 0;
}

.info-text strong {
  color: #1f2937;
}
.fade-in {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>