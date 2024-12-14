import openai

openai.api_key = "GPT_API_KEY"

def send_to_gpt(content):
    """
    Sends preprocessed feedback to the GPT API and returns the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Updated to GPT-4
            messages=[{"role": "user", "content": content}],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error communicating with GPT API: {e}")
        return "Error processing feedback"
def batch_send_to_gpt(data):
    # Function logic here
    pass
