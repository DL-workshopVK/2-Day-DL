#Stage 1: Build

FROM python:3.9-slim as builder

#install system dependencies
RUN apt-get update &&\
    apt-get install -y --no-install-recommends gcc python3-dev &&\
    rm -rf /var/lib/apt/lists/

#install python dependencies
COPY req_production.txt .
RUN pip install --user -r req_production.txt

#STAGE 2 :Final
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

#Set Evnvironment Variables:
ENV PATH = /root/.local/bin:$PATH
ENV STREAMLIT_SERVER_PORT = 8501

#Expose Port:
EXPOSE 8501

#Run Application:
CMD ["streamlit","run","webapp/app.py","--server.port=8501", "--server.address=0.0.0.0"]