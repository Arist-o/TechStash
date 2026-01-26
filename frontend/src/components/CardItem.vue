<template>
  <div class="col-12 col-sm-6 col-lg-4">
    <div class="card h-100 shadow-sm rounded-4 border-0">
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
    // Приймаємо об'єкт картки від батьківського компонента (MainContent)
    card: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.card {
  transition: transform 0.2s ease-in-out;
}
.card:hover {
  transform: translateY(-5px); /* Ефект підйому при наведенні */
}
</style>