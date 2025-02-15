FROM python:3.9-slim
WORKDIR /app

# Copia i requisiti e installa le dipendenze
COPY ./actuators/requirements.txt .
RUN pip install -r requirements.txt

# Copia il codice degli attuatori
COPY ./actuators/ .

# Copia il file di configurazione dell'ambiente
COPY ./simulated_env/env.json /app/env/env.json

# Comando di avvio
CMD ["python", "act.py"]