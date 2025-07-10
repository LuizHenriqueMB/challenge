# Diretório de relatórios
REPORTS_DIR=./reports
# Nome da imagem Docker da aplicação para escaneamento
IMAGE_NAME := challenge

# Evita repetição de mkdir em cada alvo individual
prepare:
	@mkdir -p $(REPORTS_DIR)

# Gitleaks - Escaneia segredos no repositório
gitleaks: prepare
	docker compose run --rm gitleaks || true

# Bandit - Verificação de vulnerabilidades no código Python
bandit: prepare
	docker compose run --rm bandit || true

# Build da imagem da aplicação para análise com Trivy
build:
	docker build -t $(IMAGE_NAME) .

# Trivy - Escaneia vulnerabilidades na imagem Docker
trivy: prepare build
	docker compose run --rm trivy trivy image --format json --output /reports/trivy-report.json challenge || true

# upload_scans
upload_scans: 
	python3 scripts/upload_scans.py

# Alvo completo: roda todas as ferramentas de segurança na sequência
all: bandit gitleaks trivy upload_scans