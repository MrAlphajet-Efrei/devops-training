# 14. Deployment Architecture

## 14.1 Deployment Strategy

| Component | Platform | Build Command | Output |
|-----------|----------|---------------|--------|
| Frontend | K8s (Kind/AKS) | `npm run build` | `.next/standalone` |
| API | K8s (Kind/AKS) | Docker build | Container image |

## 14.2 Environments

| Environment | Frontend URL | API URL | Purpose |
|-------------|--------------|---------|---------|
| Development | `localhost:3000` | `localhost:8000` | Local docker-compose |
| Kind | `app.local` | `api.local` | Local K8s |
| Production | `app.example.com` | `api.example.com` | Live |

## 14.3 CI/CD Pipeline

1. **On PR:** Lint, test, build validation
2. **On merge to main:**
   - Build Docker images
   - Push to ACR with SHA tag
   - Deploy to dev environment
   - Run smoke tests
3. **Production:** Manual approval required

---
