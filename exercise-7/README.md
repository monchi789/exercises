# 🧩 **Ejercicio Avanzado: Buscador de Países con Enriquecimiento vía Web Scraping**

### 📝 Enunciado

Una empresa dedicada a servicios de geolocalización necesita construir un sistema que permita buscar países por nombre y obtener información estructurada de cada uno, incluyendo su código ISO, código Alpha-3 e identificador numérico.

Sin embargo, no existe una API oficial gratuita para este fin, por lo que se requiere **usar técnicas de web scraping** para extraer estos datos desde una fuente web confiable.

Tu tarea es crear una **API RESTful que haga scraping del sitio [iban.com](https://www.iban.com/country-codes)** para extraer la información relevante y construir un sistema de búsqueda funcional.

---

### 🎯 Objetivo

Desarrollar un endpoint `/countries` que permita buscar países por nombre parcial y devuelva datos enriquecidos obtenidos vía scraping en tiempo real o desde una caché local.

---

### 🔗 Fuente de Datos

* **IBAN.com Country Codes**:
  [https://www.iban.com/country-codes](https://www.iban.com/country-codes)
  Esta tabla contiene:

  * Country
  * Alpha-2 code
  * Alpha-3 code
  * Numeric code

---

### ✅ Requisitos y Reglas de Negocio

1. Crear una **API RESTful** con un endpoint:
   `/countries?name={nombre}`
   El parámetro `name` es obligatorio.

2. El sistema debe buscar **coincidencias parciales e insensibles a mayúsculas** (por ejemplo, "peRu" debe coincidir con "Peru").

3. La respuesta debe ser un **array JSON**, cada entrada con esta estructura:

```json
{
  "country": "Peru",
  "alpha2": "PE",
  "alpha3": "PER",
  "numeric": "604"
}
```

4. Implementar una **capa de caching en memoria o en disco**:

   * El scraping solo debe realizarse **una vez por sesión o cada cierto tiempo configurable (e.g. 24 horas)**.
   * Las búsquedas deben realizarse sobre la versión cacheada.

5. Debe manejarse adecuadamente errores como:

   * Caída del sitio fuente.
   * Problemas al parsear el HTML.
   * Filtros sin resultados.

6. El sistema debe responder en un máximo de **3 segundos**.

---

### 💡 Bonus (opcional)

* Permitir buscar por código (Alpha-2, Alpha-3 o código numérico).
* Exponer un endpoint adicional `/regions` que agrupe los países por región (esto puede simularse internamente, usando una lógica manual simple).

---

### 📦 Ejemplo de solicitud

```http
GET /countries?name=land
```

### 📤 Ejemplo de respuesta

```json
[
  {
    "country": "Finland",
    "alpha2": "FI",
    "alpha3": "FIN",
    "numeric": "246"
  },
  {
    "country": "Iceland",
    "alpha2": "IS",
    "alpha3": "ISL",
    "numeric": "352"
  },
  {
    "country": "Ireland",
    "alpha2": "IE",
    "alpha3": "IRL",
    "numeric": "372"
  }
]
```

---

### 🔧 Pistas Técnicas

* Usa `BeautifulSoup` o `lxml` en Python, o `cheerio` si usas Node.js.
* Para el caché, puedes usar una variable global, archivo JSON, Redis o `pickle`.
* Realiza el scraping una única vez, salvo que el cache expire.

---