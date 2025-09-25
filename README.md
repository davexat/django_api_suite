# Django API Suite

## Descripción

Django API Suite es una aplicación web backend integral construida con Django y Django REST Framework. Proporciona múltiples endpoints de API para diferentes propósitos, incluyendo una API REST de demostración para gestión de usuarios, una API de landing page con integración a Firebase, y una interfaz de inicio limpia. El proyecto está diseñado para escalabilidad, prácticas modernas de desarrollo web e integración perfecta de APIs con soluciones de base de datos tanto en memoria como en la nube.

🚀 **Demo en vivo:** [https://davexat.pythonanywhere.com/](https://davexat.pythonanywhere.com/)

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints de la API](#endpoints-de-la-api)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Características

- **Interfaz de Inicio:** Página de inicio limpia y responsiva con UI moderna usando Tailwind CSS y fuentes Inter/Noto Sans.
- **API REST de Demostración:** Operaciones CRUD completas para gestión de usuarios con almacenamiento de datos en memoria.
- **API de Landing:** Integración con Firebase Realtime Database para gestión de comentarios con timestamps automáticos.
- **Interfaz de Administración:** Panel de administración Django integrado para gestión backend.
- **Gestión de Archivos Estáticos:** Servicio de archivos estáticos optimizado con configuración adecuada.
- **Diseño Responsivo:** Interfaz amigable para móviles con soporte de modo oscuro.
- **Documentación de API:** Estructura de API RESTful siguiendo las mejores prácticas de Django REST Framework.
- **Integración Firebase:** Conectividad con base de datos en tiempo real para almacenamiento de datos en la nube.
- **Generación UUID:** Generación de identificadores únicos para consistencia de datos.

## Tecnologías Utilizadas

<a href="https://www.djangoproject.com/">![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)</a>
<a href="https://www.django-rest-framework.org/">![Static Badge](https://img.shields.io/badge/Django%20REST%20Framework-red?style=for-the-badge&logo=django&logoColor=white)</a>
<a href="https://www.python.org/">![Static Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)</a>
<a href="https://firebase.google.com/">![Static Badge](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)</a>
<a href="https://tailwindcss.com/">![Static Badge](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)</a>
<a href="https://www.sqlite.org/">![Static Badge](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)</a>

## Estructura del Proyecto

```
django_api_suite/
├── backend_data_server/          # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py                   # Configuración ASGI
│   ├── settings.py               # Configuraciones Django con config Firebase
│   ├── urls.py                   # Enrutamiento principal de URLs
│   └── wsgi.py                   # Configuración WSGI
├── homepage/                     # App de página de inicio
│   ├── __init__.py
│   ├── admin.py                  # Configuración del admin
│   ├── apps.py                   # Configuración de la app
│   ├── models.py                 # Modelos de base de datos
│   ├── urls.py                   # Patrones URL de homepage
│   ├── views.py                  # Vistas de homepage
│   └── migrations/               # Migraciones de base de datos
├── demo_rest_api/                # App de API REST de demostración
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py                   # Patrones URL de API
│   ├── views.py                  # Vistas API CRUD
│   └── migrations/
├── landing_api/                  # API de landing page con Firebase
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py                   # Patrones URL de Landing API
│   ├── views.py                  # Vistas de integración Firebase
│   └── migrations/
├── templates/                    # Plantillas HTML
│   └── homepage/
│       └── index.html            # Plantilla principal de homepage
├── static/                       # Archivos estáticos (CSS, JS, Imágenes)
│   └── img/
├── secrets/                      # Credenciales Firebase (privado)
├── env/                          # Entorno virtual
├── manage.py                     # Script de gestión Django
├── requirements.txt              # Dependencias Python
├── db.sqlite3                    # Base de datos SQLite
├── LICENSE                       # Licencia MIT
└── README.md                     # Este archivo README
```

## Instalación

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/davexat/django_api_suite.git
   cd django_api_suite
   ```

2. **Crear y activar entorno virtual:**
   ```sh
   python -m venv env
   
   # En Windows
   env\Scripts\activate
   
   # En macOS/Linux
   source env/bin/activate
   ```

3. **Instalar dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configurar Firebase (opcional para Landing API):**
   - Crear un proyecto Firebase y descargar la clave de cuenta de servicio
   - Colocar el archivo de clave en el directorio `secrets/` como `landing-key.json`
   - Actualizar la URL de la base de datos en `settings.py` si es necesario

5. **Ejecutar migraciones:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (opcional):**
   ```sh
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo:**
   ```sh
   python manage.py runserver
   ```

## Uso

- **Página de Inicio:** Visita [http://localhost:8000/](http://localhost:8000/) para la interfaz principal
- **Panel de Administración:** Accede a [http://localhost:8000/admin/](http://localhost:8000/admin/) para administración backend
- **API de Demostración:** Usa [http://localhost:8000/demo/rest/api/index/](http://localhost:8000/demo/rest/api/index/) para gestión de usuarios
- **API de Landing:** Accede a [http://localhost:8000/landing/api/index/](http://localhost:8000/landing/api/index/) para comentarios

## Endpoints de la API

### API REST de Demostración
- `GET /demo/rest/api/index/` - Obtener todos los usuarios activos
- `POST /demo/rest/api/index/` - Crear un nuevo usuario
- `GET /demo/rest/api/<id>/` - Obtener usuario específico por ID
- `PUT /demo/rest/api/<id>/` - Actualizar usuario (actualización completa)
- `PATCH /demo/rest/api/<id>/` - Actualizar usuario (actualización parcial)
- `DELETE /demo/rest/api/<id>/` - Eliminación suave del usuario (marcar como inactivo)

### API de Landing
- `GET /landing/api/index/` - Obtener todos los comentarios de Firebase
- `POST /landing/api/index/` - Crear un nuevo comentario con timestamp

### Ejemplos de Uso de la API

**Crear un nuevo usuario:**
```bash
curl -X POST http://localhost:8000/demo/rest/api/index/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Pérez", "email": "juan@example.com"}'
```

**Crear un comentario:**
```bash
curl -X POST http://localhost:8000/landing/api/index/ \
  -H "Content-Type: application/json" \
  -d '{"author": "María", "message": "¡Hola mundo!"}'
```

## Contribuir

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias, por favor envía un pull request o abre un issue.

1. Haz fork del proyecto
2. Crea tu rama de feature (`git checkout -b feature/CaracteristicaIncreible`)
3. Haz commit de tus cambios (`git commit -m 'Agregar alguna CaracteristicaIncreible'`)
4. Haz push a la rama (`git push origin feature/CaracteristicaIncreible`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**Autores:** 
- David Elias Sandoval Bernitta
- Bruno Rafael Romero Yagual

**Proyecto:** Django API Suite  
**Año:** 2025