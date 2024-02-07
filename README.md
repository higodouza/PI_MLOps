
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>


## **Presentacion e Introduccion**


El proyecto propuso emular la función de un Ingeniero MLOps, una fusión de las disciplinas de Ingeniería de Datos y Ciencia de Datos. La idea fue utilizar dato para la plataforma global de videojuegos, Steam, para realizar el estudio correspondiente. El objetivo principal fue desarrollar un Producto Mínimo Viable (MVP) que demuestre la implementación de una API en un servicio de nube, junto con un sistema de recomendacion de juegos para los usuarios.

Para su desarrollo, se trabajo a partir de dichos datos en crudo para crear todo el sistema solicitado. Se esperaba que el MPV no solo muestre una API desplegada en un servicio en la nube, sino que también aplicase un modelo de Aprendizaje Automático. Este enfoque garantiza que el proyecto estuvo alineado con las prácticas modernas de MLOps.


## **Tratamiento de los Datos - ETL**

Se utilizaron 3 archivo como base de datos para crear todo el diseno del proyecto. Estos dataset fueron trabajados a partir de un proceso de ETL (extracttion, Transformation and Load), para su optimo manejo. Por lo que se limpiaron tomando en cuenta los parametros mas relevantes para la toma de decisiones en funcion a lo requerido. Adicionalmentem, se crearon nuevas instancias que se iban a tomar en cuenta posteriormente para el diseno modelo de Machine Learning y el sistema de recomendaciones. 

## **Categorizacion de Reviews**

Para esta etapa se creo un campo llamado 'sentiment_analysis' que discriminaba los reviews que los usuarios le hacia a los juegos, tomando en cuenta esta jerarquia:
- 0 malo
- 1 neutral o sin review
- 2 positivo

Esto se logro a traves de una funcion que analiza los sentimientos de los reviews y los ubica en una de esas 3 categorias. De tal forma, se obtuvo data cuantificable todos los juegos con o sin review, para posteriormente ser analizada.

## **EDA - Exploratory Data Analysis**

Esta fase se baso en revisar a fondo los datos ya previamente tratados agrupandolos entre si de manera que, utilizando herramientas de graficos y tablas como Matplotlib y Seaborn, se pudiesen identificar patrones o rankings especificos sobre, por ejemplo, juegos mas jugados, juegos mas vendidos, tipos de reviews, etc, y asi obtener informacion relevante de dicha data.

## **Machine Learning** 

Por ultimo, se creo un modelo predictivo utilizando toda la data que se tenia para entrenarlo y que tambien, utilizando la lib surprise de python, nos ayudo a la tarea de recomendar juegos a un usuario en especifico partiendo de sus juegos que suele jugar, la cual era la tarea final.

## **FastAPI** 

Todo este trabajo, a parte de ser generado via codigo, se implemento en un framework de python llamado FastAPI, la cual nos permite levantar una especie de formulario interactivo que cuenta con nuestro programa por debajo que lo alimenta y presenta de manera mas amigable las querys posibles de nuestro programa final junto con sus salidas correspondientes a los input elegidos.

## **Render** 

Partiendo de que el proyecto se hizo de manera local, tambien se utilizo el aplicativo de servicios web de Render, que  ofrece un pequeno espacio de procesamiento para desplegar una API en la nube, de tal forma que se clonara todo el proyecto a una web libre alcanzable por internet. 

