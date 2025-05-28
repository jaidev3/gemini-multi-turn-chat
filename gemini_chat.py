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

    print("\nStarting chat session...")

    # Get the first user input
    user_input1 = input("You (first message): ")

    # Send the first message to the model
    # We don't need to print the first response as per the requirement.
    chat.send_message(user_input1)

    # Get the second user input
    user_input2 = input("You (second message): ")

    # Send the second message to the model
    final_response = chat.send_message(user_input2)

    # Print the final Gemini response (text only)
    if final_response.parts:
        print(f"Gemini: {final_response.text}")
    else:
        print("Gemini: No response received or response was empty.")
        # It can be helpful to see the full response for debugging if it's empty
        # print(f"Full response: {final_response}")

if __name__ == "__main__":
    main() 