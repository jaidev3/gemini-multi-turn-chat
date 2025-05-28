import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="add your api here")

def main():
    # Get model parameters from the user
    temperature_str = input("Enter temperature (e.g., 0.7, leave blank for default(0.9)): ")
    temperature = None
    if temperature_str:
        try:
            temperature = float(temperature_str)
        except ValueError:
            print("Invalid temperature value. Using default.")

    generation_config = genai.types.GenerationConfig(
        temperature=temperature if temperature is not None else 0.9 # Default to 0.9 if not provided or invalid
    )

    # Initialize the model
    # Using a generally available model that supports chat, like 'gemini-1.5-flash-latest'
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config=generation_config
    )

    # Start a chat session
    chat = model.start_chat(history=[])

    print("\nConversation  . Type 'quit' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting chat.")
            break

        # Send message to the model
        response = chat.send_message(user_input)

        # Print the Gemini response (text only)
        if response.parts:
            print(f"Gemini: {response.text}")
        else:
            print("Gemini: No response received or response was empty.")
            # It can be helpful to see the full response for debugging if it's empty
            # print(f"Full response: {response}")

if __name__ == "__main__":
    main() 