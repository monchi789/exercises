# 🧪 Ejercicio de Práctica Backend – *Desafío Biblioteca Mundial API*

Tenemos acceso a varias APIs públicas que nos brindan información sobre libros y autores de todo el mundo. Tu misión será desarrollar una API propia que consuma esas APIs externas y devuelva **exactamente 15,000 libros únicos**, estructurados y optimizados.

---

## 🎯 Objetivo
Desarrollar una API propia que consuma las **APIs públicas de libros** y devuelva **15,000 libros únicos** en una sola solicitud.

---

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST** utilizando cualquier framework backend (por ejemplo, FastAPI, Express.js, Django, etc.).
2. La API debe hacer llamadas a las APIs de OpenLibrary y Google Books para obtener y estructurar la información.
3. La respuesta debe devolver exactamente **15,000 objetos únicos**, cada uno representando un libro con datos enriquecidos.
4. Cada objeto de libro debe tener exclusivamente los siguientes campos:
   * `book_id` (identificador único generado)
   * `title` (título del libro)
   * `author` (nombre del autor)
   * `published_year` (año de publicación)
   * `category` (categoría o género del libro)
   * `rating` (calificación promedio generada aleatoriamente entre 1.0 y 5.0)
   * `availability` (booleano aleatorio para indicar disponibilidad)
   * `pages` (número de páginas, si está disponible o generado aleatoriamente)
   * `isbn` (número ISBN del libro si está disponible o generado)
   * `uuid` (identificador único global para evitar duplicados)
5. Los datos deben ser **únicos** por `uuid` y combinación de `title` y `author`.
6. La API debe responder en **menos de 3 segundos**.
7. La respuesta debe ser un **JSON array plano**.

---

## 📚 Documentación de APIs Utilizadas

### 🔸 Open Library API
🔗 [https://openlibrary.org/developers/api](https://openlibrary.org/developers/api)
Puedes obtener:
* Búsqueda de libros: `https://openlibrary.org/search.json?q=subject:fiction&limit=100`
* Información de autor: `https://openlibrary.org/authors/{author_key}.json`

### 🔸 Google Books API
🔗 [https://developers.google.com/books/docs/v1/using](https://developers.google.com/books/docs/v1/using)
* Búsqueda de libros: `https://www.googleapis.com/books/v1/volumes?q=subject:adventure&maxResults=40`

### 🔸 The New York Times Books API (opcional)
🔗 [https://developer.nytimes.com/docs/books-product/1/overview](https://developer.nytimes.com/docs/books-product/1/overview)
* Listas de bestsellers: `https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json`

---

## 💡 Consideraciones Técnicas

* Puedes usar `async` y `parallel requests` para acelerar la carga de datos.
* Debes almacenar en memoria solo lo necesario.
* Implementa un sistema de caché para evitar llamadas redundantes a las APIs externas.
* Asegúrate de **limitar los cuellos de botella** al usar APIs externas.
* Utiliza mecanismos de paginación para recuperar suficientes datos de las APIs.
* Implementa un sistema de "rate limiting" para evitar bloqueos de las APIs externas.
* Utiliza una estrategia eficiente para evitar libros duplicados.

---

## 📦 Output Esperado (Ejemplo)

```json
[
  {
    "book_id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "category": "fiction",
    "rating": 4.5,
    "availability": true,
    "pages": 180,
    "isbn": "9780743273565",
    "uuid": "b86dfcef-2ef9-5b34-973a-d4e9f1c4fdd8"
  },
  ...
]
```

---

## 🔍 Criterios de Evaluación

* **Arquitectura**: Diseño limpio, modular y eficiente.
* **Rendimiento**: Tiempo de respuesta menor a 3 segundos.
* **Código limpio**: Legible, bien comentado y siguiendo mejores prácticas.
* **Manejo de errores**: Gestión adecuada de excepciones y casos borde.
* **Escalabilidad**: Solución que podría escalar a más datos y solicitudes.
* **Optimización**: Uso eficiente de recursos y minimización de llamadas a APIs externas.

---

## 🚀 Bonus (Opcional)

* Implementar un sistema de caché persistente.
* Añadir documentación con Swagger o similar.
* Implementar tests unitarios y de integración.
* Añadir filtros en la API (por categoría, año, etc.).
* Utilizar Docker para contenerizar la aplicación.
* Implementar un sistema de monitoreo y logging.