# Use a imagem oficial mais recente do Python como base
FROM python:latest

# Define o diretório de trabalho no contêiner
WORKDIR /app

#copiar os arquivos
COPY ./ /app

# Instale as dependências (se houver um arquivo requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt