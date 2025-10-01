# AgroGestor - API con FastAPI

Este proyecto implementa una API REST para el sistema de gestión agrícola AgroGestor, construida con FastAPI.
La principal finalidad es gestionar las operaciones CRUD para las entidades clave de la gestión agrícola, utilizando datos estáticos para simular la persistencia.

agrogestor/
│── main.py                 # Punto de entrada de la aplicación FastAPI
│
└── Models/                 # Definición de modelos de datos (clases Pydantic)
    │── usuario_Model.py
    │── Cultivo_Model.py
    │── MantenimientoCultivo_Model.py
    │── Insumo_Model.py
    |── categoriaInsumo_Model.py                 # opcional 
    |── DetalleInsumoUsado_Model.py              # opcional
    |── MonitoreoSuelo_Model.py                  # opcional      
    |── Rol_Model.py                             # opcional 
    |── SueloCultivo_Mode.py                     # opcional
    |── Suelo_Model.py                           # opcional
    |── UnidadMedida.py                          # opcional
│
└── Entity/                 # Lógica de las rutas (Implementación CRUD con datos estáticos)
    │── usuario.py
    │── cultivos.py
    │── MantenimientoCultivos.py
    │── gestionInsumos.py
    

1. **¿Cómo clonar el repositorio?**

    Python: En la terminal ->
        git clone https://github.com/TU_USUARIO/agrogestor.git
        cd agrogestor

2. **Crear un entorno virtual (Python)**

    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows (o .venv\Scripts\Activate.ps1 en PowerShell)

3. **Instalación de dependencias**

    pip install fastapi uvicorn pydantic

4. **Ejecutar el servidor**

    uvicorn main:app --reload
    # Alternativa: python -m uvicorn main:app --reload

5. **Acceso a la API**

    Documentación interactiva: http://127.0.0.1:8000/docs
    Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

# Endpoints principales (Versión CRUD Completa)

| Entidad | Método | Endpoint | Acción Principal |
| :--- | :---: | :--- | :--- |
| Usuarios | POST | /usuarios/ | Crear nuevo usuario |
| | GET | /usuarios/ | Listar / Obtener por ID (/{id}) |
| | PUT | /usuarios/{id} | Actualizar datos |
| | DELETE | /usuarios/{id} | Eliminar usuario |
| Cultivos | POST | /cultivos/ | Crear nuevo cultivo |
| | GET | /cultivos/ | Listar / Obtener por ID (/{id}) |
| | PUT | /cultivos/{id} | Actualizar datos |
| | DELETE | /cultivos/{id} | Eliminar cultivo |
| Mantenimientos | POST | /mantenimientos/ | Registrar nueva acción |
| | GET | /mantenimientos/ | Listar / Obtener por ID (/{id}) |
| | PUT | /mantenimientos/{id} | Actualizar registro |
| | DELETE | /mantenimientos/{id} | Eliminar registro |
| Insumos | POST | /insumos/ | Agregar nuevo insumo al inventario |
| | GET | /insumos/ | Listar / Obtener por ID (/{id}) |
| | PUT | /insumos/{id} | Actualizar stock/info |
| | DELETE | /insumos/{id} | Eliminar insumo |

# Tecnologías utilizadas
    Python 3.x
    FastAPI
    Pydantic (Validación de datos)
    Uvicorn (Servidor ASGI)

# Autores
  Proyecto desarrollado como caso de estudio en gestión agrícola.
  
  * Nombres: 
  Juan Flores
  Deyling Espinoza
  Luis Acosta
            
  * Github: @alexanderf100
  
  * Contacto: alexanderfmairena100@gmail.com
