from fastapi import FastAPI
from typing import Union
from funciones import developer
from funciones import userdata
from funciones import userForGenre  
from funciones import best_developer_year  
from funciones import  developer_reviews_analysis
from funciones import recomendacion_usuario
from fastapi.responses import JSONResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/developer/{desarrollador}")
async def desarrollador(desarrollador: str):
    try:
        resultado = developer(desarrollador)
        return resultado
    except Exception as e:
        return {"error": str(e)}    


@app.get("/userdata/{user_id}")
async def user(user_id: str):
    try:
        result = userdata(user_id)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/genre/{genero}")
async def genre(genero: str):
    try:
        resultado = userForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}    


@app.get("/best_developer_year/{año}")
async def Best_developer_year(year: str):
    try:
        year_int = int(year)  # Convertir el año a un entero
        result2 = best_developer_year(year_int)
        return result2
    except Exception as e:
        return {"error": str(e)}                                      

@app.get("/developer_reviews_analysis/{desarrolladora}") 
async def get_developer(desarrolladora: str):
    try:
        resultado= developer_reviews_analysis(desarrolladora)
        return resultado
    except Exception as e:
        return {"error":str(e)}


@app.get("/recomendacion_usuario/{user_id}")
async def get_recomendacion(user_id: str):
    try:
        resultado= recomendacion_usuario(user_id)
        return resultado
    except Exception as e:
        return {"error":str(e)}

