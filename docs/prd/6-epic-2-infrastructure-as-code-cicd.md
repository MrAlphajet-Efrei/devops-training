# 6. Epic 2: Infrastructure as Code & CI/CD

**Goal:** Establish cloud infrastructure using Terraform and automate the entire build-deploy pipeline with GitHub Actions. This epic delivers a fully automated workflow where code changes trigger builds, push container images to Azure Container Registry, and deploy to Kubernetes. Infrastructure changes are also managed through the pipeline, enabling GitOps-style operations.

## Story 2.1: Azure Account & CLI Setup

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

## Story 2.2: Terraform Remote State Backend

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

## Story 2.3: Terraform Azure Resources - ACR

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

## Story 2.4: Terraform Azure Resources - Key Vault

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

## Story 2.5: Terraform Modules Refactoring

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

## Story 2.6: GitHub Actions - Build & Test Workflow

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

## Story 2.7: GitHub Actions - Docker Build & Push to ACR

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

## Story 2.8: GitHub Actions - Deploy to Kubernetes (Dev)

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

## Story 2.9: GitHub Actions - Terraform in Pipeline

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

## Story 2.10: GitHub Environments & Production Approval

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
