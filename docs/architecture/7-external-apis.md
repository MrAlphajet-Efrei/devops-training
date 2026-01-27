# 7. External APIs

| Service | Purpose | Auth Method | Used By |
|---------|---------|-------------|---------|
| **Azure ACR** | Container images | Service Principal | GitHub Actions, K8s |
| **Azure Key Vault** | Secrets storage | Service Principal / CSI | API pods |
| **Azure Storage** | Terraform state | Service Principal | Terraform |
| **Azure ARM** | Resource provisioning | Service Principal | Terraform |
| **Let's Encrypt** | TLS certificates | ACME account | cert-manager |
| **GitHub API** | CI/CD automation | GITHUB_TOKEN | GitHub Actions |
| **Docker Hub** | Base images | Anonymous | Docker builds |

## 7.1 Azure Container Registry

- **Base URL:** `https://{registry-name}.azurecr.io`
- **Authentication:** Service Principal or `az acr login`
- **Rate Limits:** Basic SKU: 10 pulls/minute

## 7.2 Azure Key Vault

- **Base URL:** `https://{vault-name}.vault.azure.net`
- **Authentication:** Service Principal with access policy
- **Key Endpoints:** `GET /secrets/{name}`, `PUT /secrets/{name}`

## 7.3 Let's Encrypt ACME

- **Staging URL:** `https://acme-staging-v02.api.letsencrypt.org/directory`
- **Production URL:** `https://acme-v02.api.letsencrypt.org/directory`
- **Rate Limits:** 50 certs/week per domain (production)

---
