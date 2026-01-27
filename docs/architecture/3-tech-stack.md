# 3. Tech Stack

This is the **DEFINITIVE** technology selection for the entire project. All development must use these exact technologies and versions.

| Category                    | Technology                   | Version               | Purpose                            | Rationale                                         |
| --------------------------- | ---------------------------- | --------------------- | ---------------------------------- | ------------------------------------------------- |
| **Frontend Language**       | TypeScript                   | 5.x                   | Type-safe frontend development     | Industry standard, catches errors at compile time |
| **Frontend Framework**      | Next.js                      | 15.x                  | React framework with SSR/SSG       | Modern React patterns, easy deployment            |
| **UI Component Library**    | Tailwind CSS                 | 3.x                   | Utility-first styling              | Rapid prototyping, minimal CSS overhead           |
| **State Management**        | React Context + SWR          | 2.x                   | Client state + data fetching       | Lightweight, SWR handles API caching              |
| **Backend Language**        | Python                       | 3.11+                 | API development                    | MLOps pathway, FastAPI ecosystem                  |
| **Backend Framework**       | FastAPI                      | 0.109+                | REST API framework                 | Async-native, auto OpenAPI docs                   |
| **API Style**               | REST                         | OpenAPI 3.0           | API communication                  | Simple, well-understood                           |
| **Database**                | PostgreSQL                   | 15.x                  | Relational data storage            | Robust, SQL standard, excellent K8s support       |
| **Cache**                   | None (MVP)                   | -                     | -                                  | Out of scope for learning project                 |
| **Authentication**          | None (MVP)                   | -                     | -                                  | Out of scope per PRD                              |
| **Frontend Testing**        | Jest + React Testing Library | 29.x / 14.x           | Unit & component tests             | Standard React testing stack                      |
| **Backend Testing**         | pytest + httpx               | 7.x / 0.26+           | Unit & integration tests           | Python standard, async support                    |
| **E2E Testing**             | curl/httpie (smoke tests)    | -                     | Pipeline validation                | Lightweight, sufficient for scope                 |
| **IaC Tool**                | Terraform                    | 1.5+                  | Infrastructure provisioning        | Industry standard, Azure provider                 |
| **CI/CD**                   | GitHub Actions               | -                     | Pipeline automation                | Native GitHub integration, free                   |
| **Container Runtime**       | Docker                       | 24.x                  | Container builds                   | Industry standard, multi-stage builds             |
| **Container Orchestration** | Kubernetes (Kind/AKS)        | 1.28+                 | Container orchestration            | Learning target, production standard              |
| **Package Manager (K8s)**   | Helm + Helmfile              | 3.x / 0.158+          | K8s app packaging                  | Declarative, environment-specific values          |
| **Monitoring**              | Prometheus + Grafana         | kube-prometheus-stack | Metrics collection & visualization | MLOps foundation, industry standard               |
| **Logging**                 | Loki + Promtail              | loki-stack            | Log aggregation                    | Grafana ecosystem, lightweight                    |
| **Ingress Controller**      | NGINX Ingress                | 4.x                   | Traffic routing                    | Most common, well-documented                      |
| **Certificate Management**  | cert-manager                 | 1.13+                 | TLS automation                     | K8s native, Let's Encrypt integration             |
| **Secrets (Phase 1)**       | Kubernetes Secrets           | native                | Basic secret storage               | Learn fundamentals first                          |
| **Secrets (Phase 2)**       | Azure Key Vault + CSI Driver | -                     | Enterprise secrets                 | Production pattern                                |

---
