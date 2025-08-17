import ollama

def process_query(query):
    try:
        response = ollama.chat(model="llama3", messages=[
            {"role": "system", "content": "You are Spider-Man. Always reply in a friendly tone. Be brief unless asked for more."},
            {"role": "user", "content": query}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"Sorry, I had a problem thinking: {str(e)}"
