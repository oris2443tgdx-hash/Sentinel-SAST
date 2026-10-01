# Sentinel SAST

A lightweight static application security testing (SAST) tool designed to scan Python codebases for security vulnerabilities, hardcoded secrets, and unsafe execution patterns.

## Features
- **Static Analysis:** Scans code for dangerous functions (`eval()`, `exec()`, unsafe subprocess calls).
- **Secret Detection:** Flags exposed API keys, tokens, and credentials before deployment.
- **Local AI Integration:** Interfaces with local Ollama models and OpenRouter for automated vulnerability remediation suggestions.

## Core Files
- `sentinel.py` - Main scanner engine and AST parser.
- `ai.py` - Integration script for local/remote LLM security analysis.
- `requirements.txt` - Project dependencies.

## Usage
Run the scanner locally against target Python files:
```bash
python sentinel.py
