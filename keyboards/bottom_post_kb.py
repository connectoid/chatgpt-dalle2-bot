from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_bottom_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=button,
        callback_data=f'{button}') for button in buttons],
        width=1)
    return kb_builder.as_markup()

def create_count_keyboard(*buttons: str, width) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=button,
        callback_data=f'{button}') for button in buttons],
        width=width)
    return kb_builder.as_markup()

def create_tariffs_keyboard(buttons: list) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=f'Тариф {button.name}, {button.gpt_amount} запросов, {button.price} руб',
        callback_data=f'tariff {button.id}') for button in buttons],
        width=1)
    return kb_builder.as_markup()
