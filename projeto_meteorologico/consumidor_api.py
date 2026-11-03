import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-26.4861&longitude=-49.0667&current=temperature_2m,relative_humidity_2m,precipitation,apparent_temperature,wind_speed_10m&timezone=America%2FSao_Paulo&forecast_days=1"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    tempo = dados["current"]["time"]
    umidade = dados["current"]["relative_humidity_2m"]
    temperatura = dados["current"]["temperature_2m"]
    sensacao = dados["current"]["apparent_temperature"]
    precipitacao = dados["current"]["precipitation"]
    vento = dados["current"]["wind_speed_10m"]

    print(f"Tempos registrados: {tempo} ")
    print(f"Temperatura: {temperatura} °C")
    print(f"Umidade: {umidade} %")
    print(f"Sensação térmica: {sensacao}")
    print(f"Precipitação: {precipitacao}")
    print(f"Velocidade do vento: {vento} ")

else:
    print("Requisição não feita.")