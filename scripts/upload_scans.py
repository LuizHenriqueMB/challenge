import requests
import os

# === CONFIGURAÇÕES ===
BASE_URL = "http://localhost:8080/api/v2"
API_TOKEN = "c80c3509baf3cfcebf5edebe0b91b13957cd6e92"  
HEADERS = {
    "Authorization": f"Token {API_TOKEN}"
}

PRODUCT_NAME = "DevSecOps PoC"
ENGAGEMENT_NAME = "CI/CD Scans"
PRODUCT_ID = None
ENGAGEMENT_ID = None

def get_or_create_product():
    global PRODUCT_ID
    res = requests.get(f"{BASE_URL}/products/", headers=HEADERS, params={"name": PRODUCT_NAME})

    if res.status_code != 200:
        print(f"[-] Erro ao buscar produto: {res.status_code} - {res.text}")
        return

    data = res.json()
    results = data.get("results", [])

    if results:
        PRODUCT_ID = results[0].get("id")
        print(f"[+] Produto encontrado: {PRODUCT_NAME} (ID: {PRODUCT_ID})")
    else:
        payload = {
            "name": PRODUCT_NAME,
            "description": "Criado via API",
            "prod_type": 1  # obrigatório para criação
        }
        res = requests.post(f"{BASE_URL}/products/", headers=HEADERS, json=payload)

        print(f"[DEBUG] Status criação produto: {res.status_code}")
        print(f"[DEBUG] Resposta criação produto: {res.text}")

        if res.status_code == 201:
            data = res.json()
            PRODUCT_ID = data.get("id")
            if PRODUCT_ID is None:
                print(f"[-] ID do produto não encontrado na resposta.")
            else:
                print(f"[+] Produto criado: {PRODUCT_NAME} (ID: {PRODUCT_ID})")
        else:
            print(f"[-] Falha ao criar produto. Código: {res.status_code}")

def get_or_create_engagement():
    global ENGAGEMENT_ID
    res = requests.get(f"{BASE_URL}/engagements/", headers=HEADERS, params={"name": ENGAGEMENT_NAME})

    if res.status_code != 200:
        print(f"[-] Erro ao buscar engagement: {res.status_code} - {res.text}")
        return

    data = res.json()
    results = data.get("results", [])

    if results:
        ENGAGEMENT_ID = results[0].get("id")
        print(f"[+] Engagement encontrado: {ENGAGEMENT_NAME} (ID: {ENGAGEMENT_ID})")
    else:
        payload = {
            "product": PRODUCT_ID,
            "name": ENGAGEMENT_NAME,
            "target_start": "2025-07-10",
            "target_end": "2025-07-30",
            "status": "In Progress"
        }
        res = requests.post(f"{BASE_URL}/engagements/", headers=HEADERS, json=payload)

        print(f"[DEBUG] Status criação engagement: {res.status_code}")
        print(f"[DEBUG] Resposta criação engagement: {res.text}")

        if res.status_code == 201:
            data = res.json()
            ENGAGEMENT_ID = data.get("id")
            if ENGAGEMENT_ID is None:
                print(f"[-] ID do engagement não encontrado na resposta.")
            else:
                print(f"[+] Engagement criado: {ENGAGEMENT_NAME} (ID: {ENGAGEMENT_ID})")
        else:
            print(f"[-] Falha ao criar engagement. Código: {res.status_code}")

def upload_scan(scan_type, path):
    with open(path, "rb") as f:
        files = {"file": (os.path.basename(path), f)}
        data = {
            "scan_type": scan_type,
            "engagement": ENGAGEMENT_ID,
            "active": "true",
            "verified": "false"
        }
        res = requests.post(f"{BASE_URL}/import-scan/", headers=HEADERS, files=files, data=data)
        if res.status_code == 201 or res.status_code == 200:
            print(f"[+] {scan_type} enviado com sucesso: {res.status_code}")
        else:
            print(f"[-] Falha ao enviar {scan_type}: {res.status_code} - {res.text}")

def main():
    get_or_create_product()
    if PRODUCT_ID is None:
        print("[-] Produto não definido, abortando.")
        return

    get_or_create_engagement()
    if ENGAGEMENT_ID is None:
        print("[-] Engagement não definido, abortando.")
        return

    scans = {
        "Bandit Scan": "./reports/bandit-report.json",
        "Gitleaks Scan": "./reports/gitleaks-report.json",
        "Trivy Scan": "./reports/trivy-report.json"
    }

    for scan_type, file_path in scans.items():
        if os.path.exists(file_path):
            upload_scan(scan_type, file_path)
        else:
            print(f"[-] Arquivo não encontrado: {file_path}")

if __name__ == "__main__":
    main()
