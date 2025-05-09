
# 🩺 Servicio de Diagnóstico Médico - Universidad Icesi

Este proyecto implementa un sistema básico de diagnóstico médico utilizando **Flask** y **Docker**.  
La aplicación expone una API que permite predecir el estado de salud de un paciente con base en su edad, presencia de fiebre y nivel de dolor.  
También incluye una interfaz web desarrollada en HTML y una ruta adicional para visualizar estadísticas de uso.

---

## 📦 Requisitos

- Tener **Docker instalado** en el equipo (versión reciente)
- Contar con un navegador para ejecutar `index.html` localmente

---

## 🚀 Instrucciones de ejecución (vía Docker)

1. Clonar el repositorio o ubicarse en la carpeta del proyecto:

```bash
git clone https://github.com/Carlosvelez1999/proyecto-mlops-U2.git
cd proyecto-mlops-U2
```

2. Construir la imagen Docker:

```bash
docker build -t diagnostico-medico .
```

3. Ejecutar el contenedor:

```bash
docker run -p 5000:5000 diagnostico-medico
```

Esto expondrá el servicio en:  
📍 `http://localhost:5000`

---

## 🧪 Uso del sistema

### 🔸 Interfaz web

1. Abrir el archivo `index.html` en el navegador.
2. Ingresar los datos del paciente:
   - Edad (0–120)
   - Si tiene fiebre (Sí / No)
   - Nivel de dolor (0–10)
3. Hacer clic en **Enviar** y visualizar el diagnóstico generado.

---

## 🧠 Diagnósticos posibles

La aplicación puede retornar una de las siguientes categorías:

- NO ENFERMO  
- ENFERMEDAD LEVE  
- ENFERMEDAD AGUDA  
- ENFERMEDAD CRÓNICA  
- **ENFERMEDAD TERMINAL** *(nueva categoría añadida)*

---

## 📬 Endpoints disponibles

### `/predecir`  `[POST]`

Permite enviar los síntomas del paciente y obtener un diagnóstico.

**Ejemplo de petición (curl):**

```bash
curl -X POST http://localhost:5000/predecir \
-H "Content-Type: application/json" \
-d '{"edad": 75, "fiebre": true, "dolor": 9}'
```

**Respuesta esperada:**

```json
{
  "diagnostico": "ENFERMEDAD TERMINAL"
}
```

---

### `/estadisticas`  `[GET]`

Muestra estadísticas acumuladas de uso del modelo.

**Ejemplo (en navegador o terminal):**

```bash
http://localhost:5000/estadisticas
```

**Respuesta esperada:**

```json
{
  "total_predicciones": 6,
  "ultimas_5_predicciones": [
    {"diagnostico": "ENFERMEDAD CRÓNICA", "fecha": "2025-05-08T20:41:34.906913"},
    ...
  ],
  "fecha_ultima_prediccion": "2025-05-08T20:41:34.906913"
}
```

---

## 🗂️ Estructura del proyecto

```
📁 Diagnostico_Medico/
│
├── app.py                # API con Flask
├── index.html            # Interfaz web para el usuario
├── Dockerfile            # Configuración para ejecución en contenedor
├── requirements.txt      # Librerías necesarias (usado internamente por Docker)
└── README.md             # Instrucciones del proyecto (este archivo)
```

---

## 👨‍💻 Autor

**Carlos Alberto Vélez**  
Maestría en Inteligencia Artificial  
Universidad Icesi – Curso MLOps
