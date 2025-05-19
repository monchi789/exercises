# Prueba Técnica: Sistema de Análisis de Datos de Lanzamientos Espaciales

## 🎯 Objetivo

Desarrollar una API REST que recopile y procese información sobre los últimos 200 lanzamientos espaciales combinando datos de fuentes públicas, y presente un análisis estadístico completo en una sola llamada.

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST** que integre y procese datos de múltiples fuentes.
2. **La API debe recopilar los últimos 200 lanzamientos espaciales** y presentar un análisis detallado.
3. La respuesta debe ser un **objeto JSON** con la siguiente estructura:
   - `launches`: Array con los 200 lanzamientos, cada uno conteniendo:
     - `mission_name` (Nombre de la misión)
     - `launch_date` (Fecha de lanzamiento)
     - `rocket_name` (Nombre del cohete)
     - `success` (Éxito o fracaso del lanzamiento)
     - `agency` (Agencia responsable)
     - `details` (Detalles de la misión)
   - `statistics`: Objeto con los siguientes análisis:
     - `success_rate` (Tasa de éxito de los lanzamientos)
     - `launches_by_year` (Distribución de lanzamientos por año)
     - `top_agencies` (Top 5 agencias con más lanzamientos)
     - `most_used_rockets` (Top 5 cohetes más utilizados)
4. La API debe responder en **menos de 5 segundos**.
5. Implementar un sistema de caché para optimizar las consultas repetidas.
6. La solución debe incluir manejo de errores apropiado y logging de las operaciones.

## 📚 APIs Disponibles para Resolver el Problema

Para esta prueba técnica, puedes utilizar las siguientes APIs gratuitas y que no requieren API Key:

1. **SpaceX API**
   - 🔗 [https://github.com/r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)
   - Endpoint principal: `https://api.spacexdata.com/v4/launches`
   - Esta API proporciona información detallada sobre los lanzamientos de SpaceX.

2. **The Space Devs - Launch Library 2**
   - 🔗 [https://thespacedevs.com/llapi](https://thespacedevs.com/llapi)
   - Endpoint principal: `https://ll.thespacedevs.com/2.2.0/launch/`
   - Esta API ofrece datos sobre lanzamientos de múltiples agencias espaciales.

## 💻 Consideraciones Técnicas

1. Deberás combinar los datos de ambas APIs para alcanzar los 200 lanzamientos requeridos.
2. Para mejorar el tiempo de respuesta, considera:
   - Implementar solicitudes asíncronas (Promise.all, async/await)
   - Utilizar un sistema de caché (Redis, memoria en aplicación, etc.)
   - Optimizar el procesamiento de datos
3. La solución debe incluir pruebas unitarias y de integración.
4. El código debe estar bien estructurado, siguiendo principios SOLID y patrones de diseño adecuados.

## 📝 Entregables

1. Repositorio de código en GitHub con instrucciones claras de instalación y ejecución.
2. Documentación de la API desarrollada (puedes usar Swagger, Postman o un README detallado).
3. Un breve documento explicando la arquitectura de la solución, decisiones técnicas y posibles mejoras.

## 🧪 Evaluación

Tu solución será evaluada según:
- Funcionalidad completa según los requisitos.
- Calidad y estructura del código.
- Rendimiento y optimización.
- Manejo de errores y casos borde.
- Documentación y claridad de la solución.
