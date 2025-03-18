import openai
from openai.error import RateLimitError, AuthenticationError

from config_data.config import Config, load_config
from database.orm import get_openai_api_key, disable_openai_api_key

config: Config = load_config()
#openai.api_key = config.open_ai.key
#current_openai_token_string = get_openai_token()
#openai.api_key = current_openai_token_string
#print('dalle', openai.api_key)
#engine = 'text-davinci-003'
#engine = 'gpt-3.5-turbo'

QUOTA_ERROR = 'Текущий API-ключ ChatGPT исчерпал свой лимит, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу.'
AUTH_ERROR = 'Текущий API-ключ ChatGPT не прошел аутентификацию, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу. '\
              'Приносим извинения за неудобства.'

def get_picture(prompt):
    current_openai_api_key = get_openai_api_key()
    openai.api_key = current_openai_api_key
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

    except RateLimitError as error:
        print(QUOTA_ERROR)
        disable_openai_api_key(current_openai_api_key)
        return QUOTA_ERROR
    
    except AuthenticationError as error:
        print(AUTH_ERROR)
        disable_openai_api_key(current_openai_api_key)
        return AUTH_ERROR