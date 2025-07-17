# One‑tailed MDE Calculator

Python script that computes the Minimum Detectable Effect for **one‑tailed** A/B tests, prints a 10‑week table, and plots how the MDE shrinks with more traffic.

## Setup

```bash
git clone https://github.com/<your‑user>/one-tailed-mde.git
cd one-tailed-mde
python -m venv .venv && source .venv/bin/activate   # Windows → .venv\Scripts\activate
pip install -r requirements.txt
python mde_one_tailed.py          # edit cr / traffic / split at the top for each new test
