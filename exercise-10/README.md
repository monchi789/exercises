### 🪐 El Enunciado: "El Radar de Dimensiones"

Estás construyendo un sistema de navegación para la nave de Rick Sánchez. Él odia leer JSONs largos, así que quiere que le resumas la información de los planetas/ubicaciones que visita.

Tu misión:

Crear un endpoint que consulte la información de una ubicación específica en la API de Rick and Morty y devuelva un resumen táctico.

1. **Endpoint:** `GET /radar/{id_ubicacion}`
    
2. **API Externa:** `https://rickandmortyapi.com/api/location/{id_ubicacion}`
    
3. **Lógica:**
    
    - Tienes que usar `httpx` de forma asíncrona.
        
    - Si el ID no existe (404), tu API debe decir: "Ubicación desconocida, Morty".
        
4. El Filtro (Response Model):
    
    Rick solo quiere saber 4 cosas. Tu JSON de respuesta debe tener esta estructura exacta:
    
    JSON

``` json
{
    "nombre": "Earth (C-137)",       // El campo 'name' de la API
    "tipo": "Planet",                // El campo 'type' de la API
    "dimension": "Dimension C-137",  // El campo 'dimension' de la API
	"poblacion_actual": 27           // OJO: Aquí debes contar cuántos elementos
	                                 //hay en la lista 'residents'
}
```

Pista para la población:

La API te devuelve "residents": ["url1", "url2", "url3"...]. Tú no quieres las URLs, quieres el número total de residentes. (Usa len()).
