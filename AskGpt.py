import openai

openai.api_key = "Your API key here"



def ask_chatgpt(question):
    # Define the messages for the chat-based conversation
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]

    # Generate a response from ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the answer from the response
    answer = response.choices[0].message.content.strip()

    return answer

# Example usage
question = input("Ask a question: ")
answer = ask_chatgpt(question)
print("Answer: " + answer)
