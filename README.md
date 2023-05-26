Este proyecto utiliza streamlit, por lo tanto para que funcione debes seguir los siguientes pasos en windows:

¡SI NO TIENES UN ENTORNO VIRTUAL CREADO!
1. Clona el repositorio o descarga el archivo .zip en tu computador
2. Instala un entorno virtual:
  1. Abre el cmd de tu computador
  2. Accede a la carpeta donde está el proyecto y todos los códigos con el comando cd "ruta de acceso de la carpeta"
  3. Pega este comando: py -m venv venv
  4. Pega este comando: venv\Scripts\activate.bat
  5. Una vez veas (venv) al lado izquierdo, instala las librerías necesarias para que el proyecto funcione pegando los siguientes comandos:
    1. pip install streamlit
    2. pip install streamlit-extras
    3. pip install networkx
3. Una vez creado el entorno virtual con las librerias necesarias instaladas, corre el programa pegando el siguiente comando: streamlit run homepage.py

¡SI YA TIENES EL ENTORNO VIRTUAL CREADO DENTRO DE TU CARPETA!
1. Abre el cmd de tu computador
2. Accede a la carpeta donde está el proyecto y todos los códigos con el comando cd "ruta de acceso de la carpeta"
3. Si no tienes las librerias necesarias para que el proyecto funcione, instalalas
4. Corre el programa pegando el siguiente comando: streamlit run homepage.py
