import sys
import ollama

path = sys.argv[1]

if path.lower().endswith((".png", ".jpg", ".jpeg")):
    msg = {"role": "user", "content": "Describe this image briefly.", "images": [path]}
else:
    text = open(path).read()
    msg = {"role": "user", "content": "Summarize in 5 bullet points:\n\n" + text}

reply = ollama.chat(model="gemma4:e2b", messages=[msg])
print(reply.message.content)
