import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
MODEL = os.getenv("CLOUDFLARE_MODEL")

MODEL_ENDPOINT = (
    f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{MODEL}"
)

if not ACCOUNT_ID or not API_TOKEN:
    raise RuntimeError(
        "Set CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN before running this notebook."
    )

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}
payload = {
    "messages": [
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a me a poem about ai agents.",
        },
    ]
}

response = requests.post(MODEL_ENDPOINT, headers=headers, json=payload, timeout=120)
response.raise_for_status()
data = response.json()

result = data.get("result", {})
text = result.get("response") or result.get("output_text") or str(data)
print(text)
