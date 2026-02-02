.DEFAULT_GOAL := help

.PHONY: help setup-local dev test lint clean kind-create kind-delete kind-status

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