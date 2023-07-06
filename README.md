# Blog Personal del Programador
---
Este repositorio contiene el código fuente de un blog personal desarrollado por Tobares Juan y Kissling Guillermo. El blog está construido utilizando Flask, HTML y Bootstrap, y proporciona una plataforma para que los programadores compartan su experiencia, proyectos y conocimientos.

#### Pasos para configurar y ejecutar el proyecto

**Sigue los siguientes pasos para configurar y ejecutar el blog personal en tu entorno local**:

1. Clona este repositorio en tu máquina local:

        git clone https://github.com/tu_usuario/blog-personal.git
2. Crea un entorno virtual utilizando venv. Abre una terminal y ejecuta el siguiente comando (reemplaza "nombre_del_entorno" por el nombre que deseas darle al entorno):

        python -m venv nombre_del_entorno
        Si el comando anterior no funciona, intenta usar python3 en lugar de python:

        python3 -m venv nombre_del_entorno
3. Activa el entorno virtual. En la misma terminal, ejecuta el siguiente comando:

        source nombre_del_entorno/bin/activate
4. Instala las dependencias del proyecto. Asegúrate de que estás en la raíz del proyecto y ejecuta el siguiente comando:

        pip install -r requirements.txt

5. Inicia el servidor. Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

        flask run --reload
6. Ahora podrás acceder al blog personal del programador en tu navegador a través de la dirección http://localhost:5000.

---