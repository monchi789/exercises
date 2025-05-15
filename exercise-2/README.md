# 🧪 Ejercicio de Práctica Backend – *Desafío Pokémon Trainer API*

Tenemos acceso a una API pública que nos brinda información de entrenadores Pokémon alrededor del mundo. Tu misión será desarrollar una API propia que consuma esa API externa y devuelva **exactamente 15,000 entrenadores únicos**, estructurados y optimizados.

---

## 🎯 Objetivo

Desarrollar una API propia que consuma la **PokéAPI** y devuelva **15,000 entrenadores Pokémon únicos** en una sola solicitud.

---

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST** utilizando cualquier framework backend (por ejemplo, FastAPI, Express.js, Django, etc.).

2. La API debe hacer llamadas a la [PokéAPI](https://pokeapi.co) y estructurar la información.

3. La respuesta debe devolver exactamente **15,000 objetos únicos**, cada uno representando un entrenador ficticio.

4. Cada objeto de entrenador debe tener exclusivamente los siguientes campos:

   * `trainer_id` (identificador único generado)
   * `name` (nombre del entrenador, puedes generarlo usando un generador como [randomuser.me](https://randomuser.me))
   * `region` (nombre de la región Pokémon, obtenido desde PokéAPI)
   * `starter_pokemon` (nombre de un Pokémon inicial aleatorio)
   * `age` (entre 10 y 99, generado aleatoriamente)
   * `email` (generado a partir del nombre + dominio aleatorio)
   * `uuid` (identificador único global para evitar duplicados)

5. Los datos deben ser **únicos** por `uuid`.

6. La API debe responder en **menos de 3 segundos**.

7. La respuesta debe ser un **JSON array plano**.

---

## 📚 Documentación de APIs Utilizadas

### 🔸 PokéAPI

🔗 [https://pokeapi.co/docs/v2](https://pokeapi.co/docs/v2)

Puedes obtener:

* Regiones: `https://pokeapi.co/api/v2/region`
* Pokémon: `https://pokeapi.co/api/v2/pokemon?limit=151` (por ejemplo, para starter Pokémon)

### 🔸 Random User API (opcional para nombres)

🔗 [https://randomuser.me/api/](https://randomuser.me/documentation)

---

## 💡 Consideraciones Técnicas

* Puedes usar `async` y `parallel requests` para acelerar la carga de datos.
* Debes almacenar en memoria solo lo necesario.
* Puedes cachear previamente información fija (como la lista de Pokémon o regiones).
* Asegúrate de **limitar los cuellos de botella** al usar APIs externas.
* Utiliza una estrategia eficiente para evitar usuarios duplicados.

---

## 📦 Output Esperado (Ejemplo)

```json
[
  {
    "trainer_id": 1,
    "name": "Ash Ketchum",
    "region": "kanto",
    "starter_pokemon": "pikachu",
    "age": 12,
    "email": "ash.ketchum@pokemail.com",
    "uuid": "a95dcbef-1ef9-4a23-872a-c3e8f0c3fdd7"
  },
  ...
]
```

---
