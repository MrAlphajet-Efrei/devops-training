import { render, screen } from "@testing-library/react";
import { ItemList } from "../ItemList";

jest.mock("@/hooks/useItems");

import { useItems } from "@/hooks/useItems";

const mockUseItems = useItems as jest.MockedFunction<typeof useItems>;

describe("ItemList", () => {
  it("shows loading state", () => {
    mockUseItems.mockReturnValue({
      items: [],
      total: 0,
      isLoading: true,
      isError: false,
      refresh: jest.fn(),
    });

    render(<ItemList />);
    expect(screen.getByText("Loading items...")).toBeInTheDocument();
  });

  it("shows error state", () => {
    mockUseItems.mockReturnValue({
      items: [],
      total: 0,
      isLoading: false,
      isError: true,
      refresh: jest.fn(),
    });

    render(<ItemList />);
    expect(screen.getByText("Failed to load items.")).toBeInTheDocument();
  });

  it("shows items from API", () => {
    mockUseItems.mockReturnValue({
      items: [
        {
          id: "1",
          name: "Item One",
          description: "First item",
          createdAt: "2026-01-01T00:00:00Z",
          updatedAt: "2026-01-01T00:00:00Z",
        },
        {
          id: "2",
          name: "Item Two",
          createdAt: "2026-01-02T00:00:00Z",
          updatedAt: "2026-01-02T00:00:00Z",
        },
      ],
      total: 2,
      isLoading: false,
      isError: false,
      refresh: jest.fn(),
    });

    render(<ItemList />);
    expect(screen.getByText("Item One")).toBeInTheDocument();
    expect(screen.getByText("Item Two")).toBeInTheDocument();
    expect(screen.getByText("2 item(s)")).toBeInTheDocument();
  });

  it("shows empty state when no items", () => {
    mockUseItems.mockReturnValue({
      items: [],
      total: 0,
      isLoading: false,
      isError: false,
      refresh: jest.fn(),
    });

    render(<ItemList />);
    expect(screen.getByText("No items found.")).toBeInTheDocument();
  });
});
