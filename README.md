## M7_desafio_2

### 1. Crea un entorno virtual:
python -m venv venv

### 2. Activa el entorno virtual
source venv/Scripts/activate

### 3. Instalar django y psycopg2
pip install django
pip install psycopg2 
pip install --upgrade pip
pip list

### 4. Crear proyecto
django-admin startproject registro_cursos
cd registro_cursos

### 5. crear app dentro del proyecto
python manage.py startapp gestion_cursos

### 6. en settings.py -> installed_apps
'gestion_cursos',

### 7. en models.py crear modelos

### 8. aplicar migraciones
python manage.py makemigrations
python manage.py migrate

### 9. Crear archivo services.py en carpeta gestion_cursos
para implementar las funciones

### 10. pruebas en la shell
importar las funciones en services.py

### 11. Llamar a las Funciones (carpeta querys)

    a. Crear un Curso
    curso1 = crear_curso("Matemáticas", "Curso básico de matemáticas")
    print(curso1)
    
    b. Crear un Profesor
    profesor1 = crear_profesor("Juan", "Pérez", "Calle Falsa 123", "Santiago", "Chile")
    print(profesor1)
    
    c. Crear un Estudiante
    estudiante1 = crear_estudiante("Ana", "González", "Calle Real 456", "Valparaíso", "Chile")
    print(estudiante1)
    
    d. Agregar un Profesor a un Curso
    agregar_profesor_a_curso(profesor1, curso1)
    
    e. Agregar Cursos a un Estudiante
    agregar_cursos_a_estudiante(estudiante1, curso1)
    
    f. Obtener un Estudiante por Nombre
    resultado_estudiante = obtiene_estudiante("Ana")
    print(resultado_estudiante)
    
    g. Obtener un Profesor por Nombre
    resultado_profesor = obtiene_profesor("Juan")
    print(resultado_profesor)
    
    h. Obtener un Curso por Nombre
    resultado_curso = obtiene_curso("Matemáticas")
    print(resultado_curso)
    
    i. Imprimir Cursos de un Estudiante
    imprime_estudiante_cursos(estudiante1)




