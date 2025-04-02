import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from texts import *

import keyboards

bot = Bot("8153898215:AAGehKoaKtlE8XPC8ql2hpKBcVmtIPOY4ME")
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Здравствуй!👋  " , reply_markup=keyboards.main_kb)
    await message.answer("⬇ Выбери категорию лагерей (снизу) ⬇!  " , reply_markup=keyboards.main_kb)

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "ссылки✅":
        await  message.answer("Ссылки на наши каналы", reply_markup=keyboards.links_kb)

    elif msg == "it лагеря👀":
        await message.answer("вот IT лагеря!👌 ", reply_markup=keyboards.main_kb)

        caption_text = 'Название: IT-Jump\nРейтинг: 5,0 1807 оценок \nМесто нахождения: Крутушка \nСсылка: https://baytik-kazan.ru/festivali-i-konkursy/it-jump-konkurs-proektov-v-oblasti-cifrovih-tehnologiy/'
        await message.answer_photo(photo=aiti_lager_aitigamp, caption=caption_text)

        caption_text2 = 'Название: IT-каникулы\nРейтинг: 5,0  212 оценок \nМесто нахождения: Казань \nСсылка: https://kidsincamp.ru/camp/it-lager-kompyuternoy-akademii-shag-21-57?ysclid=m8a93nvkn9156613762'
        await message.answer_photo(photo=aiti_lager_aiticanicule, caption=caption_text2)



    elif msg == "спортивные  лагеря👀":
        await message.answer("вот спортивные  лагеря!👌 ", reply_markup=keyboards.main_kb)

        caption_text5 = 'Название: лагерь Сталкер\nРейтинг: 5.0  429 отзывов\nМесто нахождения: РФ, Татарстан, Казань, ДОЛ "Регина в Петровском"\nСсылка: https://incamp.ru/camp/lager-stalker-12547/'
        await message.answer_photo(photo=sport_lager_stalker, caption=caption_text5)

        caption_text6 = 'Название: Шторм\nРейтинг: 5,0 195 отзывов\nМесто нахождения: Республика Татарстан, Высокогорский р-н, пос. Кульсеитово, палаточный лагерь "Шторм"\nСсылка:https://kidsincamp.ru/camp/palatochnyy-lager-shtorm'
        await message.answer_photo(photo=sport_lager_shtorm, caption=caption_text6)


    elif msg == "языковые лагеря👀":
        await message.answer("вот языковые лагеря!👌 ", reply_markup=keyboards.main_kb)

        caption_text3 = 'Название: Эрудит\nРейтинг:  4,1  4 оценки  \nМесто нахождения: РФ, Татарстан, Чистополь, ЛОК "Раздолье" \nСсылка: https://incamp.ru/camp/dol-yerudit-na-baze-lok-razdol-6334/'
        await message.answer_photo(photo=yaz_lager_erudit, caption=caption_text3)

        caption_text4 = 'Название: Английский клуб\nРейтинг: 5,0  212 оценок \nМесто нахождения: Казань\nСсылка: https://kidsincamp.ru/camp/englishclub-sankt-peterburg'
        await message.answer_photo(photo=yaz_lager_anglclub, caption=caption_text4)

    elif msg == "кулинарные  лагеря👀":
        await message.answer("вот кулинарные  лагеря!👌 ", reply_markup=keyboards.main_kb)

        caption_text8 = 'Название: Кулинарные каникулы  \nРейтинг: 5,0  1807 оценок\nМесто нахождения: Крутушка \nСсылка: https://baytik-kazan.ru/kulinarnye-smeny/'
        await message.answer_photo(photo=culinar_lager_canicule, caption=caption_text8)

        caption_text9 = 'Название: Вкуснобайтик\nРейтинг: 5,0  1807 оценок\nМесто нахождения: Крутушка\nСсылка: https://baytik-kazan.ru/kulinarnye-smeny/osennie-kanikuly-so-vkusom/'
        await message.answer_photo(photo=culinar_lager_vcusnobaisic, caption=caption_text9)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


smiliki = "📌  👀"
