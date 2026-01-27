# 16. Testing Strategy

## 16.1 Testing Pyramid

| Level | Coverage | Tools |
|-------|----------|-------|
| Unit | 70% | Jest, pytest |
| Integration | 25% | pytest + test DB |
| E2E | 5% | curl smoke tests |

## 16.2 Running Tests

```bash
# All tests
make test

# API tests with coverage
cd apps/api && poetry run pytest -v --cov=app

# Frontend tests
cd apps/frontend && npm test
```

## 16.3 Test Examples

**Backend:**
```python
@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    response = await client.post("/items", json={"name": "Test"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

**Frontend:**
```typescript
it('renders item name', () => {
  render(<ItemCard item={mockItem} />);
  expect(screen.getByText('Test Item')).toBeInTheDocument();
});
```

---
