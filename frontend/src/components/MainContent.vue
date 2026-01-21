<template>
  <main class="container-fluid py-4">

    <div class="d-flex align-items-center mb-4">
      <h4 class="mb-0 me-3">All Cards</h4>
      <small class="text-muted">{{ cards.length }} cards found</small>
    </div>

    <div class="row g-4">
      <div
          v-for="card in cards"
          :key="card.id"
          class="col-12 col-sm-6 col-lg-4"
      >
        <div class="card h-100 shadow-sm rounded-4">
          <div class="card-body d-flex flex-column">

            <h5 class="card-title">{{ card.title }}</h5>
            <p class="card-text text-muted small">
              {{ card.description }}
            </p>

          </div>
        </div>
      </div>
    </div>

  </main>
</template>

<script setup>
const cards = [
  {
    id: 1,
    title: "React Documentation",
    description:
        "The official React documentation with comprehensive guides, API reference, and best practices for building user interfaces.",
    tags: ["react", "javascript", "frontend"],
    link: "https://react.dev"
  },
  {
    id: 2,
    title: "Docker Guide",
    description:
        "Complete Docker documentation including container management, deployment strategies, and Docker Compose tutorials.",
    tags: ["docker", "devops", "containers"],
    link: "https://docs.docker.com"
  },
  {
    id: 3,
    title: "Python Official Docs",
    description:
        "Python programming language documentation with tutorials, library reference, and language specifications.",
    tags: ["python", "backend", "programming"],
    link: "https://docs.python.org"
  }
]
</script>