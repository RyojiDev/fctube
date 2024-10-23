# Usar a imagem oficial do Python 3.12.6
FROM python:3.12.6-slim

# Instalar pipenv
RUN pip install --no-cache-dir pipenv

# Defina a variável de ambiente PATH
ENV PATH="$HOME/.local/bin:$PATH"

# Crie um diretório para o projeto
WORKDIR /app

# Copie o arquivo requirements.txt (se houver) para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto, se houver um requirements.txt
# Caso contrário, essa linha pode ser removida
RUN pipenv install --skip-lock

EXPOSE 8000

# Copie o restante do código para o contêiner
COPY . .

# Comando padrão ao iniciar o contêiner
CMD ["bash"]
