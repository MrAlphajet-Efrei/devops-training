#!/bin/bash
set -euo pipefail

#############################
# VARIABLES
#############################
CLUSTER_NAME="devops-demo"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/../infra/kind/cluster-config.yaml"

#############################
# FONCTIONS
#############################

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --help, -h     Show this help message"
    echo "  --delete, -d   Delete the cluster"
    echo ""
    echo "Without options, creates the cluster and installs NGINX Ingress."
}

check_prerequisites() {
    command -v kind >/dev/null 2>&1 || { echo "kind is not installed. Please install kind to proceed."; exit 1; }
    command -v kubectl >/dev/null 2>&1 || { echo "kubectl is not installed. Please install kubectl to proceed."; exit 1; }
    command -v docker >/dev/null 2>&1 || { echo "Docker is not installed. Please install Docker to proceed."; exit 1; }
}

create_cluster() {
    echo "Creating kind cluster '${CLUSTER_NAME}'..."
    if kind get clusters 2>/dev/null | grep -q "^${CLUSTER_NAME}$"; then
        echo "Cluster '${CLUSTER_NAME}' already exists. Skipping creation."
        return 0
    fi    
    kind create cluster --name "${CLUSTER_NAME}" --config "${CONFIG_FILE}"
    EXPECTED_CONTEXT="kind-${CLUSTER_NAME}"
    CURRENT_CONTEXT=$(kubectl config current-context)
    if [[ "${CURRENT_CONTEXT}" != "${EXPECTED_CONTEXT}" ]]; then
        echo "Warning: Context is '$CURRENT_CONTEXT', expected '$EXPECTED_CONTEXT'"
    fi
}

install_ingress() {
    echo "Installing NGINX Ingress Controller..."
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
    kubectl wait --namespace ingress-nginx \
    --for=condition=ready pod \
    --selector=app.kubernetes.io/component=controller \
    --timeout=120s
    echo "NGINX Ingress Controller installed successfully."
}

delete_cluster() {
    echo "Deleting kind cluster '${CLUSTER_NAME}'..."
    kind get clusters 2>/dev/null | grep -q "^${CLUSTER_NAME}$" || { echo "Cluster '${CLUSTER_NAME}' does not exist."; return 0; }
    kind delete cluster --name "${CLUSTER_NAME}"
    echo "Cluster '${CLUSTER_NAME}' deleted successfully."
}

#############################
# MAIN
#############################

check_prerequisites

case "${1:-}" in
    --delete|-d)
        delete_cluster
        ;;
    --help|-h)
        usage
        ;;
    *)
        create_cluster
        install_ingress
        echo "Kind cluster '${CLUSTER_NAME}' is ready for use."
        ;;
esac