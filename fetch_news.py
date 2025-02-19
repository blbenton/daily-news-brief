import openai  # Required to communicate with ChatGPT

# Replace with your OpenAI API key if running this locally
openai.api_key = "YOUR_OPENAI_API_KEY"

# Request the news summary
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "system", "content": "Generate today's news summary in the usual format."}]
)

news_summary = response["choices"][0]["message"]["content"]

# Save to a text file
with open("news_summary.txt", "w", encoding="utf-8") as file:
    file.write(news_summary)
