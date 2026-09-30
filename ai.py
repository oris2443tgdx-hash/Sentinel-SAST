import sys
from openai import OpenAI

api_key = "YOUR_OPENROUTER_API_KEY_HERE"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
api_key = "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"
)

print("--- AI CMD Assistant Ready! ---")
print("Type 'exit' or 'quit' to close.\n")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    try:
        user_input = input("You > ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if not user_input.strip():
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
        )

        reply = response.choices[0].message.content
        print(f"\nAI > {reply}\n")

        messages.append({"role": "assistant", "content": reply})

    except KeyboardInterrupt:
        print("\nSession ended.")
        break
    except Exception as e:
        print(f"\nError: {e}\n")
