import os
from dotenv import load_dotenv
from google.genai import types, Client

import sys

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = Client(api_key=api_key)

    user_prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    verbose = "--verbose" in args

    generate_content(client=client, messages=messages, verbose=verbose)



def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    prompt_token = response.usage_metadata.prompt_token_count
    response_token = response.usage_metadata.candidates_token_count
    prompt_response_text = response.text

    if verbose:
        print("User prompt:", messages[-1].parts[-1].text)
        print("Prompt tokens:", prompt_token)
        print("Response tokens:", response_token)

    print("Response:")
    print(prompt_response_text)


if __name__ == __name__:
    main()