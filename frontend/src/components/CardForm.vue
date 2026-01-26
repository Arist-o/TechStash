<template>
  <main class="container-fluid py-4">
    <!-- ВИДАЛЕНО: <CardForm @card-added="addNewCardToList" /> -->

    <div class="row g-4">
      <CardItem 
        v-for="card in cards" 
        :key="card.id" 
        :card="card" 
      />
    </div>
  </main>
</template>

<script>
import CardItem from './CardItem.vue';
// ВИДАЛЕНО: import CardForm from './CardForm.vue';

export default {
  components: { 
    CardItem 
    // ВИДАЛЕНО: CardForm 
  },
  data() {
    return {
      cards: [] 
    }
  },
  methods: {
    // Цей метод можна видалити, якщо тепер картки завантажуються з бекенду
    addNewCardToList(newCard) {
      this.cards.push(newCard);
    }
  },
  // Додай завантаження карток з API при монтуванні:
  async mounted() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/cards');
      this.cards = await response.json();
    } catch (error) {
      console.error('Помилка завантаження карток:', error);
    }
  }
}
</script>