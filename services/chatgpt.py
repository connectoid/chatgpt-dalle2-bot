import openai

from config_data.config import Config, load_config

config: Config = load_config()
openai.api_key = config.open_ai.key
#engine = 'text-davinci-003'
engine = 'gpt-3.5-turbo'
role = 'user'
messages = [
    {"role": "system",
     "content" : "You are ChatGPT, "\
     "a large language model trained by OpenAI. Answer as concisely as possible.\n"\
     "Knowledge cutoff: 2022-09-01\nCurrent date: 2023-03-02"},

]


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


def get_answer(prompt):
    try:
        update(messages, "user", prompt)
        completion = openai.ChatCompletion.create(
            model=engine,
            messages=messages,
        )
        print(prompt)
        print('++++++++++++++++++++', completion.choices[0].message.content)
        return completion.choices[0].message.content

    except TypeError as error:
        print('Ошибка: ', error)
        return None

