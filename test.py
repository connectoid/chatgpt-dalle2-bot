import openai


messages = [
    {"role": "system",
     "content" : "Привет, расскажи о себе"},
]


current_openai_api_key = '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'
openai.api_key = current_openai_api_key
try:
    print('Completion start')

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    print('Completion finish')

    print(completion['usage']['total_tokens']) 
    print('='*10)
    print('Ответ от ChatGPT:', completion.choices[0].message.content)
    print('Количество токенов:', completion['usage']['total_tokens'])
    print('='*10)
    answer = completion.choices[0].message.content
    print(f'Answeer from gpt: {answer}')
except Exception as e:
    print(f'Error: {e}')
