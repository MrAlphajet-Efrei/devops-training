import { render, screen } from "@testing-library/react";
import { ItemCard } from "../ItemCard";
import type { Item } from "@/types/item";

const mockItem: Item = {
  id: "1",
  name: "Test Item",
  description: "A test description",
  createdAt: "2026-01-01T00:00:00Z",
  updatedAt: "2026-01-01T00:00:00Z",
};

describe("ItemCard", () => {
  it("renders item name", () => {
    render(<ItemCard item={mockItem} />);
    expect(screen.getByText("Test Item")).toBeInTheDocument();
  });

  it("renders item description", () => {
    render(<ItemCard item={mockItem} />);
    expect(screen.getByText("A test description")).toBeInTheDocument();
  });

  it("renders without description when not provided", () => {
    const itemWithoutDesc: Item = { ...mockItem, description: undefined };
    render(<ItemCard item={itemWithoutDesc} />);
    expect(screen.getByText("Test Item")).toBeInTheDocument();
    expect(screen.queryByText("A test description")).not.toBeInTheDocument();
  });
});
