# Prueba Técnica: Desarrollo de API REST para Consumo de Usuarios

Tenemos un CRM el cual tiene una API ya desarrollada que nos brinda usuarios a demanda con una estructura JSON ya definida.  
El objetivo de la prueba consiste en desarrollar nuestra propia API para devolver **15,000 usuarios** en una sola llamada del API del CRM.

---

## 🎯 Objetivo

Desarrollar una API propia que consuma la API del CRM y devuelva exactamente 15,000 usuarios únicos en una sola solicitud.

---

## ✅ Requisitos y Reglas de Negocio

1. **Construir una API tipo REST**.
2. **La API debe devolver 15,000 usuarios no repetidos** en una sola llamada.
3. La respuesta debe ser un **array en formato JSON** con los siguientes campos únicamente:
   - `gender` (Género)
   - `first_name` (Primer nombre)
   - `last_name` (Primer apellido)
   - `email` (Correo electrónico)
   - `uuid` (Identificador único no repetido)
   - `age` (Edad)
4. La API debe responder en **menos de 3 segundos**.

> **Nota:** Todos los requisitos y reglas de negocio deben cumplirse para que la solución sea válida.

---

## 📚 Documentación de la API del CRM

Puedes consultar la documentación oficial del CRM en el siguiente enlace:

🔗 [https://randomuser.me/documentation](https://randomuser.me/documentation)
