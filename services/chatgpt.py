from openai import OpenAI
from openai import RateLimitError, AuthenticationError

from database.orm import get_openai_api_key, disable_openai_api_key


TOKEN_ERROR_MESSAGE = f'В данный момент вы использовали максимум токенов в рамках контекста, будет произведена очистка памяти'
MAX_TOKEN_COUNT = 4096
QUOTA_ERROR = 'Текущий API-ключ ChatGPT исчерпал свой лимит, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу.'
AUTH_ERROR = 'Текущий API-ключ ChatGPT не прошел аутентификацию, '\
              'мы заменили его на новый, пожалуйста повторите свой запрос кнопкой "Повторить" внизу. '\
              'Приносим извинения за неудобства.'


def get_answer(prompt, user):
    print('get_unswer started')
    current_openai_api_key = get_openai_api_key()
    print(f'Current openai key: {current_openai_api_key}')
    try:
        print('Completion start')
        client = OpenAI(api_key=current_openai_api_key)

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print('Completion finish')

    

        print('='*100)
        print(f'Вопрос пользователя: {user}', prompt)
        print('Ответ от ChatGPT:', completion.choices[0].message.content)
        print('='*100)
        answer = completion.choices[0].message.content
        return answer

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

    except Exception as e:
        print(f'Unrecognized Exception: {e}')
        return e