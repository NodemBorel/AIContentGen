from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Retrieve form data
    topic = request.form.get("topic")
    tone = request.form.get("tone")
    impact = request.form.get("impact")
    desired_length = int(request.form.get("desired_length"))
    word_count = int(request.form.get("word_count"))
    content_style = request.form.get("content_style")
    keywords = request.form.get("keywords")

    # Get API key from environment variable
    api_key = os.getenv("GENAI_API_KEY")

    # Configure Generative AI with API key
    genai.configure(api_key=api_key)
    
    # Generate blog post based on user input
    prompt = f"Hi, put your self as an expert blog writer and create a {tone} blog post about {topic} targeting {impact}. The post should be {desired_length} words in length and written in {content_style} style."
    if keywords:
        prompt += f" Include keywords: {keywords}"
    
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    generated_text = response.text
    
    return render_template("result1.html", generated_text=generated_text)

@app.route("/generate_product_description", methods=["POST"])
def generate_product_description():
    # Retrieve form data
    product_category = request.form.get("product_category")
    product_features = request.form.get("product_features")
    target_audience = request.form.get("target_audience")
    tone_style = request.form.get("tone_style")
    key_features = request.form.get("key_features")
    benefits = request.form.get("benefits")
    use_cases = request.form.get("use_cases")

    # Get API key from environment variable
    api_key = os.getenv("GENAI_API_KEY")

    # Configure Generative AI with API key
    genai.configure(api_key=api_key)

    # Construct the prompt for product description generation
    prompt = f"Create a product description for a {product_category}. "
    prompt += f"The product is designed for {target_audience} and aims to convey a {tone_style} tone.\n\n"
    prompt += "Highlight the following key features:\n"
    prompt += f"- {key_features}\n\n"
    prompt += "Describe the product features in detail, including:\n"
    prompt += f"- {product_features}\n\n"
    prompt += "Emphasize the benefits of the product, including:\n"
    prompt += f"- {benefits}\n\n"
    prompt += "Illustrate the use cases of the product, such as:\n"
    prompt += f"- {use_cases}\n\n"
    prompt += "Craft a concise and engaging product description that captures the essence of the product, resonates with the target audience, and showcases its unique features, benefits, and use cases."

    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    generated_product_description = response.text

    return render_template("result2.html", product_description=generated_product_description)

@app.route("/generate_summary", methods=["POST"])
def generate_summary():
    # Retrieve form data
    text_to_summarize = request.form.get("text_to_summarize")
    summary_length = int(request.form.get("summary_length"))
    summary_focus = request.form.get("summary_focus")

    # Get API key from environment variable
    api_key = os.getenv("GENAI_API_KEY")

    # Configure Generative AI with API key
    genai.configure(api_key=api_key)

    # Construct the prompt for summary generation
    prompt = f"Generate a summary of the given text that focuses on {summary_focus}. "
    prompt += f"The summary should be concise and approximately {summary_length} sentences long.\n\n"
    prompt += "Text to Summarize:\n"
    prompt += f"{text_to_summarize}"

    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    generated_summary = response.text

    return render_template("result3.html", summary=generated_summary)

if __name__ == "__main__":
    app.run(debug=True)
