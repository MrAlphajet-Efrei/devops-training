import { Header } from "@/components/layout/Header";
import { ItemList } from "@/components/items/ItemList";

export default function Home() {
  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950">
      <Header />
      <main className="mx-auto max-w-5xl px-6 py-8">
        <ItemList />
      </main>
    </div>
  );
}
