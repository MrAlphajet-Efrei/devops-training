import { Card } from "@/components/ui/Card";
import type { Item } from "@/types/item";

interface ItemCardProps {
  item: Item;
}

export function ItemCard({ item }: ItemCardProps) {
  return (
    <Card>
      <h3 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100">
        {item.name}
      </h3>
      {item.description && (
        <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">
          {item.description}
        </p>
      )}
      <p className="mt-3 text-xs text-zinc-400 dark:text-zinc-500">
        Created: {new Date(item.createdAt).toLocaleDateString()}
      </p>
    </Card>
  );
}
