# 13. Development Workflow

## 13.1 Prerequisites

```bash
docker --version          # >= 24.0.0
node --version            # >= 20.0.0
python --version          # >= 3.11.0
kubectl version --client  # >= 1.28.0
helm version              # >= 3.13.0
terraform --version       # >= 1.5.0
kind version              # >= 0.20.0
```

## 13.2 Initial Setup

```bash
# Clone and setup
git clone https://github.com/YOUR_USERNAME/devops-learning-project.git
cd devops-learning-project
cp .env.example .env

# Install dependencies
cd apps/api && poetry install && cd ../..
cd apps/frontend && npm install && cd ../..

# Start local development
make dev

# Verify
curl http://localhost:8000/health
curl http://localhost:3000
```

## 13.3 Common Commands

```bash
# Local development
make dev                  # Start docker-compose
make dev-down             # Stop docker-compose
make test                 # Run all tests
make lint                 # Lint all code

# Kind cluster
make kind-up              # Create Kind cluster
make kind-down            # Delete Kind cluster
make deploy-local         # Deploy to Kind

# Terraform
make tf-init              # Initialize Terraform
make tf-plan              # Plan changes
make tf-apply             # Apply changes
```

## 13.4 Environment Variables

```bash
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=devops_demo
DB_USER=app_user
DB_PASSWORD=your_secure_password

# API
API_DEBUG=true
API_LOG_LEVEL=INFO

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000

# Azure (for Terraform & CI/CD)
ARM_CLIENT_ID=
ARM_CLIENT_SECRET=
ARM_SUBSCRIPTION_ID=
ARM_TENANT_ID=
```

---
