# 8. Epic 4: Production Hardening & Cloud

**Goal:** Elevate the deployment to production-grade quality with proper networking, security, and optional cloud deployment. This epic delivers HTTPS-enabled ingress, secrets management via Azure Key Vault, and validates the entire stack on Azure Kubernetes Service. The result is a portfolio-ready project demonstrating enterprise-level DevOps practices.

## Story 4.1: Deploy NGINX Ingress Controller

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

## Story 4.2: Configure Ingress Resources for Application

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

## Story 4.3: Deploy cert-manager for Certificate Management

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

## Story 4.4: Configure TLS Certificates

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

## Story 4.5: Azure Key Vault CSI Driver Setup

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

## Story 4.6: Migrate Secrets to Azure Key Vault

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

## Story 4.7: Network Policies (Bonus)

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

## Story 4.8: Provision AKS Cluster with Terraform (Bonus)

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

## Story 4.9: Deploy Application to AKS (Bonus)

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

## Story 4.10: Project Documentation & Portfolio Polish

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
