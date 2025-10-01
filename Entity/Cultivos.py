from fastapi import APIRouter, HTTPException, status
from typing import List
from Models.Cultivo_Model import Cultivo, CultivoCreate, CultivoUpdate

# Lista estática para simular la base de datos
db_cultivos: List[Cultivo] = []
next_id = 1

router = APIRouter(
    prefix="/cultivos",
    tags=["Cultivos"]
)

# === GET (Leer todos) ===
@router.get("/", response_model=List[Cultivo])
async def get_all_cultivos():
    return db_cultivos

# === POST (Crear) ===
@router.post("/", response_model=Cultivo, status_code=status.HTTP_201_CREATED)
async def create_cultivo(cultivo_data: CultivoCreate):
    global next_id
    new_cultivo = Cultivo(id=next_id, **cultivo_data.dict())
    db_cultivos.append(new_cultivo)
    next_id += 1
    return new_cultivo

# (Aquí se agregarían las rutas PUT y DELETE similares a las de usuario.py)