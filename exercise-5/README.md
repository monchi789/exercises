# Prueba Técnica: API de Consolidación de Usuarios

## 🎯 Objetivo
Desarrollar una API REST que consuma datos de la API pública de [JSONPlaceholder](https://jsonplaceholder.typicode.com/) y [Random Data API](https://random-data-api.com/), combinando y enriqueciendo los datos para devolver exactamente 8,000 usuarios únicos en una sola llamada.

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST** con un endpoint principal `/api/users`.
2. **La API debe devolver 8,000 usuarios no repetidos** en una sola llamada.
3. La respuesta debe ser un **array en formato JSON** con los siguientes campos únicamente:
   - `id` (Identificador único no repetido)
   - `name` (Nombre completo)
   - `username` (Nombre de usuario)
   - `email` (Correo electrónico)
   - `phone` (Número telefónico)
   - `company` (Nombre de la empresa)
   - `subscription_tier` (Nivel de suscripción: "basic", "premium", "enterprise")
   - `last_login` (Fecha del último acceso)
4. La API debe responder en **menos de 5 segundos**.
5. Implementar un mecanismo de caché para optimizar el rendimiento.
6. Incluir manejo de errores adecuado.

> **Nota:** Todos los requisitos y reglas de negocio deben cumplirse para que la solución sea válida.

## 📚 Documentación de las APIs a utilizar

1. **JSONPlaceholder API**
   - Documentación: [https://jsonplaceholder.typicode.com/guide/](https://jsonplaceholder.typicode.com/guide/)
   - Endpoint de usuarios: [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)

2. **Random Data API**
   - Documentación: [https://random-data-api.com/documentation](https://random-data-api.com/documentation)
   - Endpoint de usuarios: [https://random-data-api.com/api/v2/users](https://random-data-api.com/api/v2/users)

## 📋 Entregables Esperados

1. Código fuente de la API (incluyendo package.json con dependencias).
2. Documentación de la API con instrucciones de instalación y uso.
3. Tests automatizados que validen los requisitos.
4. Pruebas de rendimiento que demuestren que la API cumple con el tiempo de respuesta requerido.

## 💡 Consideraciones Técnicas

- Utilizar Node.js y Express para el desarrollo de la API.
- Implementar un manejo efectivo de promesas y peticiones concurrentes.
- La solución debe ser escalable y mantener un buen rendimiento.
- El código debe seguir buenas prácticas y estar bien organizado.
- Se valorará positivamente el uso de patrones de diseño adecuados.

## 🧪 Criterios de Evaluación

1. **Funcionalidad (40%)**: La API cumple con todos los requisitos establecidos.
2. **Rendimiento (25%)**: La API responde en el tiempo establecido y hace uso efectivo de recursos.
3. **Código (20%)**: Calidad del código, estructura, legibilidad y mantenibilidad.
4. **Pruebas (15%)**: Cobertura y calidad de las pruebas automatizadas.

## ⏱️ Tiempo Estimado

Se espera que esta prueba técnica se complete en aproximadamente 4-6 horas, dependiendo de la experiencia del candidato.

## 📬 Forma de Entrega

- Repositorio Git (GitHub, GitLab, Bitbucket) con el código fuente.
- README.md con instrucciones detalladas para instalar, ejecutar y probar la API.
- Si es posible, desplegar la API en alguna plataforma gratuita (Heroku, Vercel, etc.) y proporcionar la URL.

¡Buena suerte!