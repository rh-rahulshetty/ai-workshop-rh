import os
import httpx
from openai import OpenAI

# Load Env variables
model = os.getenv('MODEL_ID')
model_api = os.getenv('MODEL_API') + "/v1"
model_key = os.getenv('USER_KEY')

# Prompt Variables
system_prompt = "You are an helpful AI agent."

user_prompt = """Answer the question based on the context below.

# Context
{context}

# Question
{question}

# Answer:
"""

# Load Context
context_file = os.getenv('CONTEXT_FILE', './data/contexts/ipl_2025.txt')
context = open(context_file, 'r', encoding='utf-8').read()

# Setup OpenAI Client
client = OpenAI(
    base_url=model_api,
    api_key=model_key,
    http_client=httpx.Client(verify=False)  # DO NOT DO THIS IN PRODUCTION!!!!
)


def generate_result(question: str):
    '''
    Run llm inference on user question with given context 
    and print the results inline.
    '''
    # Add context from webpage
    new_user_prompt = user_prompt.format(
        question=question,
        context=context
    )

    # Run LLM Inference
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "assistant", "content": system_prompt},
            {"role": "user", "content": new_user_prompt},
        ],
        max_tokens=64,
    )

    # Show Model Output
    result = completion.choices[0].message.content
    print("Question: ", question)
    print("Answer: ", result)
    print()


print("========== CONTEXT ==========")
print("Length: ", len(context))
if len(context) > 0:
    print("First 300 lines:", context[:300], "...")
print("========== END CONTEXT ==========")

while True:
    try:
        query = input('Enter question on given context (Enter q to exit): ')
        if query.strip().lower() == 'q':
            exit(0)
        generate_result(query)
    except KeyboardInterrupt:
        exit(1)
