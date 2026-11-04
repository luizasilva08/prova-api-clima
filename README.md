# PROVA API CLIMA

# Tecnologias utilizadas:
- VS CODE
- Python
- Postman
- Git

# Principais bibliotecas do Python utilizadas:
- Requests
- Streamlit
- e mais outras no requirements.txt
 
# Passo a Passo:
- Criação de uma venv (opcional)
- Instalar as bibliotecas (python -m pip install -r requirements.txt)
- Criação do código de consumo da API da Open Meteo (https://api.open-meteo.com/v1/forecast?latitude=-26.4861&longitude=-49.0667&current=temperature_2m,relative_humidity_2m,precipitation,apparent_temperature,wind_speed_10m&timezone=America%2FSao_Paulo&forecast_days=1)
- Tratar o código conforme as variavéis que precise (variavel = ["dados"]["current"]["variavel"]).
- Criação do Streamlit e adaptação conforme as necessidades do código de consumo.
- Testes no terminal e com o Postman.
