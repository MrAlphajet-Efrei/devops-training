# 15. Security and Performance

## 15.1 Security Requirements

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

## 15.2 Performance Targets

| Metric | Target |
|--------|--------|
| API p95 latency | < 200ms |
| Frontend bundle | < 100KB |
| Container startup | < 30s |

## 15.3 Resource Limits

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
