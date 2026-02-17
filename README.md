# Local AI Infrastructure

**Build, Run, and Scale AI on Your Own Hardware**

By Jake Cusack -- [Deepify Academy](https://deepifyai.gumroad.com/)

---

The complete guide to running LLMs locally. Three hardware tiers, full software stack, 8 production patterns with working code. Every platform gotcha documented. 70+ pages, battle-tested on real hardware.

## Chapters

| Chapter | Topic | Examples |
|---------|-------|----------|
| [1. Why Local AI?](chapter-01-why-local-ai/) | Cost analysis, privacy, control | 2 |
| [2. Hardware](chapter-02-hardware/) | Laptop → workstation, ARM64 vs x86 | 3 |
| [3. Software Stack](chapter-03-software-stack/) | Ollama, Open WebUI, vector DBs | 5 |
| [4. Getting Started](chapter-04-getting-started/) | Setup on macOS, Linux, Windows | 8 |
| [5. Ollama Deep Dive](chapter-05-ollama-deep-dive/) | Custom models, API, Python, Docker | 12 |
| [6. Production Patterns](chapter-06-production-patterns/) | 8 patterns with full code | 16 |
| [7. Troubleshooting](chapter-07-troubleshooting/) | 10+ common issues with fixes | 5 |
| [8. What's Next](chapter-08-whats-next/) | Four paths forward | 2 |

## Quick Start

```bash
# 1. Install Ollama (https://ollama.ai)
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Pull a model
ollama pull gemma2:9b

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run your first pattern
cd chapter-06-production-patterns/examples
python3 01_stateless_api.py
```

## The 8 Production Patterns

1. **Stateless API** -- Simple request/response server
2. **Conversational Agent** -- Memory + context management
3. **RAG Pipeline** -- Query your own documents
4. **Tool Use** -- Function calling and actions
5. **Multi-Agent** -- Agents collaborating on tasks
6. **Streaming** -- Real-time token streaming
7. **Model Fallback** -- Chain models for reliability
8. **Batch Processing** -- Process documents at scale

Each pattern includes a complete, runnable example.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.ai) installed
- 8GB+ RAM (16GB recommended)
- macOS, Linux, or Windows (WSL)

No cloud API keys needed. No subscriptions. No recurring costs.

## Get the Ebook

[Buy on Gumroad](https://deepifyai.gumroad.com/) -- £19 (Pay What You Want)

## Also by Jake Cusack

- [Build Your Own AI Agent](https://github.com/DeepifyAI/build-your-own-ai-agent) -- From zero to a working voice-enabled AI agent

---

**Jake Cusack | [Deepify Academy](https://deepify.ai) | [@jakescusack](https://x.com/jakescusack)**
