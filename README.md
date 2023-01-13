# Pràctica 2 - Tipologia i cicle de vida de les dades
Assignatura: M2.851 / Semestre: 2022-1 / Data: 09-01-2023

## Autors
  * Sara Jose Roig - [sjoser@uoc.edu](sjoser@uoc.edu)
  * Joan Peracaula Prat - [joanperacaula@uoc.edu](joanperacaula@uoc.edu)

## Descripció

En aquesta pràctica consisteix de 3 parts. Primerament hem fet una neteja de les dades obtingudes en la pràctica anterior, després hem fet una integració per corregir valors buits mitjançant les coordenades de latitud i longitud extretes d'una font externa. A continuació, hem fet un anàlisi d'aquestes dades: univariant, bivariant, multivariant, de normalitat i homogeneïtat de les dades. També inclou un model de regressió logística per a la categorització de les dades entre allotjaments de pagament i gratuïts. Finalment, n'hem extret uns resultats.


## Estructura del projecte 

 - `memoria.pdf`: Document memòria del projecte, amb les respostes de l'enunciat. 
 - `LICENSE`: Llicència del projecte, The MIT License.   
 - `/code`: Directori amb el codi utilitzat. 
   - `/code/main.py`: Fitxer python punt d'entrada al programa. 
   - `/code/clean_data.py`: Fitxer que s'encarrega del procés de neteja de les dades i les guarda a la carpeta data.
   - `/code/requirements.txt`: Fitxer amb les dependències necessàries per executar el codi.
   - `/code/data_analysis.ipynb`: Jupyter notebook amb diferents tipus d'anàlisi de les dades
   - `/code/data_integration.py`: Fitxer que s'encarrega d'integrar dades de una font externa en forma de DEM (Digital Elevation Model).   
 - `/data`: Directori amb el dataset. 
   - `/data/initial_shelters_and_campsites.csv`: Fitxer CSV que conté totes les dades scrapejades.
   - `/data/final_shelters_and_campsites.csv`: Fitxer CSV que conté totes les dades després de haver fet una neteja de dades.
    - `/raster_data`: Conjunt de fitxers amb les coordenades de Espanya, Andorra i França.
    
 
## Dataset 

El dataset consisteix en una llista de llocs on dormir a la muntanya, siguin refugis (lliures o guardats) o bé espais d’acampada habilitats, en les regions d’Espanya, Andorra i sud de França. El lloc web d’on s’ha extret aquesta informació és https://www.walkaholic.me  
El dataset s'ha obtingut de les dades scrapejades a la pràctica 1 i està publicat la plataforma Zenodo amb DOI [10.5281/zenodo.7338336](https://doi.org/10.5281/zenodo.7338336).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7338336.svg)](https://doi.org/10.5281/zenodo.7338336)

## Video de presentació 