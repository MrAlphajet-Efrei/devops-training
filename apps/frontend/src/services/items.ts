import { apiClient } from "./api";
import type { Item, ItemListResponse, CreateItemRequest } from "@/types/item";

export const itemsService = {
  list: () => apiClient<ItemListResponse>("/items"),
  getById: (id: string) => apiClient<Item>(`/items/${id}`),
  create: (data: CreateItemRequest) =>
    apiClient<Item>("/items", {
      method: "POST",
      body: JSON.stringify(data),
    }),
};
