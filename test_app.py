from app import app

def test_prediccion_terminal():
    client = app.test_client()
    response = client.post('/predecir', json={
        "edad": 80,
        "fiebre": True,
        "dolor": 9
    })
    assert response.status_code == 200
    assert response.get_json()["diagnostico"] == "ENFERMEDAD TERMINAL"

import json

def test_estadisticas_formato():
    client = app.test_client()
    response = client.get('/estadisticas')
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert "A continuación" in data["informe"]
    assert "Número total de predicciones realizadas" in data["informe"]



