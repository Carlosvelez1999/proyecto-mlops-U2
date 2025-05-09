from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Lista para guardar historial de predicciones
historial = []

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

    # Guardar predicción con fecha
    historial.append({
        "diagnostico": resultado,
        "fecha": datetime.now().isoformat()
    })

    return jsonify({'diagnostico': resultado})


@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    total = len(historial)
    ultimas = historial[-5:] if total > 0 else []
    ultima_fecha = ultimas[-1]['fecha'] if ultimas else None

    return jsonify({
        "total_predicciones": total,
        "ultimas_5_predicciones": ultimas,
        "fecha_ultima_prediccion": ultima_fecha
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
