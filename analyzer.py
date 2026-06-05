# It powers. So its.... Mitochondria
# Fetches the html data, cleans it, gets structured response from Gemini

# Headers
import os
from google import genai
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# Universal Variables
load_dotenv()
client = genai.Client(api_key=os.getenv('dumbeldore'))
MAX_CHARS = 16000


# Getting HTML data. Playwright
def get_page_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        html  = page.content()
        browser.close()
    
    return html


# Getting cleaned html format. Input for Gemini. BeautifulSoup
def clean_html(html):

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "meta", "noscript"]):
        tag.decompose()

    videos = soup.find_all("ytd-playlist-video-renderer")
    if videos:
        text = "\n".join([v.get_text(separator=" ", strip=True) for v in videos])
    else:
        text = soup.get_text()
    
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean_text = "\n".join(lines)
    return clean_text[:MAX_CHARS]


# Getting structured form of HTML data. Gemini doing brain. Returns the result to the user.
def analyze(url):
    html = get_page_html(url)
    text = clean_html(html)

    prompt = f"""
You are an AI that helps agents navigate websites.

Analyze the following webpage content and extract in JSON format:
1. "page_type": what kind of page is this
2. "site": which website is this
3. "key_information": the most important data on this page
4. "agent_actions": the 5 most useful actions an AI agent could take on this page

Only respond with JSON, nothing else.

Page content:
{text}
"""
    
    response = client.models.generate_content(

        model = 'gemini-2.5-flash', 
        contents = prompt
    )

    return response.text