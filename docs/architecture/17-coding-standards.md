# 17. Coding Standards

## 17.1 Critical Rules

| Rule | Description |
|------|-------------|
| **Type Safety** | TypeScript strict mode; Pydantic for API I/O |
| **API Calls** | Use service layer, never direct fetch in components |
| **Environment Variables** | Access through config objects only |
| **Error Handling** | Global handlers; consistent error format |
| **Secrets** | Never hardcode; always from environment |
| **Logging** | Structured JSON; include request_id |

## 17.2 Naming Conventions

| Element | Frontend | Backend |
|---------|----------|---------|
| Components | PascalCase | - |
| Hooks | camelCase (`use*`) | - |
| API Routes | - | kebab-case |
| DB Tables | - | snake_case |
| Env Vars | SCREAMING_SNAKE | SCREAMING_SNAKE |

---
