from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from collections import Counter
import os

app = Flask(__name__)
CORS(app)

historial = []

# Definir zona horaria de Colombia (UTC-5)
zona_colombia = timezone(timedelta(hours=-5))

# Asegurar que exista la carpeta para guardar resultados
os.makedirs("resultados", exist_ok=True)

@app.route('/predecir', methods=['POST'])
def predecir():
    datos = request.json
    edad = datos.get('edad')
    fiebre = datos.get('fiebre')
    dolor = datos.get('dolor')

    # Validaciones
    if edad not in range(0, 121):
        return jsonify({'error': 'Edad fuera de rango permitido'}), 400
    if fiebre not in [True, False]:
        return jsonify({'error': 'Valor de fiebre inválido'}), 400
    if dolor not in range(0, 11):
        return jsonify({'error': 'Nivel de dolor fuera de rango'}), 400

    # Diagnóstico
    if edad > 70 and fiebre and dolor >= 8:
        resultado = "ENFERMEDAD TERMINAL"
    elif edad < 30 and dolor < 3 and not fiebre:
        resultado = "NO ENFERMO"
    elif dolor < 5:
        resultado = "ENFERMEDAD LEVE"
    elif fiebre and dolor >= 5:
        resultado = "ENFERMEDAD AGUDA"
    else:
        resultado = "ENFERMEDAD CRÓNICA"

    # Fecha local y registro
    fecha_actual = datetime.now(zona_colombia)
    historial.append({
        "diagnostico": resultado,
        "fecha": fecha_actual.isoformat()
    })

    # Guardar en archivo con formato amigable
    fecha_formato_txt = fecha_actual.strftime("%d/%m/%Y %I:%M %p")
    with open("resultados/predicciones.txt", "a", encoding="utf-8") as f:
        f.write(f"[{fecha_formato_txt}] → Diagnóstico: {resultado}\n")

    return jsonify({'diagnostico': resultado})


@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    if not historial:
        return jsonify({"mensaje": "Aún no se han registrado predicciones."}), 200

    # 1. Conteo por categoría
    conteo = Counter([registro["diagnostico"] for registro in historial])

    # 2. Últimas 5 predicciones (formato texto)
    ultimas = historial[-5:]
    ultimas_texto = [
        f'{datetime.fromisoformat(item["fecha"]).strftime("%d/%m/%Y %I:%M %p")} - {item["diagnostico"]}'
        for item in ultimas
    ]

    # 3. Fecha formateada de la última predicción
    ultima_fecha = ultimas[-1]["fecha"]
    fecha_formato = datetime.fromisoformat(ultima_fecha).strftime("%d/%m/%Y %I:%M %p")

    # Formato de entrega
    respuesta = {
        "informe": (
            "A continuación, te hacemos entrega de las estadísticas obtenidas para los datos tomados últimamente:\n\n"
            "1. Número total de predicciones realizadas por cada categoría:\n"
            + "\n".join([f"   - {clave}: {valor}" for clave, valor in conteo.items()]) + "\n\n"
            "2. Estas fueron las últimas predicciones realizadas:\n"
            + "\n".join([f"   - {linea}" for linea in ultimas_texto]) + "\n\n"
            "3. A continuación, se muestra la fecha y hora de la última predicción realizada:\n"
            f"   - {fecha_formato}\n"
        )
    }

    return jsonify(respuesta)


@app.route('/descargar-resultados', methods=['GET'])
def descargar_resultados():
    path = "resultados/predicciones.txt"
    if not os.path.exists(path):
        return jsonify({"error": "Aún no se han generado predicciones."}), 404
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
