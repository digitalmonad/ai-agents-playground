# AI agents playground

This project includes a simple examples for calling Cloudflare Workers AI from Python.

## Setup

1. Create a Cloudflare account and enable Workers AI.
    First, you'll need a Cloudflare API Token. You can generate one from your Cloudflare dashboard (under "My Profile" > "API Tokens").
    Important: Store your API token securely.
2. Find your Cloudflare account ID.
3. In Colab, you can use the Secrets Manager (the 🔑 icon on the left panel) to set the env variables.

```bash
export CLOUDFLARE_ACCOUNT_ID="your-account-id"
export CLOUDFLARE_API_TOKEN="your-api-token"
export CLOUDFLARE_MODEL="@cf/meta/llama-3.1-8b-instruct"
```
