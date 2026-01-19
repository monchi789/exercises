## 📺 PROBLEMA 5 — _El Archivo de Series_

Estás creando un sistema para una plataforma de streaming.  
El gerente solo quiere saber si una serie es larga o corta, no todos los episodios.

### 🎯 Tu misión

Consultar una serie y devolver un resumen ejecutivo.

1. **Endpoint:**  
    `GET /series/{id}`
    
2. **API Externa:**
    
    `https://api.tvmaze.com/shows/{id}`
    
3. **Lógica:**
    
    - Usa `httpx` async.
        
    - Si la serie no existe, responde:  
        **"Serie inexistente"**
        
4. **Filtro (Response Model):**
    

```json
{   
	"nombre": "Under the Dome",
	"idioma": "English",   
	"estado": "Ended",   
	"total_episodios": 39 
}
```

📌 **Pista:**  
Debes consultar el endpoint de episodios y usar `len()`.