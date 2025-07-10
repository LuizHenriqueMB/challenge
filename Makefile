# Diretório de relatórios
REPORTS_DIR=./reports

# Alvo para rodar o Gitleaks
gitleaks:
	@mkdir -p $(REPORTS_DIR)
	docker compose run --rm gitleaks

# Alvo para rodar o Bandit
bandit:
	@mkdir -p $(REPORTS_DIR)
	docker compose run --rm bandit

# Alvo para rodar o Trivy
IMAGE_NAME := challenge

trivy-image:
	docker compose run --rm trivy image $(IMAGE_NAME)

# Alvo para rodar tudo
all: bandit gitleaks trivy
