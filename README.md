# Proyecto Educativo sobre Inteligencia Artificial

Este es un proyecto académico que tiene como fin el desarrollo de una página web a través del vibecoding utilizando el lenguaje **Python** y el framework **Django**.

---

## 🚀 Características Clave

1. **Landing Page Pública**: Presenta el título del proyecto y una sección dinámica de curiosidades científicas sobre Inteligencia Artificial cargadas desde la base de datos.
2. **Control de Acceso y Autenticación**: Sistema completo de registro (`Register`) e inicio de sesión (`Login`) de alumnos utilizando el módulo seguro integrado de Django (`django.contrib.auth`), con encriptación de contraseñas.
3. **Módulo Educativo Protegido**: Sección de acceso exclusivo para usuarios autenticados que contiene:
   - **3 definiciones** clave de IA formuladas por autores consagrados de la disciplina.
   - Una definición general estructurada sobre **Redes Neuronales Artificiales**.
   - La clasificación detallada de **7 tipos de redes neuronales**, explicando qué son y cómo funcionan.
4. **Diseño Visual e Interactivo Premium**:
   - Estilizado en HSL personalizado (paleta azul pizarra tecnológica con acentos cian y violeta).
   - Efectos de *glassmorphism* (vidrio glaseado) en formularios y elementos flotantes.
   - Micro-animaciones sutiles y cambios de elevación interactivos al pasar el mouse por encima (*hover*).
   - **Efecto de Descubrimiento progresivo (Scroll Reveal)**: Mediante la API nativa de JavaScript `IntersectionObserver`, el contenido protegido se va revelando gradualmente a medida que el usuario desciende en la página.
5. **Carga Automatizada de Datos (Data Migrations)**: Al ejecutar las migraciones, la base de datos se pobla de manera automática con las definiciones académicas y las curiosidades, garantizando que el sitio web no se muestre vacío desde el primer arranque.

---

## 🛠️ Requisitos Previos

Asegúrate de tener instalado:
- **Python 3.8** o superior.
- **Git** (opcional, para clonar el repositorio).

---

## ⚙️ Instrucciones de Instalación y Despliegue

Sigue estos pasos detallados para replicar y ejecutar el proyecto en tu entorno local:

### 1. Descargar o Clonar el Repositorio
Si usas Git, ejecuta en tu terminal:
```bash
git clone <URL_DEL_REPOSITORIO>
cd "Vibecoding page"
```
*(O simplemente descomprime el archivo ZIP del proyecto en una carpeta y abre una terminal allí).*

### 2. Crear el Entorno Virtual
Crea un entorno virtual aislado para evitar conflictos de dependencias:
*   **En Windows:**
    ```bash
    python -m venv .venv
    ```
*   **En macOS/Linux:**
    ```bash
    python3 -m venv .venv
    ```

### 3. Activar el Entorno Virtual
Activa el entorno antes de instalar las dependencias:
*   **En Windows (PowerShell):**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
*   **En Windows (CMD):**
    ```cmd
    .venv\Scripts\activate.bat
    ```
*   **En macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

*(Sabrás que está activo porque aparecerá `(.venv)` al inicio de la línea de comandos de tu terminal).*

### 4. Instalar las Dependencias
Instala Django y las bibliotecas necesarias listadas en el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Ejecutar las Migraciones (Carga automática de datos)
Este paso crea la base de datos SQLite y ejecuta la migración de datos que inserta de forma automática las curiosidades, definiciones de IA y tipos de redes neuronales:
```bash
python manage.py migrate
```

### 6. Crear un Administrador (Superusuario) - Opcional
Para gestionar el contenido (agregar o modificar curiosidades y definiciones) desde el panel de administración de Django, crea una cuenta de administrador:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones en consola (indica nombre de usuario, correo y una contraseña segura).

### 7. Iniciar el Servidor de Desarrollo
Inicia el servidor local de Django:
```bash
python manage.py runserver
```

### 8. Acceder a la Aplicación
Abre tu navegador de preferencia e ingresa a:
- **Sitio Web:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (accede con el superusuario creado en el paso 6).

---

## 📂 Estructura y Arquitectura del Proyecto

El proyecto está diseñado bajo la arquitectura MTV de Django:

- **`config/`**: Carpeta de configuración global del proyecto.
  - `settings.py`: Contiene los ajustes de idioma (`es-ar`), zona horaria, registro de la app `education` y rutas de redirección de login/logout.
  - `urls.py`: Enrutamiento raíz que redirige a las URLs de la aplicación.
- **`education/`**: Carpeta de la aplicación educativa.
  - `models.py`: Modelos de base de datos (`Curiosity`, `AIDefinition`, `Concept`, `NeuralNetworkType`).
  - `views.py`: Controladores lógicos (Landing page, registro, login, logout, y contenido protegido con decorador `@login_required`).
  - `urls.py`: Mapeo de rutas internas (`/`, `/registro/`, `/login/`, `/contenido/`).
  - `migrations/`: Historial de base de datos. Resalta `0002_initial_data.py`, encargado de poblar el contenido educativo académico de forma automática.
  - **`templates/education/`**: Plantillas HTML.
    - `base.html`: Esqueleto global con el diseño responsivo, menú de navegación y notificaciones toast.
    - `landing.html`: Página de inicio pública.
    - `login.html` & `register.html`: Pantallas de autenticación de alumnos.
    - `content.html`: Panel didáctico protegido que implementa el descubrimiento gradual.
  - **`static/`**: Recursos estáticos.
    - `css/styles.css`: Estilos visuales a medida con soporte de HSL, glassmorphism, responsive, e interactividades hover/reveal.
    - `js/main.js`: Lógica para accionar el `IntersectionObserver` y desencadenar las transiciones de scroll.
    - `images/`: Contiene diagramas y cabeceras del curso generados mediante Inteligencia Artificial.
