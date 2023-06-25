BUTTON = {'ru':{'MAIN_MENU_BUTTON':'🏠 Главное меню',
                'HELP_BUTTON': '🆘 Помощь',
                'TO_MAIN_MENU_BUTTON': '⬅️ В главное меню',
                'REPEAT_BUTTON': '🔁 Повторить',
                'PROFILE_BUTTON': 'ℹ️ Профиль',
                'REMAINS_BUTTON': '🔢 Остаток заросов',
                'TARIFF_BUTTON': '💰 Выбрать тариф',
                'HISTORY_BUTTON': '🕑 История запросов',
                'RUS_LANG_BUTTON': 'Русский (ru)',
                'ENG_LANG_BUTTON': 'Английский (en)',
            },

            'en':{'MAIN_MENU_BUTTON':'🏠 Main menu',
                'HELP_BUTTON': '🆘 Help',
                'TO_MAIN_MENU_BUTTON': '⬅️ To main menu',
                'REPEAT_BUTTON': '🔁 Repeat',
                'PROFILE_BUTTON': 'ℹ️ Profile',
                'REMAINS_BUTTON': '🔢 Rest of requests',
                'TARIFF_BUTTON': '💰 Choose a tariff',
                'HISTORY_BUTTON': '🕑 Requests history',
                'RUS_LANG_BUTTON': 'Русский (ru)',
                'ENG_LANG_BUTTON': 'English (en)',

            }
}

MESSAGE = {'ru': {
                'LEXICON_HELP': 'Данный бот отвечает на любые вопросы и генерирует любые изображения по текстовому описанию.\n\n'\
                'За тектовый диалог отвечает искусственный интелект на основе нейронной сети (ИИ) <b>ChatGPT</b>. '\
                'Данный ИИ работает в диалоговом режиме, и поддерживает запросы на естественных языках, '\
                'в том числе на русском. Он способен не просто отвечать на легкие вопросики в стиле Алисы, '\
                'но и пересказывать часовые фильмы в считанные секунды, создавать программный код по запросу, '\
                'сводить финансовые таблицы, писать сценарии, стихи и давать подробные гайды по любым '\
                'интересующим вас тематикам. Попробуйте задать ему вопрос, например "Напиши реферат на тему '\
                'Морские животные Арктики" или "Создай регулярку для всех телефонных номеров России". '\
                '\n\n'\
                'Второй ИИ, представленный в данном боте, это <b>DALL-E2</b>. Это новый алгоритм нейронной сети, '\
                'который создает картинку из предоставленной вами короткой фразы или предложения. '\
                'Данный ИИ, так же как и ChatGPT понимает русский язык, но лучших результатов '\
                'можно добиться создавая запросы (промпты, анг. prompt) на английском языке. Попробуйте задать, например '\
                'такие промпты: <i>"An oil painting of a mechanical clockwork flying machine from the renaissance, '\
                'Gorgeous digital painting, amazing art, artstation 3, realistic"</i> '\
                'или <i>"a photo of cat flying out to space as an astronaut, digital art"</i>, но можно эксперементировать и на русском :) \n\n'\
                '<u>Бот работает в демоснтрационном режиме, вы можете бесплатно выбрать любой тариф в разделе /profile</u>',
                
                'GPT_CHAT_TEXT': 'Пожалуйста, вводите запросы (prompt) к ChatGPT в режиме диалога. '\
                'Для выхода из диалога с ChatGPT и возврата в главное меню введите команду /cancel '\
                'или нажмите кнопку внизу',

                'DALLE_CHAT_TEXT': 'Пожалуйста, вводите запросы (prompt) к ChatGPT в режиме диалога. '\
                'Для выхода из диалога с ChatGPT',

                'START_MESSAGE': 'Вы запустили бот ChatGPT/DALL-E2. Выберите в нижнем меню ИИ с которым '\
                'будете вести диалог (ChatGPT или DALL-E2). '\
                'Подробнее о возможностях данного бота можно почитать в разделе "🆘 Помощь" '\
                'или вызвав команду /help',

                'FEEDBACK_TEXT': 'Введите ваше сообщение, оно будет отправлено админситратору. '\
                'В сообщении вы можете сообщить об ошибке, написать пожелание или '\
                'сообщить любую другую информацию. Для выхода из диалога используйте команду /cancel',

                'FEEDBACK_SENT': 'Ваше сообщение отправлено!',

                'UNRECOGNIZED_COMMAND': 'Неизвестная команда или вы задаете вопрос не находясь в диалоге с ИИ. '\
                'Пожалуйста, выберите ChatGPT или DALL-E2  внижнем меню. Если данных пунктов нет в меню, '\
                'выполните команду /start',
                'LANG': 'Выберите ваш язык. Choose your language',
                'LANG_CHOSEN': 'Язык выбран (Применение перевода текста командного меню займет какое-то '\
                'время, чтобы ускорить вы можете перезагрузить приложение: ',
                'EXIT_DIALOGUE': 'Вы вышли из диалога',
                'NOT_IN_DIALOGUE': 'В данный момент вы не ведёте диалог. Выберите в главном меню ИИ для диалога',
                'CHOOSE_TARIFF': 'Выберите тариф (бесплатно в тестовом режиме):',
                'NOT_IN_DIALOGUE': 'В данный момент вы не ведёте диалог. Выберите в главном меню ChatGPT или DALL-E2 для диалога',
                'DENIED_IN_DIALOGUE': 'Эта команда недоступна в режиме диалога с ИИ. Для вызова данной команды '\
                'нужно выйти из диалога командой /cancel или вы можете продолжить диалог.',
                'LIMIT_RICHED': 'У вас не осталось оплаченных запросов, выйдите из диалога командой /cancel и '\
                'выберите любой тариф в разделе Профиль /profile (это бесплатно)',
                'CHOOSE_SECTION': 'Выберите раздел',
                'UNDER_DEVELOPMENT': '👷‍♂️ Данный раздел пока в разработке',
                'TARIFF_SELECTED': 'Выбран тариф',
                'PROMPTS_REMAINS': 'У вас осталось запросов:',
                'YOUR_TARIFF': 'Ваш тариф: ',
                
            },


            'en': {
                'LEXICON_HELP': 'This bot can answer any question and generate any image based '\
                'on text description. The <b>ChatGPT</b> artificial intelligence neural network '\
                'is responsible for text dialogue. This AI works in dialogue mode and supports '\
                'natural language requests, including in Russian. It is capable of not only '\
                'answering easy questions in the style of Alice, but also summarizing hours-long '\
                'films in just a few seconds, creating program code on request, compiling financial '\
                'tables, writing scripts, poems, and providing detailed guides on any topics of '\
                'interest to you. Try asking him a question, such as "Write me an essay on the topic '\
                'of Arctic marine life" or "Create a regular expression for all phone numbers in '\
                'Russia".\n\n'\
                'The second AI presented in this bot is <b>DALL-E2</b>. This is a new neural network '\
                'algorithm that creates an image from a short phrase or sentence provided by you. '\
                'This AI, like ChatGPT, understands Russian, but better results can be achieved by '\
                'creating prompts in English. Try, for example, such prompts: <i>"An oil painting '\
                'of a mechanical clockwork flying machine from the renaissance, Gorgeous digital '\
                'painting, amazing art, artstation 3, realistic"</i> or <i>"a photo of cat flying '\
                'out to space as an astronaut, digital art"</i>, but you can also experiment with '\
                'Russian ones 🙂 \n\nBot is running in demo mode. You can choose any tariff for free '\
                'in the /profile section.',
                
                'GPT_CHAT_TEXT': 'Please enter your queries to ChatGPT in dialogue mode. '\
                'To exit the ChatGPT dialogue and return to the main menu, type the command /cancel '\
                'or press the button at the bottom.',

                'DALLE_CHAT_TEXT': 'Please enter your requests (prompt) for ChatGPT in dialogue mode. '\
                'To exit the ChatGPT dialogue and return to the main menu, enter the /cancel command '\
                'or click the button below.',

                'START_MESSAGE': 'You have launched the ChatGPT/DALL-E2 bot. Choose an AI to dialogue '\
                'with in the bottom menu (ChatGPT or DALL-E2). Read more about the possibilities of this bot '\
                'in the "🆘 Help" section or by calling the /help command.',

                'FEEDBACK_TEXT': 'Enter your message, it will be sent to the administrator. '\
                'In the message, you can report an error, write a suggestion, or provide any other '\
                'information. Use the /cancel command to exit the dialog.',

                'FEEDBACK_SENT': 'Your message has been sent!',

                'UNRECOGNIZED_COMMAND': 'Unknown command or you are asking a question outside of the '\
                'AI dialog. Please select ChatGPT or DALL-E2 in the bottom menu. If these options are '\
                'not visible in the menu, please execute the command /start',
                'LANG': 'Выберите ваш язык. Choose your language',
                'LANG_CHOSEN': 'Language has been chosen (Applying the command-menu translation may '\
                'take some time, to speed it up you can restart the application): ',
                'EXIT_DIALOGUE': 'You are exit from dialogue',
                'NOT_IN_DIALOGUE': 'You are not in dealogue now. Choose in Main menu AI to dialogue',
                'CHOOSE_TARIFF': 'Choose your tariff (free in demo-mode):',
                'NOT_IN_DIALOGUE': 'Currently you are not in conversation. Select ChatGPT or DALL-E2 from '\
                'the main menu to start a conversation.',
                'DENIED_IN_DIALOGUE': 'This command is not available in AI dialog mode. '\
                'To use this command,  you need to exit the dialog by using the /cancel '\
                'command or you can continue the dialog.',
                'LIMIT_RICHED': 'You have no paid requests left, please exit the dialog by command /cancel '\
                'and select any tariff in the Profile section /profile (it is for free).',
                'CHOOSE_SECTION': 'Please select a section.',
                'UNDER_DEVELOPMENT': '👷‍♂️ This section is still under development.',
                'TARIFF_SELECTED': 'Tariff selected',
                'PROMPTS_REMAINS': 'You have requests left:',
                'YOUR_TARIFF': 'Your tariff: ',
            },
}

COMMAND = {'ru':{
                '/start': 'Запуск бота (если перестал работать)',
                '/cancel': 'Выйти из диалого с ИИ',
                '/profile': 'Перейти в профиль пользователя',
                '/feedback': 'Написать админу',
                '/lang': 'Переключить язык',
                '/help': 'Справка',
                },
            'en':{
                '/start': 'Starts bot (or if it stopping working)',
                '/cancel': 'Exit the dialogue with AI',
                '/profile': 'Go to user profile',
                '/feedback': 'Message to admin',
                '/lang': 'change language',
                '/help': 'Help',
            }

}

TARIFF = {'ru':{
                'tariff-1': 'Тариф "Лайт" (25 запросов)',
                'tariff-2': 'Тариф "Оптима" (50 запросов)', 
                'tariff-3': 'Тариф "Макс" (100 запросов)',
            },
        'en':{
                'tariff-1': 'Tariff "Light" (25 prompts)',
                'tariff-2': 'Tariff "Optima" (50 prompts)', 
                'tariff-3': 'Tariff "Max" (100 prompts)',
            }

}

BROADCAST = {'ru':{
                'whats_new': 'Бот был обновлен до новой версии. В новой версии: \n'\
                '- Добавлена возможность отправки сообщения администратору (команда /feedback). \n'\
                '- Добавлена возможность переключения языков интерфейса между Русским и Английским '\
                '(команда /lang). \n'\
                '- Бот обновлен до модели ChatGPT 3.5 Turbo. \n'\
                '- Исправлены некоторые ошибки при попытке выполнить команду находясь в состоянии диалога с ИИ.',
                'spam-1': 'Тариф "Оптима" (50 запросов)', 
                'spam-2': 'Тариф "Макс" (100 запросов)',
            },
        'en':{
                'whats_new': 'Bot was updated to new version. In new version: \n'\
                '- Added the ability to send a message to the administrator. (command /feedback). \n'\
                '- Added the ability to switch interface languages between Russian and English '\
                '(команда /lang). \n'\
                '- Bot was updated to model ChatGPT 3.5 Turbo. \n'\
                '- Fixed some errors when trying to execute a command while in a dialog state',
                'spam-1': 'Тариф "Оптима" (50 запросов)', 
                'spam-2': 'Тариф "Макс" (100 запросов)',
            }
}