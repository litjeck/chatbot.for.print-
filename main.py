import asyncio
import os
import logging  #For receive important messages about status of programm
from config import TOKEN  # import our token from config.py
from aiogram import Bot, Dispatcher, Router, types, F  #
from aiogram.filters.command import Command  #
from aiogram.types import Message
from PyQt5 import Qt

logging.basicConfig(level=logging.INFO)
router = Router()
# Our Values(Переменные)
flag_printer = False #values about "Have we got connection with printer?"

@router.message(Command("start")) # Starting command
async def com_start(message: types.Message):
    await message.answer(
        "Приветствую тебя! Я, бот который может дистанционно печатать.\nВведи /list для получения полного списка комманд")

@router.message(Command("list")) #Command as /help. Print all commands and their functions
async def com_list(message: types.Message):
    await message.answer(
        "/info - дополнительная информация\n/photo - печать фото\n/docs- печать документов. Файлы должны быть .pdf или .txt")

@router.message(Command("photo")) #
async def com_photo(message: types.Message):
    await message.reply("Пришли Фотографию размером до 25Мб")
    @router.message(F.photo)
    async def com_photo(message: types.Message, bot: Bot):
        await bot.download(
            message.photo[-1],
            destination=f"{message.photo[-1].file_id}.jpg")
        '''
        if __name__ == "__main__":
            app = Qt.QApplication([])
            printer = Qt.QPrinter()
            te = Qt.QTextEdit()
            te.setHtml(f"{message.photo[-1].file_id}.jpg")
            te.show()
            print_dialog = Qt.QPrintDialog(printer)
            if print_dialog.exec() == Qt.QDialog.Accepted:
                te.print(printer)
            app.exec()
        '''
        os.startfile(f"{message.photo[-1].file_id}.jpg", "print")

@router.message(Command("docs"))
async def com_docs(message: types.Message):
    await message.reply("Пришли документ ")

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
