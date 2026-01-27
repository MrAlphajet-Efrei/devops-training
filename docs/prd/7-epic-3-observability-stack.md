# 7. Epic 3: Observability Stack

**Goal:** Implement production-grade observability with metrics and logging. This epic delivers complete visibility into application health and behavior through Prometheus for metrics collection, Grafana for visualization, and Loki for centralized logging. The observability stack enables proactive monitoring and efficient troubleshooting—critical skills for MLOps where model monitoring follows similar patterns.

## Story 3.1: Deploy Prometheus & Grafana via Helm

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

## Story 3.2: Instrument API with Prometheus Metrics

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

## Story 3.3: Configure Prometheus ServiceMonitor

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

## Story 3.4: Create Custom Grafana Dashboard for API

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

## Story 3.5: Deploy Loki & Promtail for Log Aggregation

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

## Story 3.6: Configure Grafana Loki Datasource

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

## Story 3.7: Create Logs Dashboard in Grafana

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

## Story 3.8: Structured Logging in API

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
