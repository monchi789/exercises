## 🌎 PROBLEMA 3 — _El Traductor de Naciones_

Estás construyendo un sistema de consulta rápida para la ONU.  
Los diplomáticos odian leer respuestas enormes en JSON, así que quieren solo lo esencial de cada país.

### 🎯 Tu misión

Crear un endpoint que consulte la información de un país y devuelva un resumen diplomático.

1. **Endpoint:**  
    `GET /nations/{codigo}`
    
2. **API Externa:**
    
    `https://restcountries.com/v3.1/alpha/{codigo}`
    
3. **Lógica:**
    
    - Debes usar `httpx` de forma **asíncrona**.
        
    - Si el código no existe (404), responde:  
        **"Nación no reconocida"**
        
4. **Filtro (Response Model):**
    

```json
{   
	"nombre": "Peru",   
	"capital": "Lima",   
	"region": "Americas",   
	"poblacion": 32971846 
}
```

📌 _Solo mapear campos. Nada de cálculos._