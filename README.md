# StudentOverflow
# Student Overflow

Student Overflow es una plataforma de preguntas y respuestas diseñada para estudiantes. Permite a los usuarios registrar sus cuentas, iniciar sesión, publicar preguntas, responder a preguntas, agregar comentarios y etiquetas (tags), y votar tanto preguntas como respuestas.

## 🚀 Funcionalidades

- **Registro de usuario**: Los usuarios pueden crear una cuenta con su nombre, correo, teléfono y contraseña.
- **Inicio de sesión**: Autenticación segura utilizando JWT para mantener la sesión activa.
- **Publicar preguntas**: Los usuarios pueden crear nuevas preguntas con título y contenido.
- **Respuestas y comentarios**: Los usuarios pueden responder preguntas y comentar sobre las respuestas existentes.
- **Etiquetas (Tags)**: Se pueden agregar etiquetas para categorizar las preguntas.
- **Votaciones**: Sistema de votación para preguntas y respuestas.
- **Dashboard**: Vista principal que muestra las preguntas más recientes y permite interactuar con ellas.
- **Perfil de usuario**: Visualización y edición del perfil del usuario.

## 🛠️ Tecnologías Utilizadas

- **Frontend**: PyQt6
- **Backend**: Flask
- **Base de datos**: PostgreSQL 
- **Autenticación**: JWT (JSON Web Token)
- **Comunicación**: API REST
- **Diagrama ERD**: DBeaver

## 📋 Requisitos Previos

- Python 3.10+
- PostgreSQL (Recomendado: Supabase)
- LibreOffice (para conversión de archivos, si es necesario)
- Git

## ⚙️ Configuración del Entorno

Hemos configurado un archivo **`.gitignore`** para excluir archivos innecesarios como:

- Directorios de entorno virtual (`.venv/`, `env/`).
- Archivos temporales (`__pycache__/`).
- Archivos de configuración (`.env`, `.vscode/`).
- Archivos de logs (`*.log`).

Esto asegura que solo los archivos relevantes se mantengan en el repositorio.

