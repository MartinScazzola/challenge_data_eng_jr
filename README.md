# Challenge for Data Eng. Jr

## Consigna

Desarrollar un programa que utilizando los datos de los archivos medias.csv y mmp.csv realice los siguientes pasos:
- Valide que no hayan caracteres especiales en los campos con tipo string (solo se pueden los caracteres punto y las letras del alfabeto '.' y 'a-z')
- Merge la data de las dos fuentes basandose en la fecha, el app_id, la campaña, los creativos y el pais.
- Agregar los campos CPI (Cost per install), and CPC (Cost per click)


**Luego responder las siguientes preguntas:**
- Cual es el pais con mas gasto?
- Cual es la campaña que mejor performance tuvo (menor CPI)
- Cual es la campaña con mas installs
- Cual fue el dia que mas installs 


**Importante:**
- Utilizar Python >= 3.10
- Utilizar Pandas
- Codigo polimorfico
- Reutilizar Codigo
- Manejo de errores

**Extra:**
- Utilizar [Docker](https://www.docker.com)
- Utilizar [Black](https://pypi.org/project/black/)
- Utilizar [Poetry](https://python-poetry.org)

### Para formatear el codigo con black ejecutar:

``` bash
black challenge.py
```

