## 📚 Explicando o Código

O código-fonte da aplicação `app.py` possui uma vulnerabilidade de XSS (Cross Site Scripting - Reflected) onde permite a injeção de código na aplicação web. Outro arquivo python é o `secrets_test.py` que contém secrets Keys falsas onde em ambos os casos da aplicação web é uma porta de entrada para que Agentes Maliciosos explorem essas vulnerabilidades.

---

## Decisões tomadas enquanto montava a pipeline


---

## 💻 Como Executar a pipepline

* Crie um arquivo `reports` através do comando `mkidr reports`.

* Depois para executar as ferramentas veja as instruções `como rodar as ferramentas`.

* O arquivo de configuração das ferramentas está dentro do `docker-compose.yml`.

---
## 🚀 Acessando o DefectDojo

credenciais de acesso ao DefectDojo:

usuário: `admin`
senha: `admin123`

Para rodar o DefectDojo utilize o comando: `make dojo-up`.
 
Para encerrar o DefectDojo utilize o comando: `make dojo-down`.

Para reiniciar o DefectDojo utilize o comando: `make dojo-restart`.

Para acessar o localhost utilize o comando: `explorer.exe http://localhost:8080`
---

## ⚒️ Ferramentas utilizadas até o momento 

* Gitleaks como SAST.
* Bandit para encontrar vulnerabilidades no código python.
* Trivy para encontrar vulnerabilidades como segredos e imagens Docker. 
* Makefile como o orquestrador da pipeline.
* DefecDojo como gerenciador de vulnerabilidades.

---

## 🪖 Para rodar as ferramentas 

Para rodar o `bandit` basta utilizar o comando: `docker compose up --build bandit` ou `make bandit`.

Para rodar o `gitleaks` basta utilizar o comando: `docker compose run --rm gitleaks` ou ``make gitleaks`.

Para rodar o `trivy` basta utilizar o comando: `make pipeline`.

---

## 🔍 Evidências (prints e logs de scans)

