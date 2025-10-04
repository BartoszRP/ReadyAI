from dotenv import load_dotenv

load_dotenv()


import replicate

input = {
    "prompt": "Jaka jest stolica Polski?"
}

for event in replicate.stream(
    "deepseek-ai/deepseek-r1",
    input=input
):
    print(event, end="")