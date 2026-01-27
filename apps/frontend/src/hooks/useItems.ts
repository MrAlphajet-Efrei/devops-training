import useSWR from "swr";
import { itemsService } from "@/services/items";

export function useItems() {
  const { data, error, isLoading, mutate } = useSWR("/items", () =>
    itemsService.list(),
  );

  return {
    items: data?.items ?? [],
    total: data?.total ?? 0,
    isLoading,
    isError: !!error,
    refresh: mutate,
  };
}
