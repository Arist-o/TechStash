<template>
  <div class="col-12 col-sm-6 col-lg-4">
    <div class="card h-100 shadow-sm rounded-4 border-0 position-relative">
      
      <!-- Кнопка видалення -->
      <button 
        @click="deleteCard" 
        class="btn-delete position-absolute top-0 end-0 m-2"
        title="Видалити картку"
      >
        ✕
      </button>

      <div class="card-body d-flex flex-column p-4">
        
        <h5 class="card-title fw-bold mb-2">{{ card.title }}</h5>
        
        <p class="card-text text-muted small mb-3">
          {{ card.description }}
        </p>
        
        <div class="mb-3 d-flex flex-wrap gap-1">
          <span v-for="tag in card.tags" :key="tag" class="badge bg-light text-dark fw-normal border">
            #{{ tag }}
          </span>
        </div>

        <div class="mt-auto">
          <a :href="card.link" target="_blank" class="btn btn-link p-0 text-decoration-none text-primary fw-medium">
            Відкрити посилання <i class="bi bi-box-arrow-up-right ms-1"></i>
          </a>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardItem',
  props: {
    card: {
      type: Object,
      required: true
    }
  },
  methods: {
    deleteCard() {
      if (confirm(`Видалити картку "${this.card.title}"?`)) {
        this.$emit('delete-card', this.card.id);
      }
    }
  }
}
</script>

<style scoped>
.card {
  transition: transform 0.2s ease-in-out;
}
.card:hover {
  transform: translateY(-5px);
}

.btn-delete {
  background: rgba(239, 68, 68, 0.1);
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #ef4444;
  font-size: 1.2rem;
  opacity: 0;
  transition: all 0.2s;
  z-index: 10;
}

.card:hover .btn-delete {
  opacity: 1;
}

.btn-delete:hover {
  background: #ef4444;
  color: white;
}
</style>