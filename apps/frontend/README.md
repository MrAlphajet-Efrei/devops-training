# DevOps Path - Frontend

React/Next.js frontend for the DevOps Path application. Displays items fetched from the backend API.

## Prerequisites

- Node.js 18+
- npm

## Installation

```bash
cd apps/frontend
npm install
```

## Environment Variables

Copy the example file and adjust as needed:

```bash
cp .env.local.example .env.local
```

| Variable | Default | Description |
|---|---|---|
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Backend API URL |

## Running Locally

```bash
npm run dev
```

Opens at [http://localhost:3000](http://localhost:3000).

## Available Scripts

| Script | Description |
|---|---|
| `npm run dev` | Start development server (Turbopack) |
| `npm run build` | Create production build |
| `npm start` | Start production server |
| `npm run lint` | Run ESLint |

## Docker

```bash
# Build
docker build -t devops-frontend:0.1.0 .

# Run
docker run -d -p 3000:3000 devops-frontend:0.1.0

# Verify
curl http://localhost:3000
```

The image uses a 3-stage build (deps, builder, runner) with `node:20-alpine` and standalone output. Runs as non-root user `nextjs`.

## Tech Stack

- Next.js 16 (App Router, Turbopack)
- React 19
- TypeScript 5
- Tailwind CSS 4
- SWR 2 (data fetching)
