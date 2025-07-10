FROM python:3.8-slim

WORKDIR /src

# Install flask via requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE port 5000
EXPOSE 5000

# Install bandit
RUN pip install Bandit --no-cache-dir

COPY . . /src/
# comando para rodar o bandit
CMD ["bandit", "-r", "/src/"]
