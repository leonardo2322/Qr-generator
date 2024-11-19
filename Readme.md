# **Django QR Code Generator**

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios crear, listar y eliminar códigos QR. Es una solución simple pero efectiva para la gestión de códigos QR, ideal para proyectos de aprendizaje o implementación básica.

---

## **Características**

- **Gestión de usuarios:**
  - Registro y autenticación de usuarios.
- **Creación de códigos QR:**
  - Generación de códigos QR personalizados basados en una URL o texto ingresado.
- **Listado de códigos QR:**
  - Visualización de todos los códigos QR creados por el usuario autenticado.
- **Eliminación de códigos QR:**
  - Función para eliminar códigos QR específicos.

---

## **Requisitos Previos**

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.8+
- Django 4.x
- Docker (opcional, para ejecutar con contenedores)
- Git (opcional, para clonar el repositorio)

---

## **Instalación y Ejecución**

#### 1.**Clona este repositorio**

```bash o windows
git clone https://github.com/leonardo2322/Qr-generator.git
cd Qrgenerator

```

#### 2. **Crea un entorno virtual **

```terminal
- python -m venv env
- source env/bin/activate # En Windows: env\Scripts\activate
```

#### 3. **con el entorno activo ejecuta en la terminal**

```terminal shell o bash
- pip install -r requirements.txt
```

#### 4. **con el entorno activo ejecuta en la terminal cd .\Qrgenerator**

- python manage.py migrate

#### 5. **Ejecuta el servidor local**

```terminal shell o bash
python manage.py runserver
```

### **Con docker**

```terminal o shell
ejecuta este comando

- docker build -t paper23/qr_generator:latest .
 esto creara la imagen

 y luego carga el container  qr-generator-container  este nombre lo puedes colocar como tu quieras

- docker run -d -p 8000:8000 --name qr-generator-container paper23/qr_generator:latest

y ya puedes acceder a localhost/8000/app/ y tendras la app funcionando

```
