import openai

from config_data.config import Config, load_config

config: Config = load_config()
openai.api_key = config.open_ai.key
engine = 'text-davinci-003'
#engine = 'gpt-3.5-turbo'

def get_answer(prompt):
    try:
        completion = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=0.5,
            max_tokens=1000
        )
        return completion.choices[0]['text']

    except TypeError as error:
        print('Ошибка: ', error)
        return None
