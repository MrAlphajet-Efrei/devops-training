# 5. API Specification

## 5.1 REST API Specification (OpenAPI 3.0)

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

## 5.2 API Endpoints Summary

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
