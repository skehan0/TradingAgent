# Python Project Setup Checklist

## Every Time You Start a New Python Project:

### 1. Create Virtual Environment
```bash
cd /path/to/project
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
# OR install individually
pip install httpx openai langsmith etc.
```

### 3. VS Code Setup
- Open VS Code in project directory: `code .`
- Set Python interpreter: `Cmd+Shift+P` → "Python: Select Interpreter"
- Choose `.venv/bin/python`
- Verify status bar shows correct Python version

### 4. Verify Setup
```bash
# Check Python path
which python
# Should show: /path/to/project/.venv/bin/python

# Check packages
pip list
# Should show your installed packages
```

## Troubleshooting

### If imports show as errors:
1. Check status bar - should show `.venv` Python version
2. `Cmd+Shift+P` → "Python: Select Interpreter"
3. `Cmd+Shift+P` → "Developer: Reload Window"
4. Check `.vscode/settings.json` has correct interpreter path

### If terminal doesn't activate venv:
1. Restart VS Code
2. Check `python.terminal.activateEnvironment: true` in settings
3. Manually activate: `source .venv/bin/activate`