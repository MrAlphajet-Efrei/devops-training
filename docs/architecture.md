# DevOps Full-Chain Learning Project - Fullstack Architecture Document

**Version:** 1.0
**Status:** Approved
**Last Updated:** 2026-01-26
**Author:** Architect Winston

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [High Level Architecture](#2-high-level-architecture)
3. [Tech Stack](#3-tech-stack)
4. [Data Models](#4-data-models)
5. [API Specification](#5-api-specification)
6. [Components](#6-components)
7. [External APIs](#7-external-apis)
8. [Core Workflows](#8-core-workflows)
9. [Database Schema](#9-database-schema)
10. [Frontend Architecture](#10-frontend-architecture)
11. [Backend Architecture](#11-backend-architecture)
12. [Unified Project Structure](#12-unified-project-structure)
13. [Development Workflow](#13-development-workflow)
14. [Deployment Architecture](#14-deployment-architecture)
15. [Security and Performance](#15-security-and-performance)
16. [Testing Strategy](#16-testing-strategy)
17. [Coding Standards](#17-coding-standards)
18. [Error Handling Strategy](#18-error-handling-strategy)
19. [Monitoring and Observability](#19-monitoring-and-observability)
20. [Checklist Results Report](#20-checklist-results-report)

---

## 1. Introduction

This document outlines the complete fullstack architecture for the **DevOps Full-Chain Learning Project**, including backend systems, frontend implementation, and their integration. It serves as the single source of truth for AI-driven development, ensuring consistency across the entire technology stack.

This unified approach combines what would traditionally be separate backend and frontend architecture documents, streamlining the development process for modern fullstack applications where these concerns are increasingly intertwined.

### 1.1 Starter Template or Existing Project

**N/A - Greenfield project**

This is a new project built from scratch as a learning exercise. No starter templates or existing codebases are being used. The architecture decisions are intentionally made fresh to maximize learning of the complete DevOps chain.

### 1.2 Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-01-26 | 1.0 | Initial architecture document | Architect Winston |

---

## 2. High Level Architecture

### 2.1 Technical Summary

This project implements a **containerized 3-tier microservices architecture** deployed to Kubernetes, following cloud-native patterns optimized for a DevOps learning journey. The frontend (React/Next.js) serves as a minimal UI layer, the backend (Python FastAPI) handles business logic with MLOps-ready instrumentation, and PostgreSQL provides persistent storage.

The architecture prioritizes **local-first development** with Kind clusters, while maintaining full compatibility with Azure cloud services (ACR, Key Vault, optional AKS). Infrastructure is managed declaratively through Terraform with remote state, applications are packaged as Helm charts orchestrated by Helmfile, and the entire pipeline is automated via GitHub Actions. This design achieves all 9 PRD goals while building a foundation for future MLOps extension.

### 2.2 Platform and Infrastructure Choice

**Selected Platform:** Azure (Hybrid Local/Cloud)

| Platform | Pros | Cons | Fit for Project |
|----------|------|------|-----------------|
| **Azure (Hybrid Local/Cloud)** | Free tier + $200 credits, ACR/Key Vault included, AKS for validation | Learning curve for Azure-specific services | ✅ **RECOMMENDED** |
| **AWS** | Mature ecosystem, EKS well-documented | No free credits context | ❌ Not aligned |
| **Local Only (Kind)** | Zero cost, full control | Misses cloud provider experience | ❌ Incomplete learning |

**Key Services:**
- **Local:** Kind (Kubernetes), Docker Desktop
- **Azure:** ACR (Container Registry), Key Vault (Secrets), Storage Account (Terraform state), AKS (bonus)
- **CI/CD:** GitHub Actions

**Deployment Regions:**
- Local: Kind cluster on development machine
- Azure: West Europe (or nearest region with free tier availability)

### 2.3 Repository Structure

**Structure:** Monorepo (single repository)

**Rationale:**
- Simplifies CI/CD pipeline configuration (single trigger point)
- Easier atomic commits across app + infrastructure changes
- Appropriate for learning project (all context in one place)
- Standard pattern for small-to-medium projects

**Monorepo Tool:** npm workspaces (lightweight) or none (simple folder structure)

### 2.4 High Level Architecture Diagram

```mermaid
graph TB
    subgraph "User Access"
        U[👤 User/Browser]
    end

    subgraph "CI/CD Layer"
        GHA[GitHub Actions]
        ACR[Azure Container Registry]
    end

    subgraph "Kubernetes Cluster - Kind/AKS"
        subgraph "Ingress Layer"
            ING[NGINX Ingress Controller]
            CM[cert-manager]
        end

        subgraph "Application Namespace"
            FE[Frontend<br/>Next.js]
            API[API<br/>FastAPI]
            DB[(PostgreSQL)]
        end

        subgraph "Monitoring Namespace"
            PROM[Prometheus]
            GRAF[Grafana]
            LOKI[Loki]
            PROM_TAIL[Promtail]
        end

        subgraph "Secrets"
            K8S_SEC[K8s Secrets]
            KV_CSI[Key Vault CSI]
        end
    end

    subgraph "Azure Cloud"
        AKV[Azure Key Vault]
        TF_STATE[Storage Account<br/>Terraform State]
    end

    U -->|HTTPS| ING
    ING -->|/| FE
    ING -->|/api| API
    FE -->|REST| API
    API --> DB
    API --> K8S_SEC
    K8S_SEC -.->|Phase 2| KV_CSI
    KV_CSI -.-> AKV

    GHA -->|Push Images| ACR
    GHA -->|Deploy| ING
    GHA -->|Terraform| TF_STATE

    PROM -->|Scrape| API
    PROM -->|Scrape| FE
    PROM_TAIL -->|Collect Logs| API
    PROM_TAIL -->|Collect Logs| FE
    PROM_TAIL --> LOKI
    GRAF --> PROM
    GRAF --> LOKI

    CM -->|TLS Certs| ING
```

### 2.5 Architectural Patterns

| Pattern | Description | Rationale |
|---------|-------------|-----------|
| **Containerized Microservices** | Each component runs in isolated containers | Standard cloud-native pattern, enables independent scaling |
| **3-Tier Architecture** | Presentation → Business Logic → Data | Clear separation of concerns, industry standard |
| **Infrastructure as Code** | All infra defined in Terraform | Reproducibility, version control, GitOps foundation |
| **Declarative Deployment** | Helm charts with Helmfile orchestration | Environment-specific config, rollback capability |
| **GitOps-Adjacent CI/CD** | GitHub Actions triggers deployments | Pipeline as code, full automation |
| **Observability-First** | Metrics (Prometheus) + Logs (Loki) from day 1 | Critical for MLOps, enables proactive monitoring |
| **Progressive Secrets Management** | K8s Secrets → Azure Key Vault migration | Learn fundamentals first, then enterprise patterns |
| **API Gateway Pattern** | NGINX Ingress as single entry point | Centralized TLS termination, routing |
| **Health Check Pattern** | Liveness + Readiness probes on API | K8s best practice, enables self-healing |

---

## 3. Tech Stack

This is the **DEFINITIVE** technology selection for the entire project. All development must use these exact technologies and versions.

| Category | Technology | Version | Purpose | Rationale |
|----------|------------|---------|---------|-----------|
| **Frontend Language** | TypeScript | 5.x | Type-safe frontend development | Industry standard, catches errors at compile time |
| **Frontend Framework** | Next.js | 14.x | React framework with SSR/SSG | Modern React patterns, easy deployment |
| **UI Component Library** | Tailwind CSS | 3.x | Utility-first styling | Rapid prototyping, minimal CSS overhead |
| **State Management** | React Context + SWR | 2.x | Client state + data fetching | Lightweight, SWR handles API caching |
| **Backend Language** | Python | 3.11+ | API development | MLOps pathway, FastAPI ecosystem |
| **Backend Framework** | FastAPI | 0.109+ | REST API framework | Async-native, auto OpenAPI docs |
| **API Style** | REST | OpenAPI 3.0 | API communication | Simple, well-understood |
| **Database** | PostgreSQL | 15.x | Relational data storage | Robust, SQL standard, excellent K8s support |
| **Cache** | None (MVP) | - | - | Out of scope for learning project |
| **Authentication** | None (MVP) | - | - | Out of scope per PRD |
| **Frontend Testing** | Jest + React Testing Library | 29.x / 14.x | Unit & component tests | Standard React testing stack |
| **Backend Testing** | pytest + httpx | 7.x / 0.26+ | Unit & integration tests | Python standard, async support |
| **E2E Testing** | curl/httpie (smoke tests) | - | Pipeline validation | Lightweight, sufficient for scope |
| **IaC Tool** | Terraform | 1.5+ | Infrastructure provisioning | Industry standard, Azure provider |
| **CI/CD** | GitHub Actions | - | Pipeline automation | Native GitHub integration, free |
| **Container Runtime** | Docker | 24.x | Container builds | Industry standard, multi-stage builds |
| **Container Orchestration** | Kubernetes (Kind/AKS) | 1.28+ | Container orchestration | Learning target, production standard |
| **Package Manager (K8s)** | Helm + Helmfile | 3.x / 0.158+ | K8s app packaging | Declarative, environment-specific values |
| **Monitoring** | Prometheus + Grafana | kube-prometheus-stack | Metrics collection & visualization | MLOps foundation, industry standard |
| **Logging** | Loki + Promtail | loki-stack | Log aggregation | Grafana ecosystem, lightweight |
| **Ingress Controller** | NGINX Ingress | 4.x | Traffic routing | Most common, well-documented |
| **Certificate Management** | cert-manager | 1.13+ | TLS automation | K8s native, Let's Encrypt integration |
| **Secrets (Phase 1)** | Kubernetes Secrets | native | Basic secret storage | Learn fundamentals first |
| **Secrets (Phase 2)** | Azure Key Vault + CSI Driver | - | Enterprise secrets | Production pattern |

---

## 4. Data Models

The data model is intentionally **minimal** as the application serves as a vehicle for DevOps learning.

### 4.1 Item

**Purpose:** Core business entity demonstrating full CRUD operations through the API, database persistence, and frontend display.

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | UUID | Unique identifier, auto-generated |
| `name` | string | Item name, required, max 255 chars |
| `description` | string | Optional item description |
| `created_at` | timestamp | Auto-set on creation |
| `updated_at` | timestamp | Auto-updated on modification |

#### TypeScript Interface

```typescript
// packages/shared/types/item.ts

export interface Item {
  id: string;
  name: string;
  description?: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateItemRequest {
  name: string;
  description?: string;
}

export interface UpdateItemRequest {
  name?: string;
  description?: string;
}

export interface ItemListResponse {
  items: Item[];
  total: number;
}
```

#### Python Model

```python
# apps/api/models/item.py

from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    description: str | None = None

class Item(ItemBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```

### 4.2 Health Check Models

```typescript
export interface HealthResponse {
  status: 'healthy' | 'unhealthy';
  timestamp: Date;
}

export interface ReadinessResponse {
  status: 'ready' | 'not_ready';
  checks: {
    database: 'ok' | 'error';
  };
  timestamp: Date;
}
```

### 4.3 Entity Relationship Diagram

```mermaid
erDiagram
    ITEM {
        uuid id PK
        varchar(255) name
        text description
        timestamp created_at
        timestamp updated_at
    }
```

---

## 5. API Specification

### 5.1 REST API Specification (OpenAPI 3.0)

```yaml
openapi: 3.0.3
info:
  title: DevOps Learning Project API
  description: A minimal REST API for the DevOps Full-Chain Learning Project.
  version: 1.0.0

servers:
  - url: http://localhost:8000
    description: Local development
  - url: http://api.local
    description: Kind cluster (via Ingress)

paths:
  /health:
    get:
      tags: [Health]
      summary: Liveness probe
      responses:
        '200':
          description: API is alive
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HealthResponse'

  /ready:
    get:
      tags: [Health]
      summary: Readiness probe
      responses:
        '200':
          description: API is ready
        '503':
          description: API is not ready

  /items:
    get:
      tags: [Items]
      summary: List all items
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 100
        - name: offset
          in: query
          schema:
            type: integer
            default: 0
      responses:
        '200':
          description: List of items
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ItemListResponse'

    post:
      tags: [Items]
      summary: Create a new item
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateItemRequest'
      responses:
        '201':
          description: Item created
        '422':
          description: Validation error

  /items/{item_id}:
    get:
      tags: [Items]
      summary: Get item by ID
      parameters:
        - name: item_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Item found
        '404':
          description: Item not found

    put:
      tags: [Items]
      summary: Update an item
      responses:
        '200':
          description: Item updated
        '404':
          description: Item not found

    delete:
      tags: [Items]
      summary: Delete an item
      responses:
        '204':
          description: Item deleted
        '404':
          description: Item not found

  /metrics:
    get:
      tags: [Metrics]
      summary: Prometheus metrics (internal only)
      responses:
        '200':
          description: Prometheus format metrics

components:
  schemas:
    HealthResponse:
      type: object
      properties:
        status:
          type: string
          enum: [healthy, unhealthy]
        timestamp:
          type: string
          format: date-time

    Item:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    CreateItemRequest:
      type: object
      required: [name]
      properties:
        name:
          type: string
          maxLength: 255
        description:
          type: string

    ItemListResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/Item'
        total:
          type: integer
```

### 5.2 API Endpoints Summary

| Method | Path | Purpose | Auth |
|--------|------|---------|------|
| `GET` | `/health` | Liveness probe | No |
| `GET` | `/ready` | Readiness probe | No |
| `GET` | `/items` | List items | No |
| `POST` | `/items` | Create item | No |
| `GET` | `/items/{id}` | Get single item | No |
| `PUT` | `/items/{id}` | Update item | No |
| `DELETE` | `/items/{id}` | Delete item | No |
| `GET` | `/metrics` | Prometheus metrics | No |
| `GET` | `/docs` | Swagger UI | No |

---

## 6. Components

### 6.1 Application Components

| Component | Responsibility | Technology | K8s Resources |
|-----------|----------------|------------|---------------|
| **Frontend** | Web UI, data display | Next.js 14 | Deployment, Service, ConfigMap |
| **API** | Business logic, REST endpoints | FastAPI | Deployment, Service, ConfigMap, Secret, ServiceMonitor |
| **PostgreSQL** | Data persistence | PostgreSQL 15 | StatefulSet, Service, PVC, Secret |

### 6.2 Infrastructure Components

| Component | Responsibility | Technology |
|-----------|----------------|------------|
| **NGINX Ingress** | Traffic routing, TLS termination | ingress-nginx Helm chart |
| **cert-manager** | TLS certificate automation | cert-manager Helm chart |
| **CSI Driver** | Azure Key Vault secret mounting | secrets-store-csi-driver |

### 6.3 Observability Components

| Component | Responsibility | Technology |
|-----------|----------------|------------|
| **Prometheus** | Metrics collection | kube-prometheus-stack |
| **Grafana** | Visualization | kube-prometheus-stack |
| **Loki** | Log aggregation | loki-stack |
| **Promtail** | Log collection | loki-stack |

### 6.4 Component Diagram

```mermaid
C4Context
    title System Context Diagram

    Person(user, "User", "Accesses web application")
    Person(dev, "Developer", "Develops and deploys")

    System_Boundary(k8s, "Kubernetes Cluster") {
        Container(frontend, "Frontend", "Next.js")
        Container(api, "API", "FastAPI")
        ContainerDb(db, "Database", "PostgreSQL")
        Container(ingress, "Ingress", "NGINX")
    }

    System_Ext(acr, "Azure ACR", "Container images")
    System_Ext(keyvault, "Azure Key Vault", "Secrets")
    System_Ext(github, "GitHub Actions", "CI/CD")

    Rel(user, ingress, "HTTPS")
    Rel(ingress, frontend, "HTTP")
    Rel(ingress, api, "HTTP /api")
    Rel(frontend, api, "REST")
    Rel(api, db, "SQL")
```

---

## 7. External APIs

| Service | Purpose | Auth Method | Used By |
|---------|---------|-------------|---------|
| **Azure ACR** | Container images | Service Principal | GitHub Actions, K8s |
| **Azure Key Vault** | Secrets storage | Service Principal / CSI | API pods |
| **Azure Storage** | Terraform state | Service Principal | Terraform |
| **Azure ARM** | Resource provisioning | Service Principal | Terraform |
| **Let's Encrypt** | TLS certificates | ACME account | cert-manager |
| **GitHub API** | CI/CD automation | GITHUB_TOKEN | GitHub Actions |
| **Docker Hub** | Base images | Anonymous | Docker builds |

### 7.1 Azure Container Registry

- **Base URL:** `https://{registry-name}.azurecr.io`
- **Authentication:** Service Principal or `az acr login`
- **Rate Limits:** Basic SKU: 10 pulls/minute

### 7.2 Azure Key Vault

- **Base URL:** `https://{vault-name}.vault.azure.net`
- **Authentication:** Service Principal with access policy
- **Key Endpoints:** `GET /secrets/{name}`, `PUT /secrets/{name}`

### 7.3 Let's Encrypt ACME

- **Staging URL:** `https://acme-staging-v02.api.letsencrypt.org/directory`
- **Production URL:** `https://acme-v02.api.letsencrypt.org/directory`
- **Rate Limits:** 50 certs/week per domain (production)

---

## 8. Core Workflows

### 8.1 User Creates Item

```mermaid
sequenceDiagram
    participant U as User Browser
    participant ING as NGINX Ingress
    participant FE as Frontend
    participant API as API
    participant DB as PostgreSQL

    U->>ING: POST /api/items
    ING->>API: POST /items
    API->>API: Validate (Pydantic)
    API->>DB: INSERT INTO items
    DB-->>API: Item record
    API-->>ING: 201 Created
    ING-->>U: Item JSON
```

### 8.2 CI/CD Pipeline

```mermaid
sequenceDiagram
    participant DEV as Developer
    participant GH as GitHub
    participant GHA as GitHub Actions
    participant ACR as Azure ACR
    participant K8S as Kubernetes

    DEV->>GH: git push main
    GH->>GHA: Trigger workflow
    GHA->>GHA: Build & Test
    GHA->>ACR: Push images
    GHA->>K8S: Helm deploy
    GHA->>K8S: Verify rollout
    GHA-->>GH: Success
```

### 8.3 Readiness Probe (Database Down)

```mermaid
sequenceDiagram
    participant K8S as Kubernetes
    participant API as API Pod
    participant DB as PostgreSQL

    K8S->>API: GET /ready
    API->>DB: SELECT 1
    DB--xAPI: Connection refused
    API-->>K8S: 503 Service Unavailable
    K8S->>K8S: Mark pod NotReady
    K8S->>K8S: Remove from endpoints
```

### 8.4 Log Aggregation

```mermaid
sequenceDiagram
    participant API as API Pod
    participant PT as Promtail
    participant LOKI as Loki
    participant GRAF as Grafana

    API->>API: logger.info("Item created")
    PT->>API: Tail logs
    PT->>PT: Add K8s labels
    PT->>LOKI: Push logs
    GRAF->>LOKI: Query logs
    GRAF-->>GRAF: Display
```

---

## 9. Database Schema

### 9.1 SQL DDL

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Items table
CREATE TABLE items (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            VARCHAR(255) NOT NULL,
    description     TEXT,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    CONSTRAINT items_name_not_empty CHECK (LENGTH(TRIM(name)) > 0)
);

-- Indexes
CREATE INDEX idx_items_created_at ON items (created_at DESC);
CREATE INDEX idx_items_name ON items (name);

-- Auto-update trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_items_updated_at
    BEFORE UPDATE ON items
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

### 9.2 SQLAlchemy Model

```python
from sqlalchemy import Column, String, Text, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("LENGTH(TRIM(name)) > 0", name="items_name_not_empty"),
    )
```

### 9.3 Connection Configuration

```python
from sqlalchemy import create_engine
from app.config import settings

engine = create_engine(
    settings.database_url,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=300,
)
```

---

## 10. Frontend Architecture

### 10.1 Component Organization

```
apps/frontend/src/
├── app/                    # Next.js App Router
│   ├── layout.tsx
│   ├── page.tsx
│   ├── loading.tsx
│   └── error.tsx
├── components/
│   ├── ui/                 # Generic UI components
│   ├── items/              # Feature components
│   └── layout/             # Layout components
├── hooks/                  # Custom React hooks
├── services/               # API client layer
├── types/                  # TypeScript types
└── lib/                    # Utilities
```

### 10.2 State Management

- **Server State:** SWR handles all API data with caching
- **UI State:** Local `useState` for component state
- **No global state manager needed** for this simple app

### 10.3 API Client

```typescript
// src/services/api.ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '/api';

export async function apiClient<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!response.ok) throw new Error('API error');
  return response.json();
}
```

### 10.4 SWR Hook Example

```typescript
// src/hooks/useItems.ts
import useSWR from 'swr';
import { itemsService } from '@/services/items';

export function useItems() {
  const { data, error, isLoading, mutate } = useSWR('/items', () => itemsService.list());
  return {
    items: data?.items ?? [],
    total: data?.total ?? 0,
    isLoading,
    isError: !!error,
    refresh: mutate,
  };
}
```

---

## 11. Backend Architecture

### 11.1 Application Structure

```
apps/api/src/app/
├── main.py                 # FastAPI application entry
├── config.py               # Settings (Pydantic)
├── api/
│   ├── router.py           # Main router
│   ├── deps.py             # Dependencies (DB session)
│   └── routes/
│       ├── health.py
│       └── items.py
├── models/                 # Pydantic schemas
├── db/
│   ├── session.py          # SQLAlchemy session
│   ├── models.py           # ORM models
│   └── repositories/       # Data access layer
├── services/               # Business logic
└── middleware/             # Custom middleware
```

### 11.2 Application Factory

```python
# src/app/main.py
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

def create_app() -> FastAPI:
    app = FastAPI(title="DevOps Learning API", version="1.0.0")

    # Middleware
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins)
    app.add_middleware(RequestLoggingMiddleware)

    # Prometheus
    Instrumentator().instrument(app).expose(app, endpoint="/metrics")

    # Routes
    app.include_router(api_router)

    return app

app = create_app()
```

### 11.3 Repository Pattern

```python
# src/app/db/repositories/item.py
class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, limit: int, offset: int) -> tuple[list[ItemModel], int]:
        total = self.db.scalar(select(func.count(ItemModel.id)))
        items = list(self.db.scalars(
            select(ItemModel).order_by(ItemModel.created_at.desc()).limit(limit).offset(offset)
        ).all())
        return items, total or 0

    def create(self, item_in: ItemCreate) -> ItemModel:
        item = ItemModel(name=item_in.name, description=item_in.description)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
```

### 11.4 Configuration

```python
# src/app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "devops_demo"
    db_user: str = "app_user"
    db_password: str
    debug: bool = False
    cors_origins: list[str] = ["http://localhost:3000"]

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## 12. Unified Project Structure

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

## 13. Development Workflow

### 13.1 Prerequisites

```bash
docker --version          # >= 24.0.0
node --version            # >= 20.0.0
python --version          # >= 3.11.0
kubectl version --client  # >= 1.28.0
helm version              # >= 3.13.0
terraform --version       # >= 1.5.0
kind version              # >= 0.20.0
```

### 13.2 Initial Setup

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

### 13.3 Common Commands

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

### 13.4 Environment Variables

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

## 14. Deployment Architecture

### 14.1 Deployment Strategy

| Component | Platform | Build Command | Output |
|-----------|----------|---------------|--------|
| Frontend | K8s (Kind/AKS) | `npm run build` | `.next/standalone` |
| API | K8s (Kind/AKS) | Docker build | Container image |

### 14.2 Environments

| Environment | Frontend URL | API URL | Purpose |
|-------------|--------------|---------|---------|
| Development | `localhost:3000` | `localhost:8000` | Local docker-compose |
| Kind | `app.local` | `api.local` | Local K8s |
| Production | `app.example.com` | `api.example.com` | Live |

### 14.3 CI/CD Pipeline

1. **On PR:** Lint, test, build validation
2. **On merge to main:**
   - Build Docker images
   - Push to ACR with SHA tag
   - Deploy to dev environment
   - Run smoke tests
3. **Production:** Manual approval required

---

## 15. Security and Performance

### 15.1 Security Requirements

**Container Security:**
- Run as non-root (UID 1000)
- Read-only root filesystem
- Drop all capabilities
- No privilege escalation

**API Security:**
- Input validation via Pydantic
- CORS whitelist
- Rate limiting via Ingress

**Secrets:**
- Never in code/config
- K8s Secrets (Phase 1)
- Azure Key Vault (Phase 2)

### 15.2 Performance Targets

| Metric | Target |
|--------|--------|
| API p95 latency | < 200ms |
| Frontend bundle | < 100KB |
| Container startup | < 30s |

### 15.3 Resource Limits

```yaml
# API
resources:
  requests: { memory: "128Mi", cpu: "100m" }
  limits: { memory: "256Mi", cpu: "500m" }

# Frontend
resources:
  requests: { memory: "64Mi", cpu: "50m" }
  limits: { memory: "128Mi", cpu: "200m" }
```

---

## 16. Testing Strategy

### 16.1 Testing Pyramid

| Level | Coverage | Tools |
|-------|----------|-------|
| Unit | 70% | Jest, pytest |
| Integration | 25% | pytest + test DB |
| E2E | 5% | curl smoke tests |

### 16.2 Running Tests

```bash
# All tests
make test

# API tests with coverage
cd apps/api && poetry run pytest -v --cov=app

# Frontend tests
cd apps/frontend && npm test
```

### 16.3 Test Examples

**Backend:**
```python
@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    response = await client.post("/items", json={"name": "Test"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

**Frontend:**
```typescript
it('renders item name', () => {
  render(<ItemCard item={mockItem} />);
  expect(screen.getByText('Test Item')).toBeInTheDocument();
});
```

---

## 17. Coding Standards

### 17.1 Critical Rules

| Rule | Description |
|------|-------------|
| **Type Safety** | TypeScript strict mode; Pydantic for API I/O |
| **API Calls** | Use service layer, never direct fetch in components |
| **Environment Variables** | Access through config objects only |
| **Error Handling** | Global handlers; consistent error format |
| **Secrets** | Never hardcode; always from environment |
| **Logging** | Structured JSON; include request_id |

### 17.2 Naming Conventions

| Element | Frontend | Backend |
|---------|----------|---------|
| Components | PascalCase | - |
| Hooks | camelCase (`use*`) | - |
| API Routes | - | kebab-case |
| DB Tables | - | snake_case |
| Env Vars | SCREAMING_SNAKE | SCREAMING_SNAKE |

---

## 18. Error Handling Strategy

### 18.1 Error Response Format

```typescript
interface ApiError {
  error: {
    code: string;        // "VALIDATION_ERROR", "NOT_FOUND"
    message: string;     // Human-readable
    details?: object;    // Additional context
    timestamp: string;   // ISO 8601
    requestId: string;   // For log correlation
  };
}
```

### 18.2 HTTP Status Codes

| Status | Usage |
|--------|-------|
| 200 | Success |
| 201 | Created |
| 204 | Deleted (no content) |
| 400 | Bad request |
| 404 | Not found |
| 422 | Validation error |
| 500 | Server error |
| 503 | Service unavailable |

### 18.3 Frontend Handling

```typescript
const { error } = useItems();
if (error) {
  toast.error(handleApiError(error));
}
```

---

## 19. Monitoring and Observability

### 19.1 Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| Metrics | Prometheus | Collection |
| Visualization | Grafana | Dashboards |
| Logs | Loki + Promtail | Aggregation |

### 19.2 Key Metrics

```promql
# Request rate
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# Latency p95
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
```

### 19.3 Grafana Dashboards

**API Dashboard:**
- Request rate (req/s)
- Error rate (%)
- Latency percentiles (p50, p95, p99)
- Requests by endpoint

**Logs Dashboard:**
- Log volume over time
- Error logs filter
- Recent logs stream

---

## 20. Checklist Results Report

### 20.1 Validation Summary

| Category | Status | Notes |
|----------|--------|-------|
| Completeness | ✅ PASS | All PRD requirements addressed |
| Tech Stack | ✅ PASS | All components with versions |
| Data Models | ✅ PASS | Full schema defined |
| API Spec | ✅ PASS | OpenAPI 3.0 included |
| Security | ✅ PASS | Non-root, secrets management |
| Observability | ✅ PASS | Metrics + Logs defined |
| CI/CD | ✅ PASS | GitHub Actions workflow |
| Testing | ✅ PASS | Pyramid with examples |

### 20.2 Executive Summary

| Metric | Value |
|--------|-------|
| **Architecture Completeness** | 95% |
| **PRD Goal Coverage** | 100% (9/9) |
| **Risk Level** | Low |
| **Readiness** | **APPROVED** |

### 20.3 Recommendations

1. Document explicit `helm rollback` commands
2. Add HPA configuration as bonus task
3. Implement alerting rules after observability is stable
4. Consider Playwright for E2E tests post-MVP

---

## Appendix A: Quick Reference

### Key URLs (Local Development)

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3001 |

### Key Commands

```bash
make dev              # Start local stack
make test             # Run tests
make kind-up          # Create K8s cluster
make deploy-local     # Deploy to Kind
make tf-apply         # Apply Terraform
```

---

*Document generated by Architect Winston using BMAD-METHOD*
*Validation Date: 2026-01-26*
