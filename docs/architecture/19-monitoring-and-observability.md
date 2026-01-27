# 19. Monitoring and Observability

## 19.1 Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| Metrics | Prometheus | Collection |
| Visualization | Grafana | Dashboards |
| Logs | Loki + Promtail | Aggregation |

## 19.2 Key Metrics

```promql
# Request rate
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# Latency p95
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
```

## 19.3 Grafana Dashboards

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
