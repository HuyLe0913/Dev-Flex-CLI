# 🚀 Dev-Flex CLI

> **Flex your development environment in style.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Style](https://img.shields.io/badge/Style-Cyberpunk-purple)

**Dev-Flex** is a stunning, cyberpunk-themed terminal dashboard designed for developers who want to monitor their system status, check tool versions, and show off their stack with a single command.

---

## ✨ Features

*   **🖥️ System Monitor**: Real-time OS information, Kernel version, Uptime, and Shell detection (Fixed for Windows!).
*   **📊 Hardware Stats**: Live CPU & RAM usage bars to keep an eye on resources.
*   **🛠️ Tech Stack**: Automatically detects versions of **Python**, **Node.js**, **Go**, **Rust**, and **Docker**.
*   **🌐 Network Center**: Displays Local IP, checks Public IP, and runs a **Speedtest** (Ping/Download).
*   **📂 Project Scanner**: Scans your current directory to show file counts by language and total size.
*   **🎨 Multi-Theme**: Choose your vibe: `cyberpunk` (default), `matrix` (hacker green), or `ocean` (calm blue).

## 📦 Installation

Install easily via pip (requires Python 3.9+):

```bash
pip install dev-flex
```
*(Or clone this repo and run `pip install -e .` for editable mode)*

## 🚀 Usage

Simply type `dev-flex` in your terminal:

```bash
dev-flex
```

### Options

| Flag | Description |
| :--- | :--- |
| `--theme [name]` | Switch theme: `cyberpunk`, `matrix`, `ocean`. |
| `--speedtest` | Run an internet speed test (takes a few seconds). |
| `--public` | Fetch and display your Public IP address. |
| `--help` | Show help message. |

### Examples

**The "Hacker" Mode:**
```bash
dev-flex --theme matrix
```

**Full System Report:**
```bash
dev-flex --theme ocean --speedtest --public
```

## 🖼️ Preview

```text
╭───────────────────────────── DEV-FLEX ─────────────────────────────╮
│ ╭─ SYS.INFO ─────────────────────────────────────────────────────╮ │
│ │ 🖥️  Windows 11 Pro • Kernel: 10.0 • ⏱️  2 days • 🐚 powershell    │ │
│ ╰────────────────────────────────────────────────────────────────╯ │
│ ╭─ HARDWARE ─────────────────────────────────────────────────────╮ │
│ │ CPU [||||||||||........] 50%   RAM [||||||.............] 6.2GB │ │
│ ╰────────────────────────────────────────────────────────────────╯ │
... and much more!
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues/PRs to add support for more tools or themes.

---
*Built with ❤️ using [Rich](https://github.com/Textualize/rich) and [Typer](https://github.com/tiangolo/typer).*