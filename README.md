# Research Papers API

Academic papers API for AI agents. Pay $0.05 per paper — no subscription needed.

Browse and search 20 landmark AI/ML papers for free. Pay $0.05 via [Mainlayer](https://mainlayer.xyz) to unlock the full text of any paper. Perfect for research agents that need to read papers on demand without managing subscriptions.

---

## How it works

1. **Browse for free** — list all papers, search by keyword, get abstracts
2. **Pay per paper** — $0.05 unlocks the full text of a single paper
3. **Your agent pays automatically** — Mainlayer handles the payment flow; your agent just needs a wallet

No API keys needed for free endpoints. No subscription. No bulk commitments.

---

## Quick start

```bash
# Clone and install
git clone https://github.com/your-org/research-papers-api.git
cd research-papers-api

cp .env.example .env
# Add your MAINLAYER_API_KEY to .env

pip install -r requirements.txt
uvicorn src.main:app --reload
```

Or with Docker:

```bash
docker compose up
```

The API is now available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

---

## API reference

Base URL: `https://your-deployment.example.com`

### Free endpoints

#### List all papers

```
GET /papers
```

Returns id, title, authors, abstract, category, and price for every paper.

```bash
curl https://your-deployment.example.com/papers
```

```json
[
  {
    "id": "paper-001",
    "title": "Attention Is All You Need",
    "authors": [{"name": "Ashish Vaswani", "affiliation": "Google Brain"}],
    "abstract": "The dominant sequence transduction models...",
    "year": 2017,
    "category": "machine-learning",
    "price_usd": 0.05,
    "doi": "10.48550/arXiv.1706.03762"
  }
]
```

---

#### Search papers

```
GET /papers/search?q={query}
```

Searches title, abstract, keywords, authors, and category. Case-insensitive.

```bash
curl "https://your-deployment.example.com/papers/search?q=transformer"
```

```json
{
  "query": "transformer",
  "total": 4,
  "papers": [...]
}
```

---

#### Paper detail

```
GET /papers/{id}
```

Returns full metadata including keywords and citation count. Does not include full text.

```bash
curl https://your-deployment.example.com/papers/paper-001
```

```json
{
  "id": "paper-001",
  "title": "Attention Is All You Need",
  "keywords": ["transformers", "attention", "NLP"],
  "citations": 98412,
  "journal": "NeurIPS 2017",
  ...
}
```

---

#### List categories

```
GET /categories
```

Returns all paper categories with paper counts.

```bash
curl https://your-deployment.example.com/categories
```

```json
[
  {
    "id": "machine-learning",
    "name": "Machine Learning",
    "description": "Core machine learning algorithms, theory, and applications.",
    "paper_count": 5
  }
]
```

---

### Paid endpoint — $0.05 per paper

#### Get full paper text

```
GET /papers/{id}/full
```

**Requires** the `X-Payer-Wallet` header with your Mainlayer wallet ID.

**Cost**: $0.05 per paper access.

```bash
curl https://your-deployment.example.com/papers/paper-001/full \
  -H "X-Payer-Wallet: your-wallet-id"
```

**Success (200)**

```json
{
  "id": "paper-001",
  "title": "Attention Is All You Need",
  "full_text": "# Attention Is All You Need\n\n## 1. Introduction\n\n...",
  ...
}
```

**Payment required (402)**

If you haven't paid yet, you receive:

```json
{
  "error": "payment_required",
  "message": "Payment of $0.05 required to access 'Attention Is All You Need'...",
  "price_usd": 0.05,
  "paper_id": "paper-001",
  "payment_url": "https://api.mainlayer.xyz/pay?resource_id=paper-001&price_usd=0.05"
}
```

Your agent should navigate to `payment_url`, complete the Mainlayer payment flow, then retry the original request.

---

## For AI agents

This API is designed to be used autonomously by AI research agents:

1. **Discover** — call `GET /papers` or `GET /papers/search?q=your-topic`
2. **Preview** — call `GET /papers/{id}` to read the abstract
3. **Pay and read** — call `GET /papers/{id}/full` with `X-Payer-Wallet`; follow the `payment_url` in the 402 if not yet paid
4. **Retry** — after payment, re-issue `GET /papers/{id}/full` to receive the full text

Payment is handled by [Mainlayer](https://mainlayer.xyz) — payment infrastructure for AI agents.

---

## Available papers

| ID | Title | Category | Year |
|----|-------|----------|------|
| paper-001 | Attention Is All You Need | machine-learning | 2017 |
| paper-002 | BERT | natural-language-processing | 2018 |
| paper-003 | Deep Residual Learning (ResNet) | computer-vision | 2016 |
| paper-004 | Generative Adversarial Networks | machine-learning | 2014 |
| paper-005 | Dropout | machine-learning | 2014 |
| paper-006 | Adam Optimizer | optimization | 2014 |
| paper-007 | Playing Atari with DRL (DQN) | reinforcement-learning | 2013 |
| paper-008 | AlphaGo | reinforcement-learning | 2016 |
| paper-009 | GPT-3 (Few-Shot Learners) | natural-language-processing | 2020 |
| paper-010 | Vision Transformer (ViT) | computer-vision | 2020 |
| paper-011 | Denoising Diffusion (DDPM) | generative-models | 2020 |
| paper-012 | InstructGPT (RLHF) | natural-language-processing | 2022 |
| paper-013 | Retrieval-Augmented Generation (RAG) | natural-language-processing | 2020 |
| paper-014 | Scaling Laws | machine-learning | 2020 |
| paper-015 | PPO | reinforcement-learning | 2017 |
| paper-016 | ImageNet (ILSVRC) | computer-vision | 2015 |
| paper-017 | DALL-E 2 | generative-models | 2022 |
| paper-018 | Neural Architecture Search | machine-learning | 2016 |
| paper-019 | Constitutional AI | ai-safety | 2022 |
| paper-020 | Toolformer | natural-language-processing | 2023 |

---

## Development

```bash
# Run tests
pytest tests/ -v --cov=src

# Lint
ruff check src/ tests/

# Build image
docker build -t research-papers-api .
```

---

## Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MAINLAYER_API_KEY` | Yes | — | Your Mainlayer API key |
| `MAINLAYER_BASE_URL` | No | `https://api.mainlayer.xyz` | Mainlayer API base URL |
| `PORT` | No | `8000` | Server port |
| `ENV` | No | `production` | Set to `development` for hot reload |

---

## License

MIT
