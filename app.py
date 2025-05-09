from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predecir', methods=['POST'])
def predecir():
    datos = request.json
    edad = datos.get('edad')
    fiebre = datos.get('fiebre')
    dolor = datos.get('dolor')

    if edad not in range(0, 121):
        return jsonify({'error': 'Edad fuera de rango permitido'}), 400
    if fiebre not in [True, False]:
        return jsonify({'error': 'Valor de fiebre inválido'}), 400
    if dolor not in range(0, 11):
        return jsonify({'error': 'Nivel de dolor fuera de rango'}), 400

    if edad < 30 and dolor < 3 and not fiebre:
        resultado = "NO ENFERMO"
    elif dolor < 5:
        resultado = "ENFERMEDAD LEVE"
    elif fiebre and dolor >= 5:
        resultado = "ENFERMEDAD AGUDA"
    else:
        resultado = "ENFERMEDAD CRÓNICA"

    return jsonify({'diagnostico': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
