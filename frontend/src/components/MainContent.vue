<template>
  <main class="container-fluid py-4">
    <div class="row g-4">
      <CardItem 
        v-for="card in cards" 
        :key="card.id" 
        :card="card"
        @delete-card="deleteCard"
      />
    </div>
  </main>
</template>

<script>
import CardItem from './CardItem.vue';

export default {
  components: { CardItem },
  data() {
    return {
      cards: [] 
    }
  },
  methods: {
    async fetchCards() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/cards');
        this.cards = await response.json();
        console.log('Завантажено карток:', this.cards.length);
      } catch (error) {
        console.error('Помилка завантаження карток:', error);
      }
    },
    
    async deleteCard(cardId) {
      try {
        await fetch(`http://127.0.0.1:8000/api/cards/${cardId}`, {
          method: 'DELETE'
        });
        this.cards = this.cards.filter(card => card.id !== cardId);
      } catch (error) {
        console.error('Помилка видалення:', error);
      }
    }
  },
  
  mounted() {
    this.fetchCards();
  }
}
</script>