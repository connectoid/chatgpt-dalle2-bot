import openai

from config_data.config import Config, load_config

config: Config = load_config()
openai.api_key = config.open_ai.key
#engine = 'text-davinci-003'
#engine = 'gpt-3.5-turbo'

def get_picture(prompt):
    try:
        completion = openai.Image.create(
            prompt=prompt,
            n=1,
            #size='256x256'
            size='1024x1024'
        )
        print(completion['data'][0])
        return completion['data'][0]['url']

    except TypeError as error:
        print('Ошибка: ', error)
        return None
