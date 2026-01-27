# 3. Technical Assumptions

## 3.1 Repository Structure: Monorepo

**Decision:** Single repository containing all components (app, infra, CI/CD)

**Rationale:**
- Simplifies CI/CD pipeline configuration (single trigger point)
- Easier to maintain atomic commits across app + infra changes
- Appropriate for learning project (all context in one place)
- Standard pattern for small-to-medium projects

**Structure:**
```
/
├── apps/
│   ├── frontend/       # React/Next.js
│   ├── api/            # Python FastAPI
│   └── docker-compose.yaml
├── infra/
│   ├── terraform/      # Azure resources
│   └── helm/           # Helm charts
│       ├── frontend/
│       ├── api/
│       ├── postgres/
│       └── helmfile.yaml
├── .github/
│   └── workflows/      # GitHub Actions
├── docs/               # Documentation, diagrams
└── README.md
```

## 3.2 Service Architecture: Containerized Microservices (3-tier)

| Service | Technology | Role |
|---------|------------|------|
| Frontend | React/Next.js | Static/SSR web interface |
| API | Python FastAPI | Business logic, REST endpoints |
| Database | PostgreSQL | Persistent data storage |

## 3.3 Testing Requirements: Unit + Integration (Pragmatic)

| Level | Scope | Implementation |
|-------|-------|----------------|
| Unit Tests | API endpoints, business logic | pytest for Python |
| Integration Tests | API ↔ Database | pytest with test containers |
| Smoke Tests | Deployed application | curl/httpie in CI pipeline |
| Infrastructure Tests | Terraform validation | `terraform validate`, `terraform plan` |
| Helm Tests | Chart validation | `helm lint`, `helm template` |

## 3.4 Additional Technical Assumptions

**Kubernetes:**
- Local cluster: Kind (preferred over Minikube - lighter, CI-compatible)
- K8s version: Latest stable (1.28+)
- Namespace strategy: `dev` and `prod` namespaces in same cluster (for learning)

**Container Registry:**
- Azure Container Registry (ACR): Basic tier (free tier eligible)
- Image tagging: Semantic versioning + git SHA for traceability

**CI/CD:**
- Platform: GitHub Actions (native, free for public repos)
- Environments: GitHub Environments for dev/prod with protection rules
- Secrets: GitHub Secrets for sensitive values (Azure credentials)

**Terraform:**
- Version: 1.5+ (latest stable)
- Backend: Azure Storage Account (azurerm backend)
- Provider: azurerm (latest)
- State locking: Enabled via Azure Blob lease

**Helm:**
- Version: 3.x (Helm 2 is deprecated)
- Helmfile: For multi-chart orchestration
- Chart sources: Bitnami (PostgreSQL), Prometheus Community (monitoring stack)

**Observability Stack:**
- Metrics: Prometheus + Grafana (kube-prometheus-stack Helm chart)
- Logs: Loki + Promtail (Grafana Loki Helm chart)
- Dashboards: Pre-built + custom for API metrics

**Networking:**
- Ingress: NGINX Ingress Controller
- TLS: cert-manager with Let's Encrypt (or self-signed for local)
- DNS: nip.io or local /etc/hosts for development

**Security:**
- Container user: Non-root (UID 1000)
- Image scanning: Trivy in CI pipeline
- Secrets encryption: Azure Key Vault with CSI Driver

---
