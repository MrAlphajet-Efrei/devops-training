# DevOps Learning Project

A full-stack application built with production-grade DevOps practices, designed as a hands-on learning platform for containerization, orchestration, infrastructure-as-code, and CI/CD pipelines.

## Project Goals

This project implements a complete DevOps lifecycle covering:

- **G1**: Containerized application deployment with Docker
- **G2**: Kubernetes orchestration (local Kind + cloud AKS)
- **G3**: Infrastructure-as-Code with Terraform
- **G4**: Kubernetes packaging with Helm + Helmfile
- **G5**: CI/CD automation with GitHub Actions
- **G6**: Monitoring and observability (Prometheus + Grafana)
- **G7**: Centralized logging (Loki + Promtail)
- **G8**: Secret management and security best practices
- **G9**: Production-grade deployment patterns

## Architecture Overview

Three-tier architecture:

```
[Next.js Frontend] --> [FastAPI Backend] --> [PostgreSQL Database]
```

- **Frontend**: Next.js (TypeScript) with Tailwind CSS
- **Backend**: Python FastAPI REST API
- **Database**: PostgreSQL with structured data persistence
- **Infrastructure**: Kubernetes (Kind local / AKS cloud) managed via Terraform and Helm

## Tech Stack

| Category      | Technology            | Version               |
| ------------- | --------------------- | --------------------- |
| Frontend      | Next.js (TypeScript)  | 14.x                  |
| UI Styling    | Tailwind CSS          | 3.x                   |
| Backend       | Python FastAPI        | 0.109+                |
| Database      | PostgreSQL            | 15.x                  |
| Container     | Docker                | 24.x                  |
| Orchestration | Kubernetes (Kind/AKS) | 1.28+                 |
| IaC           | Terraform             | 1.5+                  |
| K8s Packaging | Helm + Helmfile       | 3.x / 0.158+          |
| CI/CD         | GitHub Actions        | -                     |
| Monitoring    | Prometheus + Grafana  | kube-prometheus-stack  |
| Logging       | Loki + Promtail       | loki-stack             |

## Project Structure

```
devops-learning-project/
├── .github/
│   └── workflows/          # CI/CD pipeline definitions
├── apps/
│   ├── frontend/           # Next.js application
│   └── api/                # FastAPI application
├── infra/
│   ├── terraform/          # Infrastructure-as-Code
│   │   ├── environments/   # Environment-specific configs
│   │   └── modules/        # Reusable Terraform modules
│   ├── helm/               # Kubernetes package definitions
│   │   ├── charts/         # Helm charts
│   │   └── environments/   # Environment value overrides
│   ├── kind/               # Local Kubernetes cluster config
│   └── grafana/
│       └── dashboards/     # Grafana dashboard JSON
├── scripts/                # Utility scripts
├── docs/                   # Project documentation
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
├── .editorconfig           # Editor formatting config
├── Makefile                # Development task runner
└── README.md               # This file
```

## Getting Started

### Prerequisites

Ensure the following tools are installed:

- **Git** 2.x+
- **Docker** 24.x+ with Docker Compose
- **Node.js** 18.x+ (for frontend)
- **Python** 3.11+ (for backend)
- **Terraform** 1.5+ (for infrastructure)
- **Helm** 3.x (for Kubernetes packaging)
- **Kind** (for local Kubernetes cluster)
- **Make** (optional, for task runner)

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd devops-learning-project

# Copy environment variables
cp .env.example .env

# Start local development environment
make dev

# Run tests
make test

# See all available commands
make help
```

## Development

Local development uses Docker Compose to run all services:

```bash
# Start all services (frontend, api, database)
make dev

# Stop all services
docker compose down

# Rebuild and restart
docker compose up --build
```

## Documentation

Additional documentation is available in the `docs/` directory:

- [Project Requirements (PRD)](docs/prd.md)
- [Architecture Documentation](docs/architecture.md)
- [Setup Guide](docs/setup-guide.md)
