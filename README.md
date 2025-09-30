# 🤖 AI Trading Agent

An intelligent trading agent that analyzes AI/technology news and provides actionable market insights using advanced language models.

## 🚀 Features

- **📰 News Analysis**: Fetches and analyzes AI-related news articles
- **🧠 AI-Powered Insights**: Uses Perplexity AI for market analysis
- **📧 Email Reports**: Automated email delivery of analysis reports
- **📊 LangSmith Tracing**: Complete observability of AI operations
- **🏗️ Modular Architecture**: Clean, maintainable codebase

## 🛠️ Setup

### 1. Clone and Install

```bash
git clone https://github.com/skehan0/TradingAgent.git
cd TradingAgent
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r .requirements.txt
```

### 2. Configure Environment

Create `.env` and fill in your API keys:

```bash
# Edit .env with your actual API keys
```

Required API keys:
- **News API**: For fetching news articles
- **Perplexity API**: For AI analysis ($5/month)
- **LangSmith API**: For tracing and monitoring
- **Mailgun API**: For email delivery (optional)

## Usage

### Command Line Options

```bash
# Basic analysis (console output)
python src/main.py
```

## 🏗️ Architecture

```
src/
├── main.py              # Main application entry point
├── services/
│   ├── news.py          # News fetching service
│   ├── analysis.py      # AI analysis service
│   ├── llm.py          # Language model interface
│   └── mail.py         # Email service
└── architecture.py      # LangGraph workflow (future)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `NEWS_API_KEY` | News API key | Yes |
| `PERPLEXITY_API_KEY` | Perplexity AI API key | Yes |
| `LANGSMITH_API_KEY` | LangSmith API key | Yes |
| `MAILGUN_API_KEY` | Mailgun API key | No* |
| `MAILGUN_DOMAIN` | Mailgun domain | No* |
| `EMAIL_RECIPIENTS` | Comma-separated email list | No* |

*Required only for email functionality

### Scheduling

Set up automated daily reports using cron:

```bash
crontab -e

# Run daily at 7 AM
0 7 * * * cd /path/to/TradingAgent && .venv/bin/python src/main.py --email --quiet

press esc

Type: :wq and press enter
```

## Monitoring

View detailed execution traces and performance metrics in your [LangSmith dashboard](https://smith.langchain.com/).

## Disclaimer

This tool provides AI-generated market analysis for informational purposes only. It is not financial advice. Always conduct your own research and consult with financial professionals before making investment decisions.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
