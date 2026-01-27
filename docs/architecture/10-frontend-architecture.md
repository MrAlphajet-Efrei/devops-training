# 10. Frontend Architecture

## 10.1 Component Organization

```
apps/frontend/src/
├── app/                    # Next.js App Router
│   ├── layout.tsx
│   ├── page.tsx
│   ├── loading.tsx
│   └── error.tsx
├── components/
│   ├── ui/                 # Generic UI components
│   ├── items/              # Feature components
│   └── layout/             # Layout components
├── hooks/                  # Custom React hooks
├── services/               # API client layer
├── types/                  # TypeScript types
└── lib/                    # Utilities
```

## 10.2 State Management

- **Server State:** SWR handles all API data with caching
- **UI State:** Local `useState` for component state
- **No global state manager needed** for this simple app

## 10.3 API Client

```typescript
// src/services/api.ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '/api';

export async function apiClient<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!response.ok) throw new Error('API error');
  return response.json();
}
```

## 10.4 SWR Hook Example

```typescript
// src/hooks/useItems.ts
import useSWR from 'swr';
import { itemsService } from '@/services/items';

export function useItems() {
  const { data, error, isLoading, mutate } = useSWR('/items', () => itemsService.list());
  return {
    items: data?.items ?? [],
    total: data?.total ?? 0,
    isLoading,
    isError: !!error,
    refresh: mutate,
  };
}
```

---
