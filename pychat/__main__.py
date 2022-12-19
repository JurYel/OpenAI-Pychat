import openai
import os
import argparse

OPENAI_API_KEY = "OPENAI_API_KEY"


def main():
    parser = argparse.ArgumentParser(description="PyChat v0.1")
    parser.add_argument("--max-tokens", help="Maximum size of tokens to be used.", type=int, default=4000)
    parser.add_argument("--engine", help="The OpenAI engine to use", type=str, default='text-davinci-003')
    args = parser.parse_args()

    max_tokens = args.max_tokens
    engine = args.engine

    print("Options: ")
    print("max_tokens: {}".format(max_tokens))
    print("engine: {}".fomat(engine))
    
    openpi_api_key = os.getenv(OPENAI_API_KEY)
    if openpi_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    print("PyChat v0.1")
    # openai.api_key = "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"
    query = input("Input: ")

    completion = openai.Completion.create(engine='text-davinci-003', prompt=query, max_tokens=4000)
    output = completion.choices[0].text
    print("Output: {}".format(output))

    
if __name__ == '__main__':
    main()