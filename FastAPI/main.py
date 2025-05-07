#Interfaz de Programación de Aplicaciones (API) para compartir recursos
from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Inicializar variable con todas las características de una API Rest.
app = FastAPI()

#Definimos el modelo.
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    description: Optional[str] = None
    nivel: str
    duracion: int
    
#Simlar Base de Datos.
cursos_db = []


#CRUD: Read (lectura) GETALL: Leer todos los cursos que haya en la DB
@app.get("/cursos/", response_model=List[Curso])
def obtener_crusos():
    return cursos_db

#CRUD: Create (escribir) POST: agregaremos un nuevo recurso a nuestra DB
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4()) #Usamos UUID para generar un id único e irrepetible.
    cursos_db.append(curso)
    return curso

#CRUD: Read (Lectura individual) GET: Leeremos el curso que coincida con el ID que coincidamos
@app.get("/crusos/{curso_id}", response_model=Curso)
def obtener_cruso(curso_id: str):
    curso =  next((curso for curso in cursos_db if curso.id == curso_id), None) #Con next() tomamos la primer coincidencia.
    if curso is None:
        raise HTTPException(status_code = 404, detail = "Curso no encontrado.")
    return curso

#CRUD: Update (Actualizar/Modificar) PUT: Modificaremos un recurso que coincida con el ID que mandemos
@app.put("/crusos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso =  next((curso for curso in cursos_db if curso.id == curso_id), None) #Con next() tomamos la primer coincidencia.
    if curso is None:
        raise HTTPException(status_code = 404, detail = "Curso no encontrado.")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso) #Buscamos el índice exacto donde está nuestro curso en la lista (db).
    cursos_db[index] = curso_actualizado
    return curso_actualizado
    
#CRUD: Delete (Eliminar/Borrar) DELETE: Eliminaremos un recurso que coincida con el ID que mandemos
@app.delete("/crusos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str, curso_actualizado: Curso):
    curso =  next((curso for curso in cursos_db if curso.id == curso_id), None) #Con next() tomamos la primer coincidencia.
    if curso is None:
        raise HTTPException(status_code = 404, detail = "Curso no encontrado.")
    cursos_db.remove(curso)
    return curso