import openai
from openai import RateLimitError, AuthenticationError

from config_data.config import Config, load_config
from database.orm import get_openai_api_key, disable_openai_api_key

TOKEN_ERROR_MESSAGE = f'В данный момент вы использовали максимум токенов в рамках контекста, будет произведена очистка памяти'
MAX_TOKEN_COUNT = 4096
QUOTA_ERROR = 'Текущий API-ключ ChatGPT исчерпал свой лимит, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу.'
AUTH_ERROR = 'Текущий API-ключ ChatGPT не прошел аутентификацию, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу. '\
              'Приносим извинения за неудобства.'

config: Config = load_config()
#openai.api_key = config.open_ai.key
#current_openai_api_key = get_openai_api_key()
#openai.api_key = current_openai_api_key
#print('chatgpt', openai.api_key)
#engine = 'text-davinci-003'
engine = 'gpt-3.5-turbo'
role = 'user'
messages = [
    {"role": "system",
     "content" : "You are ChatGPT, "\
     "a large language model trained by OpenAI. Answer as concisely as possible.\n"\
     "Knowledge cutoff: 2022-09-01\nCurrent date: 2023-03-02"},

]

def change_openai_api_key(open_api_key):
    current_openai_api_key = get_openai_api_key()
    openai.api_key = current_openai_api_key
    print('chatgpt', openai.api_key)


def update(messages, role, content):
    """
    Функция обновления списка сообщений
    """
    messages.append({"role": role, "content": content})
    return messages


def reset_messages():
    """
    Функция очистки истории сообщений контекста, чтобы избежать ошибки с токенами
    """
    messages.clear()
    messages.append({
        "role": "system",
        "content" : "You are ChatGPT, "\
        "a large language model trained by OpenAI. Answer as concisely as possible.\n"\
        "Knowledge cutoff: 2022-09-01\nCurrent date: 2023-03-02"
    })


def get_answer(prompt, user):
    current_openai_api_key = get_openai_api_key()
    openai.api_key = current_openai_api_key
    try:
        update(messages, "user", prompt)
        completion = openai.ChatCompletion.create(
            model=engine,
            messages=messages,
        )
        if completion['usage']['total_tokens'] >= MAX_TOKEN_COUNT:
            reset_messages()
            print(TOKEN_ERROR_MESSAGE, completion['usage']['total_tokens'])
            return TOKEN_ERROR_MESSAGE
        print('='*10)
        print(f'Вопрос пользователя: {user}', prompt)
        print('Ответ от ChatGPT:', completion.choices[0].message.content)
        print('Количество токенов:', completion['usage']['total_tokens'])
        print('='*10)
        return completion.choices[0].message.content

    except TypeError as error:
        print('Ошибка: ', error)
        return error
    
    except RateLimitError as error:
        print(QUOTA_ERROR)
        disable_openai_api_key(current_openai_api_key)
        return QUOTA_ERROR

    except AuthenticationError as error:
        print(AUTH_ERROR)
        disable_openai_api_key(current_openai_api_key)
        return AUTH_ERROR