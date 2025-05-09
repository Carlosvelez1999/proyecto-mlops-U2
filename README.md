
# Servicio de Diagnóstico Médico - Universidad Icesi

Este proyecto permite simular un diagnóstico médico básico usando Flask y Docker.

## Requisitos
- Tener Docker instalado

## Instrucciones

1. Construir la imagen:
```
docker build -t diagnostico-medico .
```

2. Ejecutar el contenedor:
```
docker run -p 5000:5000 diagnostico-medico
```

3. Acceder desde navegador con index.html o enviar petición con curl/postman:
```
curl -X POST http://localhost:5000/predecir -H "Content-Type: application/json" -d '{"edad": 45, "fiebre": true, "dolor": 6}'
```
