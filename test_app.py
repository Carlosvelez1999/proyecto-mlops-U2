import requests

def test_prediccion_terminal():
    response = requests.post("http://localhost:5000/predecir", json={
        "edad": 80,
        "fiebre": True,
        "dolor": 9
    })
    assert response.status_code == 200
    assert response.json()["diagnostico"] == "ENFERMEDAD TERMINAL"

def test_estadisticas_formato():
    response = requests.get("http://localhost:5000/estadisticas")
    assert response.status_code == 200
    assert "total_predicciones" in response.json()