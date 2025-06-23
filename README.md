# chumdump 🦈

> Obfuscate. Pollute. Evaporate.  
> A privacy-first CLI to poison behavioral data trails before deletion.

## 🧠 Overview

**chumdump** is a Python-based command-line tool that helps you obscure your digital footprint before wiping it out. It simulates realistic (but fake) user behavior, scrambles metadata, and can optionally perform deletions—all to make behavioral profiling and surveillance harder.

## 🖥️ Commands

- `bait` — Seeds fake activity on social platforms
- `scramble` — Injects noise into behavioral data (DNS, browser history, etc.)
- `purge` — Obfuscates then deletes social/media/identity data
- `vanish` — Full wipe and optional tool self-destruction

## 🚀 Getting Started

```bash
# Clone this repo
git clone https://github.com/m3lixir/chumdump.git
cd chumdump

# Install dependencies
pip install -r requirements.txt

# Run CLI
python chumdump.py --help
```

## 🧪 Example Usage

```bash
python chumdump.py bait --target reddit --intensity high
python chumdump.py scramble --dns --webhistory --window 30d
```

## 📂 Project Structure

```
chumdump/
├── chumdump.py         # CLI entrypoint
├── modules/
│   ├── bait.py         # Adds fake interactions
│   ├── scramble.py     # Injects behavioral noise
│   ├── purge.py        # Deletes data/accounts
│   └── vanish.py       # Secure wipe
├── data/
│   └── personas/       # Optional persona templates
├── utils.py            # Shared utilities
├── requirements.txt
└── README.md
```

## 🔐 License

MIT — do whatever you want, just don't sue.
