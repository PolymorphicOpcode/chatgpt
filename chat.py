#!/usr/bin/env python3

import openai
openai.api_key = "PUT-YOUR-API-KEY-FROM-THE-WEBSITE"

model_engine = "gpt-3.5-turbo-0301"
completion = openai.Completion.create(engine = model_engine,
    prompt = input("Prompt: "),
    max_tokens = 2048, #how long the response can be
    temperature = 0.8 # 0-2 rating, is kind of like variability of answers
)
message = completion.choices[0].text
print(message)
