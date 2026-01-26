<template>
  <div class="col-12 col-sm-6 col-lg-4 mb-4">
    <div class="card h-100 shadow-sm rounded-4 border-primary" style="border-style: dashed;">
      <div class="card-body d-flex flex-column">
        <input v-model="newCard.title" class="form-control mb-2 border-0 fw-bold" placeholder="Назва...">
        <textarea v-model="newCard.description" class="form-control mb-2 border-0 small" placeholder="Опис..."></textarea>
        <input v-model="newCard.link" class="form-control mb-3 border-0 text-primary small" placeholder="URL посилання...">
        <button @click="saveCard" class="btn btn-primary btn-sm mt-auto">Зберегти</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() { return { newCard: { title: '', description: '', link: '', tags: [] } } },
  methods: {
    async saveCard() {
      await axios.post('http://127.0.0.1:8000/api/cards', this.newCard);
      this.$emit('card-added');
      this.newCard = { title: '', description: '', link: '', tags: [] };
    }
  }
}
</script>