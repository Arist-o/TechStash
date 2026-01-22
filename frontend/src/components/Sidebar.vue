<script setup>
import { ref } from "vue";

const activeCategory = ref("Documentation");
const activeTags = ref(["backend", "containers", "css"]);
</script>


<template>
  <aside class="sidebar">
    <h4>Категорії</h4>

    <ul class="menu">
      <li
          v-for="c in ['All','Documentation','Tutorials','Tools','Resources']"
          :key="c"
          :class="{ active: activeCategory === c }"
          @click="activeCategory = c"
      >
        {{ c }}
      </li>
    </ul>

    <h4>Фільтр за тегами</h4>

    <ul class="tags">
      <li
          v-for="t in ['backend','containers','css','database','devops','docker','frontend','javascript','postgresql','typescript']"
          :key="t"
          :class="{ active: activeTags.includes(t) }"
          @click="
    activeTags.includes(t)
      ? activeTags = activeTags.filter(x => x !== t)
      : activeTags.push(t)
  "
      >
        # {{ t }}
      </li>

    </ul>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 260px;
  padding: 20px;
  border-right: 1px solid #e5e7eb;
  background: #fff;
}

h4 {
  margin-bottom: 12px;
  font-size: 14px;
  font-weight: 600;
}

.menu li,
.tags li {
  padding: 6px 10px;
  border-radius: 6px;
  transition: 0.2s;
  cursor: default;
}

/* hover */
.menu li:hover,
.tags li:hover {
  background: #f3f4f6;
}

/* active category */
.menu li.active {
  background: #e0edff;
  color: #2563eb;
  font-weight: 600;
}

/* active tag */
.tags li.active {
  background: #d1fae5;
  color: #059669;
}
</style>
