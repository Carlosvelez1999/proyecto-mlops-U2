# 🩺 Servicio de Diagnóstico Médico - Universidad Icesi

Este proyecto implementa un sistema básico de diagnóstico médico utilizando **Flask** y **Docker**.  
La aplicación expone una API que permite predecir el estado de salud de un paciente con base en su edad, presencia de fiebre y nivel de dolor.  
También incluye una interfaz web desarrollada en HTML con Bootstrap, y rutas adicionales para visualizar estadísticas, descargar resultados en `.txt` y ejecutar pruebas automatizadas mediante GitHub Actions.

---

## 📦 Requisitos

- Tener **Docker instalado**
- Contar con un navegador para ejecutar `index.html` localmente
- Python ≥ 3.10 (solo si se desea ejecutar local sin Docker)

---

## 🚀 Ejecución (vía Docker)

1. Clonar el repositorio:

```bash
git clone https://github.com/Carlosvelez1999/proyecto-mlops-U2.git
cd proyecto-mlops-U2
```

2. Construir la imagen:

```bash
docker build -t diagnostico-medico .
```

3. Ejecutar el contenedor:

```bash
docker run -p 5000:5000 diagnostico-medico
```

📍 Visita `http://localhost:5000`

---

## 🧪 Uso del sistema

### 🔸 Interfaz Web

1. Abre `index.html` en tu navegador.
2. Llena el formulario con:
   - Edad (0 a 120)
   - Si tiene fiebre
   - Nivel de dolor (0 a 10)
3. Haz clic en **Enviar**.
4. Opcional:
   - **Ver estadísticas** → `/estadisticas`
   - **Descargar historial** → `/descargar-resultados`

---

## 🧠 Diagnósticos posibles

- NO ENFERMO  
- ENFERMEDAD LEVE  
- ENFERMEDAD AGUDA  
- ENFERMEDAD CRÓNICA  
- ENFERMEDAD TERMINAL

---

## 📬 Endpoints disponibles

### `/predecir` `[POST]`

```json
{{
  "edad": 75,
  "fiebre": true,
  "dolor": 9
}}
```

➡️ Respuesta:

```json
{{
  "diagnostico": "ENFERMEDAD TERMINAL"
}}
```

---

### `/estadisticas` `[GET]`

Devuelve:

- Conteo por categoría
- Últimas 5 predicciones
- Fecha/hora de la última

---

### `/descargar-resultados` `[GET]`

Descarga un `.txt` con predicciones registradas:

```
[10/05/2025 11:13 AM] → Diagnóstico: ENFERMEDAD LEVE
```

---

## 🧪 Pruebas unitarias

Se encuentra el archivo `test_app.py` con pruebas automatizadas de:

- Diagnóstico terminal esperado
- Contenido textual en `/estadisticas`

Puedes correrlas localmente con:

```bash
pytest test_app.py
```

---

## ⚙️ CI/CD con GitHub Actions

Se usa GitHub Actions para:

1. Ejecutar pruebas unitarias en Pull Requests y Push
2. Comentar el estado de ejecución en los PRs
3. Crear imagen Docker y subirla a GitHub Packages

Workflow: `.github/workflows/ci.yml`

---

## 🗂️ Estructura del proyecto

```
📁 Diagnostico_Medico/
│
├── app.py                    # API principal
├── index.html                # Interfaz web
├── test_app.py               # Pruebas unitarias
├── Dockerfile                # Imagen del contenedor
├── requirements.txt          # Dependencias Python
├── .dockerignore             # Ignorar archivos en Docker
├── .github/workflows/ci.yml  # Workflow de CI/CD
├── resultados/               # Carpeta con predicciones
│   └── predicciones.txt
├── CHANGELOG.md              # Registro de cambios entre versiones
└── README.md                 # Este archivo
```

---

## 📜 Historial de cambios

Para ver los cambios entre la versión inicial del pipeline y esta versión final con MLOps integrado, revisa el archivo:

📄 [`CHANGELOG.md`](./CHANGELOG.md)

---

## 👨‍💻 Autor

**Carlos Alberto Velez**  
Maestría en Inteligencia Artificial  
Universidad Icesi – Curso MLOps

