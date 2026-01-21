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

            <div class="mb-3">
              <span
                  v-for="tag in card.tags"
                  :key="tag"
                  class="badge bg-light text-dark me-2 mb-2"
              >
                #{{ tag }}
              </span>
            </div>

            <a
                :href="card.link"
                target="_blank"
                class="mt-auto text-decoration-none text-primary fw-medium"
            >
              Відкрити посилання ↗
            </a>

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
  },
  {
    id: 4,
    title: "TypeScript Handbook",
    description:
        "Learn TypeScript with the official handbook covering type system, advanced types, and best practices.",
    tags: ["typescript", "javascript", "frontend"],
    link: "https://www.typescriptlang.org/docs/"
  },
  {
    id: 5,
    title: "Tailwind CSS",
    description:
        "Utility-first CSS framework documentation with examples and customization guides for modern web design.",
    tags: ["css", "tailwind", "frontend"],
    link: "https://tailwindcss.com/docs"
  },
  {
    id: 6,
    title: "PostgreSQL Manual",
    description:
        "Comprehensive PostgreSQL database documentation including SQL syntax, administration, and performance tuning.",
    tags: ["postgresql", "database", "backend"],
    link: "https://www.postgresql.org/docs/"
  }
]
</script>