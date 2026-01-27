# DevOps Full-Chain Learning Project - Product Requirements Document (PRD)

**Version:** 1.0
**Status:** Draft
**Last Updated:** 2025-01-25

---

## 1. Goals and Background Context

### 1.1 Goals

- **G1:** Deploy a complete 3-tier application (Frontend + API + DB) to Kubernetes from scratch
- **G2:** Implement production-grade observability with metrics (Prometheus/Grafana) and centralized logging (Loki)
- **G3:** Automate infrastructure provisioning with Terraform (Azure resources, remote state, modules)
- **G4:** Build a complete CI/CD pipeline with GitHub Actions covering build, test, push, and deployment stages
- **G5:** Package and manage applications using Helm charts (custom + community)
- **G6:** Configure Kubernetes networking (Services, Ingress, TLS) following production best practices
- **G7:** Implement secrets management progressively (K8s Secrets → Azure Key Vault)
- **G8:** Gain hands-on experience with Azure cloud provider (ACR, Key Vault, bonus AKS)
- **G9:** Build a portfolio-ready project demonstrating full DevOps chain mastery as foundation for MLOps transition

### 1.2 Background Context

This project addresses a specific skills gap: transitioning from a fullstack-heavy background with limited DevOps exposure to a production-ready DevOps skillset, ultimately preparing for MLOps/GenAI roles.

The participant has 3 years of professional experience but predominantly in fullstack development, with only one deployment participation and 2 years without active DevOps practice. The current knowledge state shows theoretical understanding (level B) for deployment but significant gaps (level C) in monitoring, infrastructure automation, CI/CD deployment stages, and production best practices.

The chosen approach—"Full Chain Progressive"—builds skills layer by layer over 7 days, with each day delivering a concrete, deployable increment. The stack is intentionally MLOps-ready: Python API (FastAPI pathway), metrics-first observability (critical for ML model monitoring), and cloud-native patterns (containers, orchestration, IaC).

### 1.3 Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2025-01-25 | 1.0 | Initial PRD based on brainstorming session | PM John |

---

## 2. Requirements

### 2.1 Functional Requirements

**Application & Containerization:**
- **FR1:** The system shall include a 3-tier application with React/Next.js frontend, Python (FastAPI) API, and PostgreSQL database
- **FR2:** Each application component shall be containerized with optimized, multi-stage Dockerfiles
- **FR3:** The application shall run locally via docker-compose for development validation

**Kubernetes Deployment:**
- **FR4:** The application shall be deployable to a local Kubernetes cluster (Kind or Minikube)
- **FR5:** Each application component shall have dedicated Kubernetes manifests (Deployment, Service, ConfigMap)
- **FR6:** The API shall implement health check endpoints (liveness and readiness probes)

**Helm Packaging:**
- **FR7:** The application shall be packaged as custom Helm charts (one chart per component or umbrella chart)
- **FR8:** Helm charts shall support multiple environments via values files (dev, prod)
- **FR9:** Community Helm charts shall be used for infrastructure components (Prometheus, Grafana, Loki)
- **FR10:** Helmfile shall orchestrate multi-chart deployments

**CI/CD Pipeline:**
- **FR11:** GitHub Actions shall automate the build process (lint, test, Docker build)
- **FR12:** The pipeline shall push container images to Azure Container Registry (ACR)
- **FR13:** The pipeline shall automatically deploy to dev environment on successful build
- **FR14:** The pipeline shall require manual approval for production deployment
- **FR15:** The pipeline shall include Terraform plan/apply stages for infrastructure changes

**Infrastructure as Code:**
- **FR16:** Terraform shall provision Azure resources (ACR, Storage Account, Key Vault)
- **FR17:** Terraform state shall be stored remotely in Azure Storage Account
- **FR18:** Terraform code shall be organized in reusable modules
- **FR19:** Terraform shall support multi-environment configuration (dev, prod)

**Observability:**
- **FR20:** Prometheus shall collect metrics from all application components and Kubernetes
- **FR21:** Grafana shall provide dashboards for application and infrastructure metrics
- **FR22:** Loki shall aggregate logs from all application components
- **FR23:** Grafana shall integrate with Loki for log querying and visualization

**Networking:**
- **FR24:** NGINX Ingress Controller shall route external traffic to services
- **FR25:** TLS certificates shall be automatically provisioned via cert-manager
- **FR26:** Services shall use appropriate types (ClusterIP for internal, Ingress for external)

**Secrets Management:**
- **FR27:** Initial deployment shall use Kubernetes native Secrets
- **FR28:** Production deployment shall integrate Azure Key Vault via CSI Driver
- **FR29:** Secrets shall never be committed to version control

**Bonus - Cloud Deployment:**
- **FR30:** (Bonus) Application shall be deployable to Azure Kubernetes Service (AKS)
- **FR31:** (Bonus) Azure Monitor shall provide cloud-native observability comparison

### 2.2 Non-Functional Requirements

**Cost Constraints:**
- **NFR1:** Azure resource usage shall stay within free tier + 200$ new account credits
- **NFR2:** AKS cluster (if used) shall be minimal (1-2 nodes, B2s size) and short-lived

**Security:**
- **NFR3:** Container images shall not run as root user
- **NFR4:** Sensitive configuration shall be managed via Secrets, not ConfigMaps
- **NFR5:** HTTPS shall be enforced for all external endpoints

**Quality & Best Practices:**
- **NFR6:** All configurations shall follow Kubernetes production best practices (resource limits, probes, etc.)
- **NFR7:** Terraform code shall pass `terraform validate` and `terraform fmt` checks
- **NFR8:** Helm charts shall pass `helm lint` validation
- **NFR9:** CI/CD pipeline shall include security scanning (container image scanning)

**Documentation:**
- **NFR10:** Each major component shall have a README documenting setup and usage
- **NFR11:** The project shall include architecture diagrams for portfolio presentation

**Learning Outcomes:**
- **NFR12:** Each requirement shall be implemented by the learner (not copied) to ensure skill acquisition
- **NFR13:** Implementation decisions shall be documented with rationale for future reference

---

## 3. Technical Assumptions

### 3.1 Repository Structure: Monorepo

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

### 3.2 Service Architecture: Containerized Microservices (3-tier)

| Service | Technology | Role |
|---------|------------|------|
| Frontend | React/Next.js | Static/SSR web interface |
| API | Python FastAPI | Business logic, REST endpoints |
| Database | PostgreSQL | Persistent data storage |

### 3.3 Testing Requirements: Unit + Integration (Pragmatic)

| Level | Scope | Implementation |
|-------|-------|----------------|
| Unit Tests | API endpoints, business logic | pytest for Python |
| Integration Tests | API ↔ Database | pytest with test containers |
| Smoke Tests | Deployed application | curl/httpie in CI pipeline |
| Infrastructure Tests | Terraform validation | `terraform validate`, `terraform plan` |
| Helm Tests | Chart validation | `helm lint`, `helm template` |

### 3.4 Additional Technical Assumptions

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

## 4. Epic List

| Epic | Title | Goal | Days |
|------|-------|------|------|
| **Epic 1** | Foundation & Local Development | Establish project structure, containerized app running locally with docker-compose and initial Kubernetes deployment | J1, J3 (partial) |
| **Epic 2** | Infrastructure as Code & CI/CD | Provision Azure resources with Terraform, deploy to K8s via Helm, automate with GitHub Actions | J2, J3 (partial), J4 |
| **Epic 3** | Observability Stack | Implement production-grade monitoring (Prometheus/Grafana) and centralized logging (Loki) | J5 |
| **Epic 4** | Production Hardening & Cloud | Configure networking (Ingress, TLS), migrate to Azure Key Vault, bonus AKS deployment | J6, J7 |

---

## 5. Epic 1: Foundation & Local Development

**Goal:** Establish the complete project foundation with a working 3-tier application. This epic delivers a containerized application running both via docker-compose (for development) and on a local Kubernetes cluster (Kind) with basic Helm charts. The foundation must be solid enough to build CI/CD and observability on top.

### Story 1.1: Project Repository Setup

**As a** DevOps engineer,
**I want** a well-structured monorepo with all necessary directories and configuration files,
**so that** I have a solid foundation to build the application and infrastructure components.

**Acceptance Criteria:**
1. GitHub repository is initialized with `.gitignore` for Python, Node.js, Terraform, and IDE files
2. Directory structure follows the agreed pattern (`apps/`, `infra/`, `.github/`, `docs/`)
3. Root `README.md` documents project purpose, structure, and getting started guide
4. `.editorconfig` ensures consistent formatting across editors
5. Pre-commit hooks are configured for basic linting (optional but recommended)

### Story 1.2: Python API Service with Health Endpoint

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

### Story 1.3: PostgreSQL Database Setup

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

### Story 1.4: React/Next.js Frontend Service

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

### Story 1.5: Docker Containerization

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

### Story 1.6: Docker Compose Local Stack

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

### Story 1.7: Kind Cluster Setup

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

### Story 1.8: Kubernetes Manifests for Application

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

### Story 1.9: Basic Helm Charts

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

## 6. Epic 2: Infrastructure as Code & CI/CD

**Goal:** Establish cloud infrastructure using Terraform and automate the entire build-deploy pipeline with GitHub Actions. This epic delivers a fully automated workflow where code changes trigger builds, push container images to Azure Container Registry, and deploy to Kubernetes. Infrastructure changes are also managed through the pipeline, enabling GitOps-style operations.

### Story 2.1: Azure Account & CLI Setup

**As a** DevOps engineer,
**I want** an Azure account configured with CLI access and service principal,
**so that** I can provision and manage cloud resources programmatically.

**Acceptance Criteria:**
1. Azure account is created with $200 free credits activated
2. Azure CLI is installed and authenticated (`az login`)
3. Service Principal is created for Terraform/GitHub Actions (`az ad sp create-for-rbac`)
4. Service Principal credentials are securely documented (not in repo)
5. Resource Group is created for the project (e.g., `rg-devops-demo`)
6. Subscription ID, Tenant ID, Client ID, and Client Secret are noted
7. `az account show` confirms correct subscription is active

### Story 2.2: Terraform Remote State Backend

**As a** DevOps engineer,
**I want** Terraform state stored remotely in Azure Storage,
**so that** state is secure, shared, and supports locking.

**Acceptance Criteria:**
1. Azure Storage Account is created (manually or via bootstrap script)
2. Blob container `tfstate` exists for state files
3. Terraform backend configuration uses `azurerm` provider
4. `backend.tf` configures remote state with storage account details
5. State locking is enabled via Azure Blob lease mechanism
6. `terraform init` successfully initializes with remote backend
7. Bootstrap script or documentation explains initial setup
8. `.gitignore` excludes local `.terraform/` and state files

### Story 2.3: Terraform Azure Resources - ACR

**As a** DevOps engineer,
**I want** Azure Container Registry provisioned via Terraform,
**so that** I have a secure place to store container images.

**Acceptance Criteria:**
1. ACR resource is defined in Terraform (`azurerm_container_registry`)
2. ACR uses Basic SKU (free tier eligible)
3. Admin user is enabled for simple authentication (or use Service Principal)
4. ACR name is globally unique and follows naming convention
5. `terraform plan` shows expected resources
6. `terraform apply` successfully creates ACR
7. `docker login` to ACR succeeds using credentials
8. Output values expose ACR login server URL and credentials

### Story 2.4: Terraform Azure Resources - Key Vault

**As a** DevOps engineer,
**I want** Azure Key Vault provisioned via Terraform,
**so that** I have secure storage for secrets (to be used later in Epic 4).

**Acceptance Criteria:**
1. Key Vault resource is defined in Terraform (`azurerm_key_vault`)
2. Access policies grant Service Principal appropriate permissions
3. Soft delete and purge protection are configured appropriately
4. Key Vault name is globally unique
5. `terraform apply` successfully creates Key Vault
6. Manual test: secret can be set/retrieved via Azure CLI
7. Output values expose Key Vault URI

### Story 2.5: Terraform Modules Refactoring

**As a** DevOps engineer,
**I want** Terraform code organized into reusable modules,
**so that** the infrastructure code is maintainable and follows best practices.

**Acceptance Criteria:**
1. Module structure exists: `infra/terraform/modules/`
2. ACR module encapsulates container registry creation
3. Key Vault module encapsulates key vault creation
4. Storage module encapsulates storage account (for state bootstrap)
5. Root module in `infra/terraform/` calls child modules
6. Variables are properly typed with descriptions
7. Outputs are defined for each module
8. `terraform validate` passes
9. `terraform fmt -check` passes (code is formatted)
10. README documents module usage

### Story 2.6: GitHub Actions - Build & Test Workflow

**As a** DevOps engineer,
**I want** a GitHub Actions workflow that builds and tests on every push,
**so that** I get fast feedback on code quality.

**Acceptance Criteria:**
1. Workflow file exists at `.github/workflows/ci.yaml`
2. Workflow triggers on push to `main` and on pull requests
3. API job: installs dependencies, runs linter, runs pytest
4. Frontend job: installs dependencies, runs linter, runs build
5. Jobs run in parallel for efficiency
6. Workflow uses caching for dependencies (pip, npm)
7. Workflow fails fast if any job fails
8. Status badge is added to README

### Story 2.7: GitHub Actions - Docker Build & Push to ACR

**As a** DevOps engineer,
**I want** the CI pipeline to build Docker images and push to ACR,
**so that** built artifacts are available for deployment.

**Acceptance Criteria:**
1. Workflow extends `ci.yaml` or creates `cd.yaml`
2. Azure credentials are stored in GitHub Secrets
3. Workflow authenticates to ACR using `az acr login` or docker login
4. Docker images are built for API and Frontend
5. Images are tagged with git SHA and `latest`
6. Images are pushed to ACR only on `main` branch (not PRs)
7. Build uses Docker layer caching for speed
8. Workflow outputs image tags for downstream jobs

### Story 2.8: GitHub Actions - Deploy to Kubernetes (Dev)

**As a** DevOps engineer,
**I want** automated deployment to Kubernetes after successful build,
**so that** the dev environment always reflects the latest code.

**Acceptance Criteria:**
1. Deployment job runs after build/push succeeds
2. Workflow configures kubectl with Kind cluster (for local) or kubeconfig
3. Helm/Helmfile is used to deploy with new image tags
4. Deployment uses `values-dev.yaml` configuration
5. Deployment waits for rollout completion (`kubectl rollout status`)
6. Smoke test validates deployment (curl health endpoint)
7. Deployment job is skipped on PRs (only runs on main)
8. Deployment status is reported in workflow summary

### Story 2.9: GitHub Actions - Terraform in Pipeline

**As a** DevOps engineer,
**I want** Terraform plan/apply integrated into the CI/CD pipeline,
**so that** infrastructure changes follow the same review process as code.

**Acceptance Criteria:**
1. Terraform workflow exists at `.github/workflows/terraform.yaml`
2. Workflow triggers on changes to `infra/terraform/**`
3. `terraform fmt -check` validates formatting
4. `terraform validate` checks configuration
5. `terraform plan` runs on pull requests (output as PR comment)
6. `terraform apply` runs on merge to main (with auto-approve or manual)
7. Azure credentials are passed via environment variables
8. State locking prevents concurrent modifications
9. Workflow uses specific Terraform version (pinned)

### Story 2.10: GitHub Environments & Production Approval

**As a** DevOps engineer,
**I want** GitHub Environments configured with protection rules,
**so that** production deployments require explicit approval.

**Acceptance Criteria:**
1. GitHub Environment `dev` is created (no protection rules)
2. GitHub Environment `prod` is created with required reviewers
3. Deployment workflow references environments
4. Dev deployment runs automatically after build
5. Prod deployment waits for manual approval
6. Environment secrets are scoped appropriately
7. Deployment history is visible in GitHub Environments UI
8. Documentation explains the approval workflow

---

## 7. Epic 3: Observability Stack

**Goal:** Implement production-grade observability with metrics and logging. This epic delivers complete visibility into application health and behavior through Prometheus for metrics collection, Grafana for visualization, and Loki for centralized logging. The observability stack enables proactive monitoring and efficient troubleshooting—critical skills for MLOps where model monitoring follows similar patterns.

### Story 3.1: Deploy Prometheus & Grafana via Helm

**As a** DevOps engineer,
**I want** Prometheus and Grafana deployed to my Kubernetes cluster,
**so that** I have the foundation for metrics collection and visualization.

**Acceptance Criteria:**
1. `kube-prometheus-stack` Helm chart is added to Helmfile
2. Chart is deployed to dedicated namespace (`monitoring`)
3. Prometheus is accessible via port-forward (`kubectl port-forward svc/prometheus 9090`)
4. Grafana is accessible via port-forward (`kubectl port-forward svc/grafana 3000`)
5. Default Grafana admin credentials are configured via values
6. Pre-built Kubernetes dashboards are available in Grafana
7. Prometheus is scraping Kubernetes metrics (nodes, pods, containers)
8. Values file customizes resource requests/limits appropriately for local cluster
9. Documentation explains how to access Prometheus and Grafana UIs

### Story 3.2: Instrument API with Prometheus Metrics

**As a** DevOps engineer,
**I want** the Python API to expose custom Prometheus metrics,
**so that** I can monitor application-specific performance indicators.

**Acceptance Criteria:**
1. `prometheus-fastapi-instrumentator` or `prometheus-client` is added to API dependencies
2. API exposes `/metrics` endpoint in Prometheus format
3. Default HTTP metrics are collected (request count, latency histogram, status codes)
4. At least one custom business metric is defined (e.g., `items_created_total`)
5. Metrics endpoint is NOT exposed externally (internal only via Service)
6. Unit test validates metrics endpoint returns valid Prometheus format
7. Documentation explains available metrics and their meaning

### Story 3.3: Configure Prometheus ServiceMonitor

**As a** DevOps engineer,
**I want** Prometheus to automatically discover and scrape my API metrics,
**so that** metrics collection is dynamic and follows Kubernetes patterns.

**Acceptance Criteria:**
1. ServiceMonitor CRD is created for the API service
2. ServiceMonitor targets the `/metrics` endpoint on correct port
3. ServiceMonitor uses label selectors matching the API Service
4. Prometheus discovers the target (visible in Prometheus UI → Targets)
5. API metrics appear in Prometheus query UI (`http_requests_total`)
6. ServiceMonitor is included in API Helm chart
7. Scrape interval is configured appropriately (15s or 30s)

### Story 3.4: Create Custom Grafana Dashboard for API

**As a** DevOps engineer,
**I want** a custom Grafana dashboard visualizing API performance,
**so that** I can monitor application health at a glance.

**Acceptance Criteria:**
1. Dashboard JSON is created and stored in repo (`infra/grafana/dashboards/`)
2. Dashboard includes panels for:
   - Request rate (requests/second)
   - Error rate (4xx, 5xx percentage)
   - Latency percentiles (p50, p95, p99)
   - Active connections / concurrent requests
3. Dashboard uses variables for namespace and service filtering
4. Dashboard is provisioned automatically via Grafana ConfigMap/sidecar
5. Dashboard loads correctly in Grafana UI
6. Time range selector works properly
7. Documentation explains dashboard panels and usage

### Story 3.5: Deploy Loki & Promtail for Log Aggregation

**As a** DevOps engineer,
**I want** centralized logging with Loki and Promtail,
**so that** I can search and analyze logs from all application components.

**Acceptance Criteria:**
1. `loki-stack` Helm chart is added to Helmfile (or separate Loki + Promtail)
2. Loki is deployed to `monitoring` namespace
3. Promtail DaemonSet runs on all nodes, collecting container logs
4. Loki is configured with appropriate retention (7 days for local)
5. Promtail labels logs with namespace, pod, container metadata
6. Loki is accessible via port-forward for testing
7. Basic query works in Grafana Explore: `{namespace="devops-demo"}`
8. Resource limits are set appropriately for local cluster

### Story 3.6: Configure Grafana Loki Datasource

**As a** DevOps engineer,
**I want** Grafana connected to Loki as a datasource,
**so that** I can query and visualize logs alongside metrics.

**Acceptance Criteria:**
1. Loki datasource is configured in Grafana (via values or ConfigMap)
2. Datasource is provisioned automatically (not manual UI configuration)
3. Grafana Explore shows Loki as available datasource
4. LogQL queries return results: `{app="api"} |= "error"`
5. Logs can be filtered by namespace, pod, container
6. Log volume visualization works in Explore
7. Documentation explains basic LogQL query syntax

### Story 3.7: Create Logs Dashboard in Grafana

**As a** DevOps engineer,
**I want** a Grafana dashboard combining logs and metrics,
**so that** I can correlate application behavior across both data sources.

**Acceptance Criteria:**
1. Dashboard includes log panel showing recent API logs
2. Dashboard includes log volume over time (logs/minute)
3. Dashboard links metrics panels with log panels (same time range)
4. Error logs can be filtered separately (`|= "ERROR"` or `level="error"`)
5. Dashboard JSON is stored in repo and auto-provisioned
6. Dashboard demonstrates metrics → logs correlation workflow
7. Documentation explains how to drill down from metrics to logs

### Story 3.8: Structured Logging in API

**As a** DevOps engineer,
**I want** the API to emit structured JSON logs,
**so that** logs are easily parsed and queried in Loki.

**Acceptance Criteria:**
1. API logging is configured with JSON formatter (e.g., `python-json-logger`)
2. Log entries include: timestamp, level, message, request_id, path, method
3. Request/response logging middleware captures key fields
4. Correlation ID (request_id) is propagated through the request lifecycle
5. Log level is configurable via environment variable
6. Logs in Grafana can be filtered by JSON fields (`| json | level="ERROR"`)
7. Documentation explains log format and available fields

---

## 8. Epic 4: Production Hardening & Cloud

**Goal:** Elevate the deployment to production-grade quality with proper networking, security, and optional cloud deployment. This epic delivers HTTPS-enabled ingress, secrets management via Azure Key Vault, and validates the entire stack on Azure Kubernetes Service. The result is a portfolio-ready project demonstrating enterprise-level DevOps practices.

### Story 4.1: Deploy NGINX Ingress Controller

**As a** DevOps engineer,
**I want** NGINX Ingress Controller deployed to my cluster,
**so that** I can route external traffic to my services using standard HTTP/HTTPS.

**Acceptance Criteria:**
1. `ingress-nginx` Helm chart is added to Helmfile
2. Ingress Controller is deployed to `ingress-nginx` namespace
3. Controller Service is accessible (NodePort for Kind, LoadBalancer for AKS)
4. Kind cluster configuration maps ports 80/443 to host
5. Ingress Controller logs show it's processing requests
6. `kubectl get ingressclass` shows nginx as available
7. Documentation explains the ingress architecture
8. Values file configures appropriate resource limits

### Story 4.2: Configure Ingress Resources for Application

**As a** DevOps engineer,
**I want** Ingress resources routing traffic to Frontend and API,
**so that** users can access the application via friendly URLs.

**Acceptance Criteria:**
1. Ingress resource is created for Frontend (e.g., `app.local` → frontend service)
2. Ingress resource is created for API (e.g., `api.local` or `app.local/api`)
3. Ingress annotations are configured for NGINX-specific features
4. Path-based routing works correctly (if using single domain)
5. Host-based routing works correctly (if using multiple subdomains)
6. `/etc/hosts` or nip.io DNS is documented for local testing
7. Application is accessible via browser at configured hostname
8. Ingress resources are included in Helm charts

### Story 4.3: Deploy cert-manager for Certificate Management

**As a** DevOps engineer,
**I want** cert-manager deployed for automatic TLS certificate management,
**so that** I can enable HTTPS without manual certificate handling.

**Acceptance Criteria:**
1. `cert-manager` Helm chart is added to Helmfile
2. cert-manager is deployed to `cert-manager` namespace
3. CRDs are installed (Certificate, Issuer, ClusterIssuer)
4. cert-manager pods are running and healthy
5. `kubectl get clusterissuer` shows available issuers
6. Documentation explains cert-manager architecture
7. Values file configures appropriate resource limits

### Story 4.4: Configure TLS Certificates

**As a** DevOps engineer,
**I want** TLS certificates provisioned for my Ingress,
**so that** all traffic is encrypted with HTTPS.

**Acceptance Criteria:**
1. Self-signed ClusterIssuer is created for local development
2. Let's Encrypt ClusterIssuer is created for production (staging first)
3. Ingress resources are annotated to request certificates
4. Certificate resources are automatically created by cert-manager
5. TLS secrets are generated and mounted by Ingress Controller
6. HTTPS access works (browser shows certificate, even if self-signed warning)
7. HTTP to HTTPS redirect is configured
8. Certificate renewal is tested (for Let's Encrypt)
9. Different issuers are used per environment (self-signed for dev, LE for prod)

### Story 4.5: Azure Key Vault CSI Driver Setup

**As a** DevOps engineer,
**I want** the Azure Key Vault CSI Driver installed in my cluster,
**so that** I can mount secrets from Key Vault into pods.

**Acceptance Criteria:**
1. Secrets Store CSI Driver is installed via Helm
2. Azure Key Vault Provider is installed via Helm
3. CRDs are created (SecretProviderClass)
4. Driver pods are running on all nodes (DaemonSet)
5. Azure AD Pod Identity or Workload Identity is configured (or SP credentials)
6. Documentation explains the CSI Driver architecture
7. Test SecretProviderClass can access Key Vault (manual validation)

### Story 4.6: Migrate Secrets to Azure Key Vault

**As a** DevOps engineer,
**I want** application secrets migrated from K8s Secrets to Azure Key Vault,
**so that** I follow enterprise-grade secrets management practices.

**Acceptance Criteria:**
1. Database password is stored in Azure Key Vault
2. SecretProviderClass is created for the API deployment
3. API pod mounts Key Vault secrets as files or environment variables
4. Kubernetes Secret is optionally synced from Key Vault (syncSecret feature)
5. API successfully connects to database using Key Vault secret
6. Old K8s Secret can be removed (or kept as fallback)
7. Helm chart values toggle between K8s Secrets and Key Vault
8. Documentation explains the migration process and rationale
9. Rollback procedure is documented

### Story 4.7: Network Policies (Bonus)

**As a** DevOps engineer,
**I want** Network Policies restricting pod-to-pod communication,
**so that** I implement defense-in-depth security.

**Acceptance Criteria:**
1. Default deny NetworkPolicy is created for application namespace
2. Allow policy permits Frontend → API communication
3. Allow policy permits API → PostgreSQL communication
4. Allow policy permits Prometheus → API (for scraping)
5. Ingress Controller can reach Frontend and API
6. Policies are tested (blocked traffic returns connection refused)
7. NetworkPolicies are included in Helm charts
8. Documentation explains the network security model

### Story 4.8: Provision AKS Cluster with Terraform (Bonus)

**As a** DevOps engineer,
**I want** an AKS cluster provisioned via Terraform,
**so that** I can validate my application on real cloud infrastructure.

**Acceptance Criteria:**
1. AKS module is created in Terraform
2. Cluster uses minimal configuration (1-2 B2s nodes)
3. Cluster is integrated with ACR (image pull permissions)
4. Azure CNI or kubenet networking is configured
5. `terraform apply` creates the cluster successfully
6. `az aks get-credentials` configures kubectl context
7. Cluster is created in reasonable time (< 15 minutes)
8. Cost estimate is documented (~$15-20 for 5 days)
9. Destroy instructions are clear to avoid ongoing charges

### Story 4.9: Deploy Application to AKS (Bonus)

**As a** DevOps engineer,
**I want** the complete application deployed to AKS,
**so that** I validate the full cloud deployment experience.

**Acceptance Criteria:**
1. Helmfile deploys all components to AKS cluster
2. Ingress Controller works with Azure Load Balancer
3. TLS certificates are provisioned via Let's Encrypt (real domain or nip.io)
4. Application is accessible via public URL
5. Observability stack works on AKS
6. Azure Key Vault integration works from AKS (Workload Identity)
7. CI/CD pipeline can deploy to AKS (new environment)
8. Performance/behavior comparison with Kind is documented

### Story 4.10: Project Documentation & Portfolio Polish

**As a** DevOps engineer,
**I want** comprehensive documentation and portfolio-ready presentation,
**so that** this project demonstrates my skills to potential employers.

**Acceptance Criteria:**
1. Root README includes project overview, architecture diagram, and quick start
2. Each component has its own README with setup instructions
3. Architecture diagram shows all components and their relationships
4. Screenshots of Grafana dashboards are included
5. CI/CD pipeline diagram illustrates the workflow
6. Lessons learned / retrospective section documents key insights
7. Technologies used are listed with brief explanations of choices
8. Setup instructions work for a fresh clone (validated)
9. Cost summary for Azure resources is documented
10. Future improvements section outlines MLOps extension possibilities

---

## 9. Summary

| Metric | Count |
|--------|-------|
| **Total Epics** | 4 |
| **Total Stories** | 37 |
| **Core Stories** | 34 |
| **Bonus Stories** | 3 |
| **Functional Requirements** | 31 |
| **Non-Functional Requirements** | 13 |

### Timeline Mapping

| Epic | Stories | Days |
|------|---------|------|
| Epic 1: Foundation | 9 | J1, J3 (partial) |
| Epic 2: IaC & CI/CD | 10 | J2, J3 (partial), J4 |
| Epic 3: Observability | 8 | J5 |
| Epic 4: Hardening & Cloud | 10 | J6, J7 |

---

## 10. Checklist Results Report

### Executive Summary

| Metric | Assessment |
|--------|------------|
| **Overall PRD Completeness** | 85% |
| **MVP Scope Appropriateness** | Just Right (ambitious but achievable with buffer) |
| **Readiness for Architecture** | **Ready** |

### Category Analysis

| Category | Status | Notes |
|----------|--------|-------|
| 1. Problem Definition & Context | PASS | Clear skills gap defined |
| 2. MVP Scope Definition | PASS | Core vs bonus clearly separated |
| 3. User Experience Requirements | N/A | Learning project - no external users |
| 4. Functional Requirements | PASS | 31 FRs, testable, well-structured |
| 5. Non-Functional Requirements | PARTIAL | Good coverage, missing specific perf numbers |
| 6. Epic & Story Structure | PASS | 4 epics, 37 stories, proper sequencing |
| 7. Technical Guidance | PASS | Comprehensive technical assumptions |
| 8. Cross-Functional Requirements | PARTIAL | Data model minimal, acceptable for learning |
| 9. Clarity & Communication | PASS | Well-structured, consistent terminology |

### Recommendations

1. Add specific performance NFRs if needed (API latency, CI/CD duration)
2. Architecture diagram to be created by Architect
3. Document rollback procedures in Epic 2 stories

### Final Decision

**READY FOR ARCHITECT** - PRD is comprehensive and ready for architectural design.

---

## 11. Next Steps

### For UX Expert
> N/A - This project does not require UX design. Frontend is a minimal demo component.

### For Architect

```
@Architect - Please review the PRD at docs/prd.md and create the technical architecture document.

Context:
- DevOps learning project (1 week + buffer)
- 3-tier app: React/Next.js + Python FastAPI + PostgreSQL
- Infrastructure: Kind (local), Azure (ACR, Key Vault, bonus AKS)
- CI/CD: GitHub Actions
- IaC: Terraform with remote state
- Packaging: Helm + Helmfile
- Observability: Prometheus, Grafana, Loki

Focus areas:
1. Component diagram with all services and interactions
2. Network topology (local Kind and Azure AKS)
3. CI/CD pipeline architecture (build → test → push → deploy flow)
4. Security architecture (secrets flow, TLS termination points)
5. Folder structure refinements if needed
6. Technical risks and mitigation strategies

Constraints:
- Azure Free Tier + $200 credits
- Must work on local Kind cluster first
- Production patterns even for learning project
```

---

*Document generated by PM John using BMAD-METHOD*
*Validation Date: 2025-01-25*
