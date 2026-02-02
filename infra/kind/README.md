# Kind Cluster Setup

Local Kubernetes cluster for development and testing using [Kind](https://kind.sigs.k8s.io/).

## Prerequisites

| Tool | Version | Installation |
|------|---------|--------------|
| Docker | Latest | [docs.docker.com](https://docs.docker.com/get-docker/) |
| Kind | Latest | [kind.sigs.k8s.io](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) |
| kubectl | 1.28+ | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/) |

Verify installation:

```bash
docker --version
kind --version
kubectl version --client
```

## Quick Start

### Create Cluster

```bash
# Using Makefile (recommended)
make kind-create

# Or directly with the script
bash scripts/create-kind-cluster.sh
```

This will:
1. Create a Kind cluster named `devops-demo`
2. Configure Ingress-ready port mappings (80, 443)
3. Install NGINX Ingress Controller
4. Set kubectl context to the new cluster

### Delete Cluster

```bash
# Using Makefile
make kind-delete

# Or directly with the script
bash scripts/create-kind-cluster.sh --delete
```

### Check Cluster Status

```bash
# Using Makefile
make kind-status

# Or manually
kind get clusters
kubectl get nodes
kubectl config current-context
```

## Cluster Configuration

The cluster is configured in `infra/kind/cluster-config.yaml`:

- **Single control-plane node** (sufficient for local development)
- **Ingress-ready label** (`ingress-ready=true`)
- **Port mappings**:
  - Host port 80 → Container port 80 (HTTP)
  - Host port 443 → Container port 443 (HTTPS)

## Loading Local Docker Images

Kind runs Kubernetes inside Docker containers, so it cannot directly access images from your local Docker daemon. You must explicitly load images:

```bash
# Load a single image
kind load docker-image myapp:latest --name devops-demo

# Load multiple images
kind load docker-image devops-api:0.1.0 devops-frontend:0.1.0 --name devops-demo
```

To verify the image is loaded:

```bash
docker exec -it devops-demo-control-plane crictl images | grep myapp
```

## Accessing Services

### Option 1: Port Forward (Simple)

```bash
# Forward a service to localhost
kubectl port-forward svc/my-service 8080:80

# Access at http://localhost:8080
```

### Option 2: Ingress (Production-like)

1. Create an Ingress resource pointing to your service
2. Add hostname to `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts` on Windows):
   ```
   127.0.0.1 app.local api.local
   ```
3. Access via `http://app.local` or `http://api.local`

## NGINX Ingress Controller

The cluster automatically installs the Kind-specific NGINX Ingress Controller.

### Verify Ingress is Running

```bash
# Check pods
kubectl get pods -n ingress-nginx

# Expected output:
# NAME                                        READY   STATUS
# ingress-nginx-controller-xxxxxxxxxx-xxxxx   1/1     Running

# Check service
kubectl get svc -n ingress-nginx
```

### Verify Port Mappings

```bash
docker port devops-demo-control-plane
# Expected:
# 80/tcp -> 0.0.0.0:80
# 443/tcp -> 0.0.0.0:443
```

## Troubleshooting

### Cluster creation fails

```bash
# Check Docker is running
docker ps

# Check for existing cluster
kind get clusters

# Delete and recreate if needed
kind delete cluster --name devops-demo
make kind-create
```

### kubectl context not set

```bash
# List available contexts
kubectl config get-contexts

# Switch to Kind context
kubectl config use-context kind-devops-demo
```

### Ingress not working

```bash
# Check Ingress controller logs
kubectl logs -n ingress-nginx -l app.kubernetes.io/component=controller

# Verify port mappings
docker port devops-demo-control-plane 80
docker port devops-demo-control-plane 443
```

### Image not found in cluster

```bash
# Reload the image
kind load docker-image myapp:latest --name devops-demo

# Verify it's loaded
docker exec devops-demo-control-plane crictl images
```

## Windows Compatibility

This setup works on Windows with:
- **Docker Desktop** with WSL2 backend
- **Git Bash** or **WSL2** for running scripts

If using PowerShell directly, run scripts with:

```powershell
bash scripts/create-kind-cluster.sh
```

For hosts file editing (Ingress hostnames), run your editor as Administrator:

```
C:\Windows\System32\drivers\etc\hosts
```

## Useful Commands Reference

| Task | Command |
|------|---------|
| Create cluster | `make kind-create` |
| Delete cluster | `make kind-delete` |
| Check status | `make kind-status` |
| List clusters | `kind get clusters` |
| Get nodes | `kubectl get nodes` |
| Load image | `kind load docker-image <image> --name devops-demo` |
| Get Ingress pods | `kubectl get pods -n ingress-nginx` |
| View logs | `kubectl logs -n ingress-nginx -l app.kubernetes.io/component=controller` |
| Port forward | `kubectl port-forward svc/<service> <local>:<remote>` |
| Switch context | `kubectl config use-context kind-devops-demo` |
