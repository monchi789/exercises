# 🧩 **Ejercicio Avanzado: Buscador Enriquecido de Universidades Internacionales**

### 📝 Enunciado

Una empresa educativa global desea un sistema que permita a los estudiantes buscar universidades en todo el mundo, pero además necesita enriquecer la información de cada universidad con los indicadores de desarrollo humano del país donde se ubica.

Tu tarea consiste en **crear una API RESTful que consuma e integre dos APIs públicas**:

1. La API de universidades del mundo.
2. La API de indicadores de desarrollo humano de cada país.

---

### 🎯 Objetivo

Desarrollar un endpoint `/enriched-universities` que permita buscar universidades por nombre o país, y que devuelva no solo los datos básicos de la universidad, sino también información sobre el contexto educativo y de desarrollo del país donde se encuentra.

---

### 🔗 APIs a usar

- **Universities API**:  
  https://universities.hipolabs.com/search

- **Human Development Index API** (a través de World Bank o alternativa):  
  Ejemplo: [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)  
  Indicador sugerido: `NY.GDP.PCAP.CD` (GDP per capita), `SE.TER.ENRR` (Gross tertiary enrollment ratio)

---

### ✅ Requisitos y Reglas de Negocio

1. Crear una **API RESTful** con un endpoint:  
   `/enriched-universities?country={pais}&name={nombre}`  
   Ambos parámetros son opcionales, pero al menos uno debe ser enviado.

2. La respuesta debe ser un **array en formato JSON**. Cada entrada debe tener la siguiente estructura:

```json
{
  "university": {
    "name": "Pontificia Universidad Católica del Perú",
    "country": "Peru",
    "web_pages": ["http://www.pucp.edu.pe"]
  },
  "country_data": {
    "gdp_per_capita": 7265.3,
    "tertiary_enrollment_rate": 57.1,
    "region": "Latin America & Caribbean"
  }
}
```

3. Si no se encuentra información del país en la API de desarrollo humano, debe incluir `"country_data": null`.

4. El servicio debe ser **capaz de devolver hasta 200 universidades** por solicitud. Implementar **paginación** (`page`, `limit`).

5. Implementar una **capa de caching (memoria temporal o disco)** para que los indicadores por país no se vuelvan a consultar en cada solicitud.

6. Tiempo de respuesta máximo: **3 segundos**.

7. Código limpio, con separación de capas y tratamiento adecuado de errores y estados HTTP.

---

### 💡 Bonus (opcional)

- Permitir ordenar los resultados por `gdp_per_capita` o `tertiary_enrollment_rate`.
- Exponer un endpoint separado que devuelva una **agrupación por región** con el número total de universidades por región y su promedio de GDP.

---

### 📦 Ejemplo de solicitud

```http
GET /enriched-universities?country=Colombia
```

### 📤 Ejemplo de respuesta (simplificado)

```json
[
  {
    "university": {
      "name": "Universidad Nacional de Colombia",
      "country": "Colombia",
      "web_pages": ["http://www.unal.edu.co/"]
    },
    "country_data": {
      "gdp_per_capita": 6830.2,
      "tertiary_enrollment_rate": 54.3,
      "region": "Latin America & Caribbean"
    }
  },
  ...
]
```

---
