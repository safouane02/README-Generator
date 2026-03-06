"""
README Generator — Flask Web App
Uses Google Gemini API (Free Tier — no credit card needed)

Author: safouane02
GitHub: https://github.com/safouane02
"""

import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure Gemini with the API key from environment
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def build_prompt(data: dict) -> str:
    return f"""You are an expert open-source developer. Generate a professional, human-written GitHub README.md.

Project details:
- Name: {data['name']}
- Description: {data['description']}
- Tech Stack: {data['tech']}
- Key Features: {data['features']}
- Installation: {data['install']}
- License: {data.get('license', 'MIT')}
- Author: {data['author']}

Requirements:
- Write in fluent, natural English as a real senior developer would
- Include these sections IN ORDER:
  1. Title with emoji + shields.io badges (build passing, license, version)
  2. One-line motivating tagline in italic
  3. Table of Contents
  4. About / Overview (2-3 sentences)
  5. Features (bullet list with emojis)
  6. Installation (with code blocks)
  7. Usage (with example code blocks)
  8. Contributing
  9. License
  10. Author / Contact
- Use GitHub Flavored Markdown
- Sound like a real passionate developer wrote it, not an AI
- Output ONLY the raw markdown, nothing else, no explanations
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    # Validate required fields
    required = ["name", "description", "tech", "features", "install", "author"]
    for field in required:
        if not data.get(field, "").strip():
            return jsonify({"error": f"Field '{field}' is required."}), 400

    try:
        response = model.generate_content(build_prompt(data))
        readme = response.text

        # Strip markdown code fences if Gemini wraps the output
        if readme.startswith("```"):
            lines = readme.splitlines()
            readme = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

        return jsonify({"readme": readme})

    except Exception as e:
        return jsonify({"error": f"Generation failed: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)