<template>
  <main class="container-fluid py-4">
    <CardForm @card-added="addNewCardToList" />

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
import CardForm from './CardForm.vue';

export default {
  components: { CardItem, CardForm },
  data() {
    return {
      cards: [] 
    }
  },
  methods: {
    addNewCardToList(newCard) {
      this.cards.push(newCard);
    }
  }
}
</script>