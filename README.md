# ⚡ README Generator

> Free web app — generate professional GitHub READMEs in seconds.
> No login. No API key for users. Powered by Google Gemini (free tier).

## 🗂 Project Structure

```
readme-generator/
├── app.py              ← Flask backend (Gemini API)
├── requirements.txt    ← Dependencies
├── render.yaml         ← One-click deploy to Render.com
└── templates/
    └── index.html      ← Full frontend (single file)
```

## 🚀 Deploy on Render — Free

1. Push this folder to a **new GitHub repo**
2. Go to [render.com](https://render.com) → **New → Web Service**
3. Connect your GitHub repo
4. Render auto-reads `render.yaml`
5. Add environment variable:
   ```
   GEMINI_API_KEY = your-key-here
   ```
6. Click **Deploy** → you get a free public URL 🎉

> Users open the link and use it for free — they never see your key.

## 🔑 Get Gemini API Key (Free)

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** → **Create API key**
3. Copy it — done. No credit card needed.

## 💻 Run Locally

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your-key-here"
python app.py
# Open http://localhost:5000
```

## 👤 Author

Built by [safouane02](https://github.com/safouane02) · MIT License