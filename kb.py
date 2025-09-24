from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝Хочеш текстову хуйню?", callback_data="generate_text"),
InlineKeyboardButton(text="🖼Хочеш хуйову картинку?", callback_data="generate_image")]
    ]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Давай назад в меню нахооой")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Давай назад в меню нахооой", callback_data="menu")]])