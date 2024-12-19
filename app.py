from flask import Flask, request, jsonify, send_file
from openai import OpenAI
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# Put your API key here
openai_api_key = "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"  # Replace this with your OpenAI API key

# Directory for saving PDFs
OUTPUT_DIR = "ebooks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_ebook(description, title):
    """Generates an eBook using OpenAI and creates a PDF."""
    content = "Generated content here for simplicity"

    # Save to PDF
    filename = os.path.join(OUTPUT_DIR, f"{title}.pdf")
    c = canvas.Canvas(filename)
    c.drawString(100, 800, title)
    y = 780
    for line in content.split("\n"):
        c.drawString(100, y, line)
        y -= 15
    c.save()

    return filename

@app.route("/", methods=["GET"])
def home():
    return "Your eBook Generator is Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400
    file_path = generate_ebook(description, title)
    return jsonify({"message": "eBook generated", "file": file_path})

if __name__ == "__main__":
    app.run(debug=True)
