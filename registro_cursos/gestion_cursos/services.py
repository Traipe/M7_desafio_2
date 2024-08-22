from .models import Curso, Profesor, Estudiante, Direccion, Inscripcion

def crear_curso(nombre, descripcion):
    curso = Curso.objects.create(nombre=nombre, descripcion=descripcion)
    return curso

def crear_profesor(nombre, apellido, calle, ciudad, pais):
    direccion = Direccion.objects.create(calle=calle, ciudad=ciudad, pais=pais)
    profesor = Profesor.objects.create(nombre=nombre, apellido=apellido, direccion=direccion)
    return profesor

def crear_estudiante(nombre, apellido, calle, ciudad, pais):
    direccion = Direccion.objects.create(calle=calle, ciudad=ciudad, pais=pais)
    estudiante = Estudiante.objects.create(nombre=nombre, apellido=apellido, direccion=direccion)
    return estudiante

def agregar_profesor_a_curso(profesor, curso):
    curso.profesores.add(profesor)

def agregar_cursos_a_estudiante(estudiante, *cursos):
    for curso in cursos:
        Inscripcion.objects.create(estudiante=estudiante, curso=curso)

def obtiene_estudiante(nombre):
    return Estudiante.objects.filter(nombre=nombre)

def obtiene_profesor(nombre):
    return Profesor.objects.filter(nombre=nombre)

def obtiene_curso(nombre):
    return Curso.objects.filter(nombre=nombre)

def imprime_estudiante_cursos(estudiante):
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante)
    for inscripcion in inscripciones:
        print(f"Curso: {inscripcion.curso.nombre}, Fecha de inscripción: {inscripcion.fecha_inscripcion}")
