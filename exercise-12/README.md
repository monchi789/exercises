## 🛰️ PROBLEMA 4 — _El Rastreador Orbital_

Estás desarrollando un panel de control para una estación espacial.  
Los ingenieros solo quieren saber dónde está el satélite ahora mismo.

### 🎯 Tu misión

Crear un endpoint que consulte la posición de un satélite y devuelva un resumen orbital.

1. **Endpoint:**  
    `GET /orbit/{satellite_id}`
    
2. **API Externa:**
    
    `https://api.wheretheiss.at/v1/satellites/{satellite_id}`
    
3. **Lógica:**
    
    - Usa `httpx` async.
        
    - Si el satélite no existe, responde:  
        **"Objeto fuera de seguimiento"**
        
4. **Filtro (Response Model):**
    

```json
{   
	"nombre": "iss",   
	"latitud": -45.23,   
	"longitud": 120.88,   
	"altitud_km": 421.7 
}
```

📌 _Solo renombrar campos._