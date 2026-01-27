# 5. Epic 1: Foundation & Local Development

**Goal:** Establish the complete project foundation with a working 3-tier application. This epic delivers a containerized application running both via docker-compose (for development) and on a local Kubernetes cluster (Kind) with basic Helm charts. The foundation must be solid enough to build CI/CD and observability on top.

## Story 1.1: Project Repository Setup

**As a** DevOps engineer,
**I want** a well-structured monorepo with all necessary directories and configuration files,
**so that** I have a solid foundation to build the application and infrastructure components.

**Acceptance Criteria:**
1. GitHub repository is initialized with `.gitignore` for Python, Node.js, Terraform, and IDE files
2. Directory structure follows the agreed pattern (`apps/`, `infra/`, `.github/`, `docs/`)
3. Root `README.md` documents project purpose, structure, and getting started guide
4. `.editorconfig` ensures consistent formatting across editors
5. Pre-commit hooks are configured for basic linting (optional but recommended)

## Story 1.2: Python API Service with Health Endpoint

**As a** DevOps engineer,
**I want** a Python FastAPI service with a health check endpoint,
**so that** I have a backend service ready for containerization and Kubernetes probes.

**Acceptance Criteria:**
1. FastAPI application is created in `apps/api/`
2. `/health` endpoint returns `{"status": "healthy"}` with 200 OK
3. `/ready` endpoint checks database connectivity (returns 503 if unavailable)
4. Basic project structure with `requirements.txt` or `pyproject.toml`
5. Application runs locally with `uvicorn` on port 8000
6. Unit tests exist for health endpoints using pytest
7. `README.md` documents how to run the API locally

## Story 1.3: PostgreSQL Database Setup

**As a** DevOps engineer,
**I want** a PostgreSQL database with initial schema,
**so that** the API can persist and retrieve data.

**Acceptance Criteria:**
1. Database initialization script exists in `apps/api/db/` or `infra/db/`
2. Schema includes at least one table (e.g., `items` with id, name, created_at)
3. API connects to PostgreSQL using environment variables for configuration
4. API has a simple CRUD endpoint (e.g., `GET/POST /items`) to validate DB connectivity
5. Database connection is properly pooled and handles reconnection
6. Integration test validates API ↔ Database communication

## Story 1.4: React/Next.js Frontend Service

**As a** DevOps engineer,
**I want** a simple React/Next.js frontend that calls the API,
**so that** I have a complete 3-tier application to deploy.

**Acceptance Criteria:**
1. Next.js application is created in `apps/frontend/`
2. Homepage displays data fetched from the API `/items` endpoint
3. Environment variable configures API URL (`NEXT_PUBLIC_API_URL`)
4. Application runs locally with `npm run dev` on port 3000
5. Basic styling is applied (minimal, portfolio-presentable)
6. `README.md` documents how to run the frontend locally

## Story 1.5: Docker Containerization

**As a** DevOps engineer,
**I want** optimized Dockerfiles for each service,
**so that** the application can run consistently across environments.

**Acceptance Criteria:**
1. Multi-stage Dockerfile for API minimizes image size (builder + runtime stages)
2. Multi-stage Dockerfile for Frontend (build + nginx/node serve)
3. Both images run as non-root user (UID 1000)
4. Images are tagged with version (e.g., `api:0.1.0`)
5. `.dockerignore` files exclude unnecessary files from build context
6. Images build successfully with `docker build` command
7. Image sizes are reasonable (API < 200MB, Frontend < 100MB)

## Story 1.6: Docker Compose Local Stack

**As a** DevOps engineer,
**I want** a docker-compose configuration that runs all services together,
**so that** I can develop and test the complete stack locally.

**Acceptance Criteria:**
1. `docker-compose.yaml` defines all three services (api, frontend, postgres)
2. Services are connected via Docker network
3. PostgreSQL data persists via named volume
4. Environment variables are managed via `.env` file (with `.env.example` template)
5. `docker-compose up` starts all services successfully
6. Frontend can reach API, API can reach Database
7. Health checks are defined for each service
8. `docker-compose down -v` cleanly removes all resources

## Story 1.7: Kind Cluster Setup

**As a** DevOps engineer,
**I want** a local Kubernetes cluster using Kind,
**so that** I can deploy and test Kubernetes manifests locally.

**Acceptance Criteria:**
1. Kind cluster configuration file exists in `infra/kind/`
2. Cluster is created with `kind create cluster` command
3. `kubectl` context is configured to use the Kind cluster
4. Cluster has at least 1 control plane and 1 worker node (or single node for simplicity)
5. Cluster configuration enables Ingress support (extra port mappings)
6. Documentation explains how to create/delete the cluster
7. Script or Makefile target automates cluster creation

## Story 1.8: Kubernetes Manifests for Application

**As a** DevOps engineer,
**I want** Kubernetes manifests to deploy the application to Kind,
**so that** I understand the fundamental K8s resources before using Helm.

**Acceptance Criteria:**
1. Deployment manifests exist for API and Frontend
2. StatefulSet manifest exists for PostgreSQL (or Deployment with PVC)
3. Service manifests expose each component (ClusterIP)
4. ConfigMaps manage non-sensitive configuration
5. Secrets manage database credentials (base64 encoded)
6. Resource requests and limits are defined for all containers
7. Liveness and readiness probes are configured for API
8. All resources are namespaced (e.g., `devops-demo` namespace)
9. `kubectl apply -k` or `kubectl apply -f` deploys the entire stack
10. Application is accessible via `kubectl port-forward`

## Story 1.9: Basic Helm Charts

**As a** DevOps engineer,
**I want** the application packaged as Helm charts,
**so that** I can manage deployments declaratively with customizable values.

**Acceptance Criteria:**
1. Helm chart exists for API (`infra/helm/api/`)
2. Helm chart exists for Frontend (`infra/helm/frontend/`)
3. Helm chart exists for PostgreSQL (or use Bitnami subchart)
4. Each chart has `values.yaml` with configurable parameters (image, replicas, resources)
5. `values-dev.yaml` and `values-prod.yaml` demonstrate environment-specific config
6. Charts pass `helm lint` validation
7. Charts can be installed with `helm install` command
8. Charts include NOTES.txt with post-install instructions
9. Helmfile.yaml orchestrates all charts together
10. `helmfile sync` deploys the complete stack to Kind

---
