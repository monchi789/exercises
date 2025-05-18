# 🌦️ Ejercicio de Práctica Backend – *Desafío API Global de Meteorología*

Tu misión es desarrollar un servicio de datos meteorológicos que consuma múltiples APIs públicas de clima y condiciones atmosféricas. El servicio deberá consolidar información de **10,000 ubicaciones geográficas** alrededor del mundo, procesarla y ofrecer una API unificada con predicciones enriquecidas.

---

## 🎯 Objetivo
Desarrollar una API REST que consuma múltiples APIs públicas meteorológicas y devuelva datos climáticos consolidados para **10,000 ubicaciones únicas** en una sola solicitud.

---

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST** utilizando cualquier framework backend (FastAPI, Express.js, Django, Flask, etc.).
2. La API debe hacer llamadas a por lo menos tres APIs meteorológicas públicas (OpenWeatherMap, WeatherAPI, OpenMeteo, etc.) para obtener y consolidar la información.
3. La respuesta debe devolver exactamente **10,000 objetos únicos**, cada uno representando datos meteorológicos de una ubicación geográfica específica.
4. Cada objeto meteorológico debe tener exclusivamente los siguientes campos:
   * `location_id` (identificador único generado)
   * `city` (nombre de la ciudad)
   * `country` (país de la ubicación)
   * `coordinates` (objeto con latitud y longitud)
   * `current_temp` (temperatura actual en grados Celsius)
   * `feels_like` (sensación térmica en grados Celsius)
   * `humidity` (porcentaje de humedad)
   * `wind_speed` (velocidad del viento en km/h)
   * `condition` (descripción del clima actual: soleado, nublado, etc.)
   * `forecast` (array con pronóstico para los próximos 3 días)
   * `last_updated` (timestamp de la última actualización)
   * `air_quality_index` (índice de calidad del aire, puede ser generado si no está disponible)
   * `uuid` (identificador único global para evitar duplicados)
5. Los datos deben ser **únicos** por `uuid` y combinación de `city` y `coordinates`.
6. La API debe responder en **menos de 5 segundos**.
7. La respuesta debe ser un **JSON array plano**.
8. Debe proporcionar endpoints para:
   * Obtener todos los datos (`/api/weather/all`)
   * Filtrar por país (`/api/weather/country/{country_code}`)
   * Filtrar por condición climática (`/api/weather/condition/{condition_type}`)

---

## 📚 Documentación de APIs Utilizadas

### 🔸 OpenWeatherMap API
🔗 [https://openweathermap.org/api](https://openweathermap.org/api)
* API Key gratuita: Permite hasta 1,000 llamadas por día
* Endpoint actual: `https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric`
* Pronóstico: `https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric`

### 🔸 WeatherAPI
🔗 [https://www.weatherapi.com/](https://www.weatherapi.com/)
* API Key gratuita: Permite hasta 1,000,000 llamadas por mes
* Endpoint actual: `https://api.weatherapi.com/v1/current.json?key={API_key}&q={city}`
* Pronóstico: `https://api.weatherapi.com/v1/forecast.json?key={API_key}&q={city}&days=3`

### 🔸 Open-Meteo API
🔗 [https://open-meteo.com/](https://open-meteo.com/)
* API completamente gratuita sin key
* Endpoint actual: `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m`

### 🔸 Air Quality Open Data Platform (opcional)
🔗 [https://aqicn.org/api/](https://aqicn.org/api/)
* API Key gratuita: Permite consultas limitadas
* Endpoint: `https://api.waqi.info/feed/{city}/?token={API_key}`

---

## 💡 Consideraciones Técnicas

* Implementa operaciones `async` y `parallel requests` para optimizar el tiempo de respuesta.
* Desarrolla un sistema de caché inteligente para minimizar llamadas redundantes a APIs externas.
* Utiliza un mecanismo de "fallback" para cuando una API no responda correctamente.
* Implementa un sistema de "rate limiting" para evitar bloqueos de las APIs externas.
* Utiliza una base de datos de geocodificación o API de geocodificación para obtener las coordenadas de las ciudades.
* Implementa un sistema de agregación para unificar datos de múltiples fuentes.
* Utiliza un mecanismo para controlar errores y reintentos cuando una API falle.
* Considera estrategias de distribución geográfica para obtener datos representativos de todo el mundo.

---

## 📦 Output Esperado (Ejemplo)

```json
[
  {
    "location_id": 1,
    "city": "Tokyo",
    "country": "Japan",
    "coordinates": {
      "lat": 35.6895,
      "lon": 139.6917
    },
    "current_temp": 22.5,
    "feels_like": 23.2,
    "humidity": 78,
    "wind_speed": 4.8,
    "condition": "cloudy",
    "forecast": [
      {
        "date": "2025-05-17",
        "min_temp": 19.4,
        "max_temp": 24.6,
        "condition": "rain"
      },
      {
        "date": "2025-05-18",
        "min_temp": 18.2,
        "max_temp": 25.1,
        "condition": "partly_cloudy"
      },
      {
        "date": "2025-05-19",
        "min_temp": 20.1,
        "max_temp": 27.3,
        "condition": "sunny"
      }
    ],
    "last_updated": "2025-05-16T14:32:15Z",
    "air_quality_index": 42,
    "uuid": "a54dc8ef-12b7-5c34-892e-f5e9b1c4fac8"
  },
  ...
]
```

---

## 🔍 Criterios de Evaluación

* **Arquitectura**: Diseño limpio, modular y escalable.
* **Rendimiento**: Tiempo de respuesta menor a 5 segundos.
* **Código limpio**: Legible, bien comentado y siguiendo mejores prácticas.
* **Manejo de errores**: Gestión adecuada de excepciones, reintentos y casos borde.
* **Escalabilidad**: Solución que podría manejar más ubicaciones y solicitudes concurrentes.
* **Optimización**: Uso eficiente de recursos y minimización de llamadas a APIs externas.
* **Integridad de datos**: Precisión y consistencia en la información meteorológica.

---

## 🚀 Bonus (Opcional)

* Implementar un sistema de caché distribuido con Redis o similar.
* Añadir documentación interactiva con Swagger/OpenAPI.
* Implementar tests unitarios, de integración y de carga.
* Añadir análisis estadístico del clima por región.
* Desarrollar un panel de administración para monitorear el estado de las APIs utilizadas.
* Implementar un sistema de alertas meteorológicas basado en umbrales.
* Contenerizar la aplicación con Docker y Docker Compose.
* Implementar CI/CD para despliegue automático.
* Añadir soporte para gráficos y visualizaciones de datos meteorológicos.