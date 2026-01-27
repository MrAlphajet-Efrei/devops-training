# 12. Unified Project Structure

```
devops-learning-project/
├── .github/
│   └── workflows/
│       ├── ci.yaml              # Build & test on PR
│       ├── cd.yaml              # Build, push, deploy on main
│       └── terraform.yaml       # Infrastructure changes
│
├── apps/
│   ├── frontend/                # Next.js application
│   │   ├── src/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   └── README.md
│   ├── api/                     # FastAPI application
│   │   ├── src/
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── docker-compose.yaml      # Local development
│
├── infra/
│   ├── terraform/
│   │   ├── environments/
│   │   │   ├── dev/
│   │   │   └── prod/
│   │   ├── modules/
│   │   │   ├── acr/
│   │   │   ├── keyvault/
│   │   │   ├── storage/
│   │   │   └── aks/
│   │   └── backend.tf
│   ├── helm/
│   │   ├── charts/
│   │   │   ├── api/
│   │   │   ├── frontend/
│   │   │   └── postgres/
│   │   ├── environments/
│   │   └── helmfile.yaml
│   ├── kind/
│   │   └── cluster-config.yaml
│   └── grafana/
│       └── dashboards/
│
├── scripts/
│   ├── setup-local.sh
│   ├── create-kind-cluster.sh
│   └── port-forward.sh
│
├── docs/
│   ├── prd.md
│   ├── architecture.md
│   └── setup-guide.md
│
├── .env.example
├── .gitignore
├── .editorconfig
├── Makefile
└── README.md
```

---
