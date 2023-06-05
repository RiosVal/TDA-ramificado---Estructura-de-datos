PUEDES VER LA APP EN LINEA HACIENDO CLICK EN ESTE ENLACE: https://proyectotdaramificado.streamlit.app/
Por favor ten en cuenta que si ves algo extraño en la app, probablemente se arreglará refrescando la página

Si lo que quieres es descargar el codigo en un archivo .zip o clonar el repositorio, debs tener en cuenta que, este proyecto utiliza streamlit, por lo tanto para que funcione debes seguir los siguientes pasos en windows:

¡SI NO TIENES UN ENTORNO VIRTUAL CREADO!
1. Clona el repositorio o descarga el archivo .zip en tu computador
2. Instala un entorno virtual:
  - Abre el cmd de tu computador
  - Accede a la carpeta donde está el proyecto y todos los códigos con el comando cd "ruta de acceso de la carpeta"
  - Pega este comando: py -m venv venv
  - Pega este comando: venv\Scripts\activate.bat
  - Una vez veas (venv) al lado izquierdo, instala las librerías necesarias para que el proyecto funcione pegando los siguientes comandos:
    1. pip install streamlit
    2. pip install streamlit-extras
    3. pip install networkx
    4. pip install scikit-learn
    5. pip install pyvis
3. Una vez creado el entorno virtual con las librerias necesarias instaladas, corre el programa pegando el siguiente comando: streamlit run homepage.py

¡SI YA TIENES EL ENTORNO VIRTUAL CREADO DENTRO DE TU CARPETA!
1. Abre el cmd de tu computador
2. Accede a la carpeta donde está el proyecto y todos los códigos con el comando cd "ruta de acceso de la carpeta"
3. Si no tienes las librerias necesarias para que el proyecto funcione, ¡instalalas!
4. Corre el programa pegando el siguiente comando: streamlit run homepage.py
