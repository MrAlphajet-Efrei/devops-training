"use client";

import { useItems } from "@/hooks/useItems";
import { ItemCard } from "./ItemCard";

export function ItemList() {
  const { items, total, isLoading, isError, refresh } = useItems();

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <p className="text-zinc-500">Loading items...</p>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="flex flex-col items-center justify-center gap-4 py-12">
        <p className="text-red-500">Failed to load items.</p>
        <button
          onClick={() => refresh()}
          className="rounded-md bg-zinc-900 px-4 py-2 text-sm text-white hover:bg-zinc-700 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-300"
        >
          Retry
        </button>
      </div>
    );
  }

  if (items.length === 0) {
    return (
      <div className="flex items-center justify-center py-12">
        <p className="text-zinc-500">No items found.</p>
      </div>
    );
  }

  return (
    <div>
      <p className="mb-4 text-sm text-zinc-500">{total} item(s)</p>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {items.map((item) => (
          <ItemCard key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}
