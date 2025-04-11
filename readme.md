# Reels Downloader CLI 🎬

A clean and lightweight command-line tool to download public Instagram Reels or Posts.  
It saves only the `.mp4` video and the original caption in a `.txt` file.

---

## ✨ Features

- Downloads public Instagram Reels or Posts
- Saves:
  - ✅ `.mp4` video
  - ✅ `.txt` caption (with ending note)
- Filenames are:
  - Lowercased
  - Stripped of special characters
  - Spaces replaced with underscores
- `.txt` files end with a legal-safe note
- All metadata and unwanted files are removed

---

## 📦 Example Output

downloads/
├── @catlover-my_cat_learned_to_open_the_fridge.mp4
└── @catlover-my_cat_learned_to_open_the_fridge_video_description.txt

**Text file content:**

my cat just learned to open the fridge. chaos followed.

This is the original caption from the video creator.

---

## ⚙️ Installation

Requires Python 3.7+

```bash
pip install instaloader
```


⸻

## 🚀 Usage

python3 main.py <REEL_OR_POST_URL> -o <OUTPUT_FOLDER>

Example:

python3 main.py https://www.instagram.com/reel/Cw4iJZrN123/ -o ./downloads



⸻

## ⚖️ Disclaimer

This tool is intended for educational and personal use only.

Downloading content from Instagram (Meta Platforms, Inc.) may violate their Terms of Use.
All downloaded content remains the intellectual property of its respective creators.

You are solely responsible for ensuring that your use of this tool complies with applicable laws, copyright regulations, and Instagram’s policies.

This project is not affiliated with, associated with, or endorsed by Instagram or Meta Platforms, Inc.

⸻

## 🧠 To-Do Ideas
	•	Download multiple Reels from a .txt list
	•	Support for private content with login
	•	Download from user profile
	•	Telegram/Discord bot
	•	GUI version

⸻

## 📄 License

MIT License — You can use, copy, modify, and distribute this tool.
However, misuse of this tool is your own legal responsibility. Don’t be a jerk.

⸻

## ✍️ Credits

Built by galvanotrip
