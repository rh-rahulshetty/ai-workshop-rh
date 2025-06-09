# AI Solutions Workshop #2

This repository contains code for getting started with basic QnA with in-context learning (a prompt engineering technique).

---

## 🧰 Prerequisites

Make sure you have the following installed **before** the workshop:

- Python 3.10+
- VS Code Editor
- kubectl or oc

---

## 🚀 Getting Started

1. **Fork this repository** to your own GitHub account.
2. **Clone your fork** to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-workshop-rh.git
   cd ai-workshop-rh
   ```

3. **Install dependencies:**

   ```bash
   python3 -m venv .venv
   source ./.venv/bin/activate
   pip install -r requirements.txt
   ```
---

## Running Examples

```
export CONTEXT_FILE="./data/contexts/ipl_2025.txt"
# export CONTEXT_FILE="./data/contexts/chess.txt"
# export CONTEXT_FILE="./data/contexts/empty.txt"

python qna.py
```


---

## 💬 Help & Questions

If you get stuck:

- Ask your workshop host or teammates!
- Or open a GitHub Issue if it's repo-related.

