# Agent Web Layer

An infrastructure layer that converts human-facing websites into clean, structured, and actionable interfaces for AI agents.

## The Problem

The web was built for human eyes. AI agents today either need a website to cooperate (like MCP), or they fumble through messy HTML blindly. Neither works for the 99% of the web that was built purely for visual consumption.

## What This Does

Point it at any URL. It automatically:
- Fetches the page using a real browser
- Strips all the noise (scripts, styles, navigation)
- Extracts what actually matters
- Returns clean structured JSON an agent can act on

## Example Output

```json
{
  "page_type": "category page",
  "site": "Minimalist",
  "key_information": {
    "products": [...],
    "promotions": [...]
  },
  "agent_actions": [
    "Add a product to cart",
    "Navigate to a different category",
    "Search for a specific concern"
  ]
}
```

## How to Run

```bash
git clone https://github.com/userdot01/amazon-agent
cd amazon-agent
pip3 install -r requirements.txt
python3 main.py
```

## Stack

- Python
- Playwright (browser automation)
- BeautifulSoup (HTML parsing)
- Gemini API (semantic extraction)

## Status

Early stage. actively building and improving every day.

## Author

Harsh Mishra — first year CS student building agent infrastructure.