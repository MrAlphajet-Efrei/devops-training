# 2. Requirements

## 2.1 Functional Requirements

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

## 2.2 Non-Functional Requirements

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
