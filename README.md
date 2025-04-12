
# 📝 Prueba Técnica - Felipe Campagnoli

Este proyecto es una **API REST** construida con **Django REST Framework** que permite gestionar una lista de tareas (_To-Do List_).  
La aplicación está dockerizada y cuenta con **tests automáticos usando Pytest**.

---

## 🚀 Requisitos previos

- Python 3.10+
- Docker
- Make (opcional, pero recomendado)

---

## 🧱 Stack Tecnológico

- Python 3.10
- Django 4+
- Django REST Framework
- Docker
- Pytest
- Flake8 + Black
- Make (para automatización de comandos)

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git 
cd prueba-backend
```

### 2. Levantar la aplicación con Docker

```bash
make build   # Construye la imagen
make up      # Inicia los contenedores
```

La API estará disponible en:  
👉 [http://localhost:8000/api/tasks/](http://localhost:8000/api/tasks/)

---

## 🧪 Tests

Para ejecutar los tests automáticos con **Pytest**:

```bash
make test
```

Si todo funciona correctamente, verás algo como:

```
[100%] ===== 5 passed in 0.64s =====
```

---

## 🧼 Linting y Formato

- Verificar el estilo del código con **Flake8**:

```bash
make lint
```

- Formatear el código automáticamente con **Black**:

```bash
make format
```

---

## ⚙️ Comandos disponibles (`Makefile`)

| Comando              | Descripción                                  |
|----------------------|----------------------------------------------|
| `make up`            | Levanta la app con Docker                    |
| `make down`          | Detiene y limpia los contenedores            |
| `make build`         | Reconstruye la imagen Docker                 |
| `make migrate`       | Aplica migraciones                           |
| `make makemigrations`| Crea nuevas migraciones                      |
| `make test`          | Ejecuta los tests con Pytest                 |
| `make lint`          | Verifica el estilo de código (Flake8)        |
| `make format`        | Formatea el código con Black                 |
| `make createsuperuser` | Crea un superusuario de Django             |
| `make shell`         | Abre el shell interactivo de Django         |

