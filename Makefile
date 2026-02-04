.DEFAULT_GOAL := help

.PHONY: help setup-local dev test lint clean kind-create kind-delete kind-status k8s-deploy k8s-delete k8s-status k8s-load-images k8s-port-forward

## help: Show this help message
help:
	@echo "Available commands:"
	@echo ""
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/## /  /'
	@echo ""

## setup-local: Set up local development environment
setup-local:
	@echo "Setting up local development environment..."
	@cp -n .env.example .env 2>/dev/null || true
	@echo "Local setup complete. Edit .env as needed."

## dev: Start development environment with Docker Compose
dev:
	docker compose up --build

## test: Run all tests
test:
	@echo "Running tests..."
	@echo "TODO: Add test commands for frontend and backend"

## lint: Run linters across the project
lint:
	@echo "Running linters..."
	@echo "TODO: Add linting commands for frontend and backend"

## clean: Clean up generated files and containers
clean:
	@echo "Cleaning up..."
	docker compose down -v --remove-orphans 2>/dev/null || true
	@echo "Cleanup complete."

SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SCRIPT_CREATE_KIND := $(SCRIPT_DIR)scripts/create-kind-cluster.sh

## kind-create: Create a Kind cluster
kind-create:
	@bash $(SCRIPT_CREATE_KIND)

## kind-delete: Delete the Kind cluster
kind-delete:
	@bash $(SCRIPT_CREATE_KIND) --delete

## kind-status: Check the status of the Kind cluster
kind-status:
	@echo "=== Kind Cluster Status ==="
	@kind get clusters 2>/dev/null || echo "No Kind cluster running"
	@echo ""
	@echo "=== Kubernetes Nodes ==="
	@kubectl get nodes 2>/dev/null || echo "No Kind nodes running"
	@echo ""
	@echo "=== Kubernetes Contexts ==="
	@kubectl config get-contexts 2>/dev/null || echo "No Kubernetes contexts available"
	@echo "=========================="

k8s-deploy:
	@echo "Deploying to Kind cluster..."
	@kubectl apply -k infra/k8s/base/
	@echo "Deployment complete."

k8s-delete:
	@echo "Deleting deployment from Kind cluster..."
	@kubectl delete -k infra/k8s/base/ --ignore-not-found
	@echo "Deletion complete."

k8s-status:
	@echo "=== Kubernetes Pods ==="
	@kubectl get all -n devops-demo
	@echo "======================="

k8s-load-images:
	@echo "Loading Docker images into Kind cluster..."
	@kind load docker-image devops-frontend:0.1.0 --name devops-demo
	@kind load docker-image devops-api:0.1.0 --name devops-demo
	@echo "Images loaded."

k8s-port-forward:
	@echo "Port forwarding services..."
	@kubectl port-forward svc/frontend 3000:3000 -n devops-demo &
	@kubectl port-forward svc/api 8000:8000 -n devops-demo &
	@echo "Port forwarding set up. Frontend: http://localhost:3000, API: http://localhost:8000"