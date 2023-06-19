LEXICON_COMMANDS_RU = {
                '/start': 'Запуск бота (если перестал работать)',
                '/cancel': 'Выйти из диалого с ИИ',
                '/profile': 'Перейти в профиль пользователя',
                '/feedback': 'Написать админу',
                '/help': 'Справка'}

LEXICON_HELP = 'Данный бот отвечает на любые вопросы и генерирует любые изображения по текстовому описанию.\n\n'\
                'За тектовый диалог отвечает искусственный интелект на основе нейронной сети (ИИ) <b>ChatGPT</b>. '\
                'Данный ИИ работает в диалоговом режиме, и поддерживает запросы на естественных языках, '\
                'в том числе на русском. Он способен не просто отвечать на легкие вопросики в стиле Алисы, '\
                'но и пересказывать часовые фильмы в считанные секунды, создавать программный код по запросу, '\
                'сводить финансовые таблицы, писать сценарии, стихи и давать подробные гайды по любым '\
                'интересующим вас тематикам. Попробуйте задать ему вопрос, например "Напиши реферат на тему '\
                'Морские животные Арктики" или "Создай регулярку для всех телефонных номеров России". '\
                '<s><i>(note: Написать об ограничениях версии ChatGPT 3.0).</i></s>\n\n'\
                'Второй ИИ, представленный в данном боте, это <b>DALL-E2</b>. Это новый алгоритм нейронной сети, '\
                'который создает картинку из предоставленной вами короткой фразы или предложения. '\
                'Данный ИИ, так же как и ChatGPT понимает русский язык, но лучших результатов '\
                'можно добиться создавая запросы (промпты, анг. prompt) на английском языке. Попробуйте задать, например '\
                'такие промпты: <i>"An oil painting of a mechanical clockwork flying machine from the renaissance, '\
                'Gorgeous digital painting, amazing art, artstation 3, realistic"</i> '\
                'или <i>"a photo of cat flying out to space as an astronaut, digital art"</i>, но можно эксперементировать и на русском :) \n\n'\
                '<u>Так как получение доступа к этим ИИ временно ограничено в России, его приходится покупать, '\
                'поэтому после исчерпания количества бесплатных тестовых запросов, нужно оформлять подписку в разделе /profile</u>'

GPT_CHAT_TEXT = 'Пожалуйста, вводите запросы (prompt) к ChatGPT в режиме диалога. '\
                'Для выхода из диалога с ChatGPT и возврата в главное меню введите команду /cancel '\
                'или нажмите кнопку внизу'
DALLE_CHAT_TEXT = 'Пожалуйста, вводите запросы (prompt) к DALL-E2 в режиме диалога. '\
                'Для выхода из диалога с DALL-E2 введите команду /cancel '\
                'или нажмите кнопку внизу. Для получения альтернативного изображения нажмите '\
                'кнопку Повторить под изображением.'
START_MESSAGE = 'Вы запустили бот ChatGPT/DALL-E2. Выберите ИИ с которым будете вести диалог. '\
                'Подробнее о возможностях данного бота можно почитать в разделе "🆘 Помощь" '\
                'или вызвав команду /help'
FEEDBACK_TEXT = 'Введите ваше сообщение, оно будет отправлено админситратору. '\
                'В сообщении вы можете сообщить об ошибке, написать пожелание или '\
                'сообщить любую другую информацию. Для выхода из диалога используйте команду /cancel'
FEEDBACK_SENT = 'Ваше сообщение отправлено!'