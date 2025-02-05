FROM python:3

WORKDIR .

COPY ./ ./

RUN chmod +x entrypoint.sh

RUN pip install paho-mqtt

RUN python -c "import paho.mqtt.client; print('paho-mqtt is installed')"

CMD ["./entrypoint.sh"]

