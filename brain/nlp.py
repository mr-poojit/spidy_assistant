import requests

OLLAMA_MODEL = "llama3"  # make sure to run: ollama pull llama3

def process_query(query):
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": query, "stream": False},
            timeout=30
        )
        if r.status_code != 200:
            return "Sorry, I had a problem thinking.", "Error: Ollama request failed"

        result = r.json().get("response", "").strip()
        short_reply = result.split(".")[0] + "." if "." in result else result
        return short_reply, result
    except Exception as e:
        return "Sorry, I had a problem thinking.", str(e)
