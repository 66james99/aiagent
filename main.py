import os
import sys

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def main(argv):
    print("Hello from aiagent!")

    if len(argv) == 1:
        prompt = argv[0]
    else:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)

        

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)




if __name__ == "__main__":
    main(sys.argv[1:])
