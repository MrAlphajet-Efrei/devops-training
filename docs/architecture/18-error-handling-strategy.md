# 18. Error Handling Strategy

## 18.1 Error Response Format

```typescript
interface ApiError {
  error: {
    code: string;        // "VALIDATION_ERROR", "NOT_FOUND"
    message: string;     // Human-readable
    details?: object;    // Additional context
    timestamp: string;   // ISO 8601
    requestId: string;   // For log correlation
  };
}
```

## 18.2 HTTP Status Codes

| Status | Usage |
|--------|-------|
| 200 | Success |
| 201 | Created |
| 204 | Deleted (no content) |
| 400 | Bad request |
| 404 | Not found |
| 422 | Validation error |
| 500 | Server error |
| 503 | Service unavailable |

## 18.3 Frontend Handling

```typescript
const { error } = useItems();
if (error) {
  toast.error(handleApiError(error));
}
```

---
