FROM ubuntu:20.04
RUN apt update -y
RUN apt install -y python3-dev
RUN apt install -y build-essential
RUN apt install python3 python3-pip -y
RUN pip install flask
RUN pip install opentelemetry-distro
RUN opentelemetry-bootstrap -a install
ADD index.html index.html
ADD server.py server.py
RUN chmod 777 server.py
EXPOSE 8000
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENTRYPOINT ["opentelemetry-instrument", "--traces_exporter", "console,otlp", "--metrics_exporter", "console,otlp", "--logs_exporter", "console,otlp", "--service_name", "python-logs-example", "python3", "server.py"]
#ENTRYPOINT ["python3", "server.py"]
