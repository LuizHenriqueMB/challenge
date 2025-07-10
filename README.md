## 📚 Explicando o Código

O código-fonte da aplicação `app.py` possui uma vulnerabilidade de XSS (Cross Site Scripting - Reflected) onde permite a injeção de código na aplicação web. Outro arquivo python é o `secrets_test.py` que contém secrets Keys falsas onde em ambos os casos da aplicação web é uma porta de entrada para que Agentes Maliciosos explorem essas vulnerabilidades.

---

## ⚒️ Ferramentas utilizadas até o momento 

* Gitleaks como SAST
* Bandit 
* Trivy
* SonarQube como SAST 
* Makefile como o Oquestrador da pipeline
---

## 🪖 Para rodar as ferramentas 

Para rodar o `bandit` basta utilizar o comando: `docker compose up --build bandit` ou `make security`

Para rodar o `gitleaks` basta utilizar o comando: `docker compose run --rm gitleaks` ou ``make gitleaks`

Para rodar o `trivy` basta utilizar o comando: `docker compose run --rm trivy image $(IMAGE_NAME)` 