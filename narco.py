import telebot

bot = TeleBot = telebot.TeleBot('959127416:AAFEzB9PUIv1D9X3g3L5LuqFOGc2Dq5Y6xw')

#потдверждения
keyboard110 = telebot.types.ReplyKeyboardMarkup(True)
keyboard110.row('Оплатил', 'Отмена')
#оплата кнопки
keyboard100 = telebot.types.ReplyKeyboardMarkup(True)
keyboard100.row('QIWI')
keyboard100.row('BITCOIN')
#города клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('◆Москва')
keyboard1.row('◆Санк-Петербург')
keyboard1.row('◆Новосибирск')
keyboard1.row('◆Екатеренбург')
keyboard1.row('◆Челябинск')
keyboard1.row('◆Нижний Новгород')
keyboard1.row('◆Казань')
keyboard1.row('◆Омск')
keyboard1.row('◆Самара')
keyboard1.row('◆Краснодар')
keyboard1.row('◆Саратов')
keyboard1.row('◆Тюмень')
keyboard1.row('◆Барнаул')
keyboard1.row('◆Ярославь')
keyboard1.row('◆Владивосток')
keyboard1.row('◆Оренбург')
keyboard1.row('◆Томск')
keyboard1.row('◆Воронеж')
keyboard1.row('◆Волгоград')
keyboard1.row('◆Уфа')
keyboard1.row('◆Красноярск')
keyboard1.row('◆Тольятти')

#районы Москвы
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('◆Измайлова')
keyboard2.row('◆Сокольники')
keyboard2.row('◆Вкуново')
keyboard2.row('◆Кунцево')
keyboard2.row('◆Крюково')
keyboard2.row('◆Щукино')
keyboard2.row('◆Лефортово')
keyboard2.row('◆Выхино-Жулебина')
keyboard2.row('◆Медведково')
keyboard2.row('◆Якиманка')
keyboard2.row('◆Отрадное')
keyboard2.row('Главная')
#районы Санк-Петербург
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('♠Центральный район')
keyboard3.row('♠Невский район')
keyboard3.row('♠Кировский район')
keyboard3.row('♠Петроградский район')
keyboard3.row('♠Московский район')
keyboard3.row('♠Василеостровской район')
keyboard3.row('Главная')
#районы Новосибирск
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('♥Кировский')
keyboard4.row('♥Дзержинский')
keyboard4.row('♥Советский')
keyboard4.row('♥Центральный')
keyboard4.row('♥Железнодорожный')
keyboard4.row('♥Калининский')
keyboard4.row('♥Ленинский')
keyboard4.row('Главная')
#районы Екатеренбург
keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row('♣Верх-Исетский')
keyboard5.row('♣Железнодорожный')
keyboard5.row('♣Кировский')
keyboard5.row('♣Ленинский')
keyboard5.row('♣Октябрьский')
keyboard5.row('Главная')
#районы Челябинск
keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
keyboard6.row('♦АМЗ')
keyboard6.row('♦Центральный')
keyboard6.row('♦Ново-Синеглазово')
keyboard6.row('Главная')
#районы Нижний Новгород
keyboard7 = telebot.types.ReplyKeyboardMarkup(True)
keyboard7.row('♔Железнодорожный')
keyboard7.row('♔Калининский')
keyboard7.row('♔Ленинский')
keyboard7.row('Главная')
#районы Казань
keyboard8 = telebot.types.ReplyKeyboardMarkup(True)
keyboard8.row('♕Московский')
keyboard8.row('♕Кировский')
keyboard8.row('♕Вахитовский')
keyboard8.row('Главная')
#районы Омск
keyboard9 = telebot.types.ReplyKeyboardMarkup(True)
keyboard9.row('♖Октябрьский')
keyboard9.row('♖Советский')
keyboard9.row('♖Центральный')
keyboard9.row('Главная')
#районы Самара
keyboard10 = telebot.types.ReplyKeyboardMarkup(True)
keyboard10.row('♗Куйбышевский')
keyboard10.row('♗Ленинский')
keyboard10.row('♗Октябрьский')
keyboard10.row('Главная')
#районы Краснодар
keyboard11 = telebot.types.ReplyKeyboardMarkup(True)
keyboard11.row('♘Западный')
keyboard11.row('♘Карасунский')
keyboard11.row('♘Прикубанский')
keyboard11.row('♘Центральный')
keyboard11.row('Главная')
#районы Саратов
keyboard12 = telebot.types.ReplyKeyboardMarkup(True)
keyboard12.row('♙Заводской')
keyboard12.row('♙Волжский')
keyboard12.row('♙Октябрьский')
keyboard12.row('♙Фрунзенский')
keyboard12.row('♙Кировский')
keyboard12.row('♙Ленинский')
keyboard12.row('Главная')
#районы Тюмень
keyboard13 = telebot.types.ReplyKeyboardMarkup(True)
keyboard13.row('✖Восточный')
keyboard13.row('✖Калининский')
keyboard13.row('✖Ленинский')
keyboard13.row('✖Центральный')
keyboard13.row('Главная')
#районы Барнаул
keyboard14 = telebot.types.ReplyKeyboardMarkup(True)
keyboard14.row('⨻Ленинский')
keyboard14.row('⨻Индустриальный')
keyboard14.row('⨻Октябрьский')
keyboard14.row('⨻Центральный')
keyboard14.row('⨻Железнодорожный')
keyboard14.row('Главная')
#районы Ярославь
keyboard16 = telebot.types.ReplyKeyboardMarkup(True)
keyboard16.row('❖Дзержинский')
keyboard16.row('❖Заволжский')
keyboard16.row('❖Кировский')
keyboard16.row('❖Красноперековский')
keyboard16.row('❖Ленинский')
keyboard16.row('❖Фрунзенский')
keyboard16.row('Главная')
#районы Владивосток
keyboard17 = telebot.types.ReplyKeyboardMarkup(True)
keyboard17.row('✤Ленинский')
keyboard17.row('✤Первомайский')
keyboard17.row('✤Первореченский')
keyboard17.row('✤Советский')
keyboard17.row('✤Фрунзенский')
keyboard17.row('Главная')
#районы Оренбург
keyboard18 = telebot.types.ReplyKeyboardMarkup(True)
keyboard18.row('✻Дхержинский')
keyboard18.row('✻Ленинский')
keyboard18.row('✻Промышленный')
keyboard18.row('✻Центральный')
keyboard18.row('Главная')
#районы Томск
keyboard19 = telebot.types.ReplyKeyboardMarkup(True)
keyboard19.row('✔Кировский')
keyboard19.row('✔Ленинский')
keyboard19.row('✔Октябрьский')
keyboard19.row('✔Советский')
keyboard19.row('Главная')
#районы Воронеж
keyboard20 = telebot.types.ReplyKeyboardMarkup(True)
keyboard20.row('◎Железнодорожный')
keyboard20.row('◎Коминтерновский')
keyboard20.row('◎Левобережный')
keyboard20.row('◎Ленинский')
keyboard20.row('◎Советский')
keyboard20.row('◎Центральный')
keyboard20.row('Главная')
#районы Волгоград
keyboard21 = telebot.types.ReplyKeyboardMarkup(True)
keyboard21.row('ΔВорошиловский')
keyboard21.row('ΔДзержинский')
keyboard21.row('ΔКировский')
keyboard21.row('ΔКрасноармейский')
keyboard21.row('ΔКраснооктябрьский')
keyboard21.row('ΔСоветский')
keyboard21.row('ΔТракторозаводский')
keyboard21.row('ΔЦентральный')
keyboard21.row('Главная')
#районы Уфа
keyboard22 = telebot.types.ReplyKeyboardMarkup(True)
keyboard22.row('◕Кировский')
keyboard22.row('◕Советский')
keyboard22.row('◕Ленинский')
keyboard22.row('◕Демский')
keyboard22.row('◕Октябрьский')
keyboard22.row('◕Калининский')
keyboard22.row('Главная')
#районы Красноярск
keyboard23 = telebot.types.ReplyKeyboardMarkup(True)
keyboard23.row('✪Октябрьский')
keyboard23.row('✪Свердловский')
keyboard23.row('✪Советский')
keyboard23.row('✪Центральный')
keyboard23.row('✪Ленинский')
keyboard23.row('✪Кировский')
keyboard23.row('✪Железнодорожный')
keyboard23.row('Главная')
#районы Тольятти
keyboard24 = telebot.types.ReplyKeyboardMarkup(True)
keyboard24.row('◔Автозаводский')
keyboard24.row('◔Комсомольский')
keyboard24.row('◔Центральный')
keyboard24.row('Главная')


#товары для Москвы
keyboard30 = telebot.types.ReplyKeyboardMarkup(True)
keyboard30.row('СК(син.крис) {0.3г/900 RUB}')
keyboard30.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard30.row('СК(син.крис) {1г/2200 RUB}')
keyboard30.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard30.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard30.row('ГАШИШ EURO {5г/5000 RUB}')
keyboard30.row('MEPHEDRONE крис {1г/1000 RUB}')
keyboard30.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard30.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard30.row('ШИШКИ OG Kush  {5/4200 RUB}')
keyboard30.row('Кокаин VHQ{5/4800 RUB}')
#товары Санк-Петербург
keyboard31 = telebot.types.ReplyKeyboardMarkup(True)
keyboard31.row('СК(син.крис) {0.3г/700 RUB}')
keyboard31.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard31.row('СК(син.крис) {1г/2200 RUB}')
keyboard31.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard31.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard31.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard31.row('MEPHEDRONE крис {1г/1000 RUB}')
keyboard31.row('ШИШКИ OG Kush {1/1200 RUB}')
#товары Новосибирск
keyboard32 = telebot.types.ReplyKeyboardMarkup(True)
keyboard32.row('СК(син.крис) {0.3г/700 RUB}')#все
keyboard32.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard32.row('СК(син.крис) {1г/2200 RUB}') #vse
keyboard32.row('ГАШИШ EURO {1г/1100 RUB}')   # vse
keyboard32.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard32.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard32.row('ШИШКИ OG Kush {1/1200 RUB}')
#товары Екатеринбург
keyboard33 = telebot.types.ReplyKeyboardMarkup(True)
keyboard33.row('СК(син.крис) {0.3г/900 RUB}')
keyboard33.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard33.row('СК(син.крис) {1г/2200 RUB}')
keyboard33.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard33.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard33.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard33.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard33.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard33.row('ШИШКИ OG Kush {5/4200 RUB}')
keyboard30.row('Амфетамин (импорт){2/1750 RUB}')
#товары Челябинск
keyboard34 = telebot.types.ReplyKeyboardMarkup(True)
keyboard34.row('СК(син.крис) {0.3г/900 RUB}')
keyboard34.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard34.row('СК(син.крис) {1г/2200 RUB}')
keyboard34.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard34.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard34.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard34.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard34.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard34.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Нижний Новгород
keyboard35 = telebot.types.ReplyKeyboardMarkup(True)
keyboard35.row('СК(син.крис) {0.3г/800 RUB}')
keyboard35.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard35.row('СК(син.крис) {1г/2000 RUB}')
keyboard35.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard35.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard35.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard35.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard35.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard35.row('ШИШКИ OG Kush {5/4200 RUB}')
keyboard30.row('Кокаин VHQ{5/4800 RUB}')
#товары Казань
keyboard36 = telebot.types.ReplyKeyboardMarkup(True)
keyboard36.row('СК(син.крис) {0.3г/800 RUB}')
keyboard36.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard36.row('СК(син.крис) {1г/2000 RUB}')
keyboard36.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard36.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard36.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard36.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard36.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard36.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Омск
keyboard37 = telebot.types.ReplyKeyboardMarkup(True)
keyboard37.row('СК(син.крис) {0.3г/900 RUB}')
keyboard37.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard37.row('СК(син.крис) {1г/2100 RUB}')
keyboard37.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard37.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard37.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard37.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard37.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard37.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Самара
keyboard38 = telebot.types.ReplyKeyboardMarkup(True)
keyboard38.row('СК(син.крис) {0.3г/850 RUB}')
keyboard38.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard38.row('СК(син.крис) {1г/2150 RUB}')
keyboard38.row('ГАШИШ EURO {1г/1050 RUB}')
keyboard38.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard38.row('ГАШИШ EURO {5г/3900 RUB}')
keyboard38.row('ШИШКИ OG Kush {1/1100 RUB}')
keyboard38.row('ШИШКИ OG Kush {2/2100 RUB}')
keyboard38.row('ШИШКИ OG Kush {5/4150 RUB}')
#товары Краснодар
keyboard39 = telebot.types.ReplyKeyboardMarkup(True)
keyboard39.row('СК(син.крис) {0.3г/850 RUB}')
keyboard39.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard39.row('СК(син.крис) {1г/2000 RUB}')
keyboard39.row('ГАШИШ EURO {1г/1150 RUB}')
keyboard39.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard39.row('ГАШИШ EURO {5г/3900 RUB}')
keyboard39.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard39.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard39.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Саратов
keyboard40 = telebot.types.ReplyKeyboardMarkup(True)
keyboard40.row('СК(син.крис) {0.3г/900 RUB}')
keyboard40.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard40.row('СК(син.крис) {1г/2100 RUB}')
keyboard40.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard40.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard40.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard40.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard40.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard40.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Тюмень
keyboard41 = telebot.types.ReplyKeyboardMarkup(True)
keyboard41.row('СК(син.крис) {0.3г/950 RUB}')
keyboard41.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard41.row('СК(син.крис) {1г/2100 RUB}')
keyboard41.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard41.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard41.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard41.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard41.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard41.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Барнаул
keyboard42 = telebot.types.ReplyKeyboardMarkup(True)
keyboard42.row('СК(син.крис) {0.3г/950 RUB}')
keyboard42.row('СК(син.крис) {0.5г/1400 RUB}')
keyboard42.row('СК(син.крис) {1г/2100 RUB}')
keyboard42.row('ГАШИШ EURO {1г/1200 RUB}')
keyboard42.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard42.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard42.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard42.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard42.row('ШИШКИ OG Kush {5/3900 RUB}')
#товары Ярославь
keyboard43 = telebot.types.ReplyKeyboardMarkup(True)
keyboard43.row('СК(син.крис) {0.3г/950 RUB}')
keyboard43.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard43.row('СК(син.крис) {1г/2100 RUB}')
keyboard43.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard43.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard43.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard43.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard43.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard43.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Владивосток
keyboard44 = telebot.types.ReplyKeyboardMarkup(True)
keyboard44.row('СК(син.крис) {0.3г/850 RUB}')
keyboard44.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard44.row('СК(син.крис) {1г/2100 RUB}')
keyboard44.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard44.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard44.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard44.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard44.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard44.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Оренбург
keyboard45 = telebot.types.ReplyKeyboardMarkup(True)
keyboard45.row('СК(син.крис) {0.3г/900 RUB}')
keyboard45.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard45.row('СК(син.крис) {1г/2100 RUB}')
keyboard45.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard45.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard45.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard45.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard45.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard45.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Томск
keyboard46 = telebot.types.ReplyKeyboardMarkup(True)
keyboard46.row('СК(син.крис) {0.3г/900 RUB}')
keyboard46.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard46.row('СК(син.крис) {1г/2100 RUB}')
keyboard46.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard46.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard46.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard46.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard46.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard46.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Воронеж
keyboard47 = telebot.types.ReplyKeyboardMarkup(True)
keyboard47.row('СК(син.крис) {0.3г/900 RUB}')
keyboard47.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard47.row('СК(син.крис) {1г/2100 RUB}')
keyboard47.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard47.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard47.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard47.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard47.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard47.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Волгоград
keyboard48 = telebot.types.ReplyKeyboardMarkup(True)
keyboard48.row('СК(син.крис) {0.3г/900 RUB}')
keyboard48.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard48.row('СК(син.крис) {1г/2100 RUB}')
keyboard48.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard48.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard48.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard48.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard48.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard48.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Уфа
keyboard49 = telebot.types.ReplyKeyboardMarkup(True)
keyboard49.row('СК(син.крис) {0.3г/900 RUB}')
keyboard49.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard49.row('СК(син.крис) {1г/2100 RUB}')
keyboard49.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard49.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard49.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard49.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard49.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard49.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Красноярск
keyboard50 = telebot.types.ReplyKeyboardMarkup(True)
keyboard50.row('СК(син.крис) {0.3г/900 RUB}')
keyboard50.row('СК(син.крис) {0.5г/1300 RUB}')
keyboard50.row('СК(син.крис) {1г/2100 RUB}')
keyboard50.row('ГАШИШ EURO {1г/1100 RUB}')
keyboard50.row('ГАШИШ EURO {2г/2000 RUB}')
keyboard50.row('ГАШИШ EURO {5г/4000 RUB}')
keyboard50.row('ШИШКИ OG Kush {1/1200 RUB}')
keyboard50.row('ШИШКИ OG Kush {2/2200 RUB}')
keyboard50.row('ШИШКИ OG Kush {5/4200 RUB}')
#товары Тольятти
keyboard51 = telebot.types.ReplyKeyboardMarkup(True)
keyboard51.row('СК(син.крис) {0.3г/800 RUB}')
keyboard51.row('СК(син.крис) {0.5г/1200 RUB}')
keyboard51.row('СК(син.крис) {1г/2000 RUB}')
keyboard51.row('ГАШИШ EURO {1г/1000 RUB}')
keyboard51.row('ГАШИШ EURO {2г/1900 RUB}')
keyboard51.row('ГАШИШ EURO {5г/3900 RUB}')
keyboard51.row('ШИШКИ OG Kush {1/1100 RUB}')
keyboard51.row('ШИШКИ OG Kush {2/2000 RUB}')
keyboard51.row('ШИШКИ OG Kush {5/4000 RUB}')

#текст и кнопки после /start
@bot.message_handler(commands=['start'],)
def start_message(message):
    bot.send_message(message.chat.id,  "Как сделать заказ? :\n"
"\n"                                     
"*1 - Выберите свой город\n*"
"\n"                                  
"*2 - Выберите что вас интересует\n*"
"\n"                                     
"*3 - Оплатите выбрыный товар(Строго с прикреплёным комментарием)\n*"
"\n"                                    
"*4 - Бот в течении часа вышлет : фото клада в близи/фото клада отдалёно/точные координаты\n*"
"\n"
"\n"
"\n"
" Хорошего отдыха!!!\n"
"\n"
"\n"
"\n"
"❗️❗️ Внимание работа ❗️❗️\n"
"\n"                                     
"🔵Ищем ответственных людей\n"
"\n"                                     
" 🛑ВАШИ ТАЛАНТЫ НЕ ОСТАНУТСЯ НЕЗАМЕЧЕННЫМИ!\n"
"\n"                                     
"▪️Курьер (от 50.000 руб/неделя)\n"
"\n"                                     
" Окупаемость залога один день!!\n"
"\n"                                     
"▪️Водитель - до 1.000.000 руб/месяц.\n"
"\n"                                      
"▪️Фасовщик на дому - от 50.000 рублей/неделя\n"
"\n"                                      
"▪️Менеджер по подбору персонала - от 500 рублей/1 человек + премии!\n"
"\n"                                      
"📢Обращаться - @aksakall10", parse_mode = 'Markdown', reply_markup=keyboard1)
#районы под городами
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '◆Москва':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard2)
    elif message.text == '◆Санк-Петербург':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard3)
    elif message.text == '◆Новосибирск':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard4)
    elif message.text == '◆Екатеренбург':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard5)
    elif message.text == '◆Челябинск':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard6)
    elif message.text == '◆Нижний Новгород':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard7)
    elif message.text == '◆Казань':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard8)
    elif message.text == '◆Омск':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard9)
    elif message.text == '◆Самара':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard10)
    elif message.text == '◆Краснодар':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard11)
    elif message.text == '◆Саратов':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard12)
    elif message.text == '◆Тюмень':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard13)
    elif message.text == '◆Барнаул':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard14)
    elif message.text == '◆Ярославь':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard16)
    elif message.text == '◆Владивосток':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard17)
    elif message.text == '◆Оренбург':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard18)
    elif message.text == '◆Томск':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard19)
    elif message.text == '◆Воронеж':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard20)
    elif message.text == '◆Волгоград':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard21)
    elif message.text == '◆Уфа':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard22)
    elif message.text == '◆Красноярск':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard23)
    elif message.text == '◆Тольятти':
        bot.send_message(message.chat.id, '⬇️ Выберите район ⬇️', reply_markup=keyboard24)
    elif message.text == '◆Измайлова': #товары под категориями районов для москва
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Сокольники':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Вкуново':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Кунцево':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Крюково':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Щукино':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Лефортово':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Выхино-Жулебина':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Медведково':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Якиманка':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '◆Отрадное':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard30)
    elif message.text == '♠Центральный район': #товары под категориями районов для санк-петербург
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♠Невский район':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♠Кировский район':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♠Петроградский район':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♠Московский район':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♠Василеостровской район':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard31)
    elif message.text == '♥Кировский': #товары под категориями районов для Новосибирск
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♥Дзержинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♥Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♠♥Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♥Железнодорожный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♥Калининский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♥Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard32)
    elif message.text == '♣Верх-Исетский':  # товары под категориями районов для Екатеренбург
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard33)
    elif message.text == '♣Железнодорожный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard33)
    elif message.text == '♣Кировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard33)
    elif message.text == '♣Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard33)
    elif message.text == '♣Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard33)
    elif message.text == '♦АМЗ': # товары под категориями районов для Челябинск
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard34)
    elif message.text == '♦Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard34)
    elif message.text == 'Ново-Синеглазово':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard34)
    elif message.text == '♔Железнодорожный':  # товары под категориями районов для Нижний новгород
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard35)
    elif message.text == '♔Калининский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard35)
    elif message.text == '♔Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard35)
    elif message.text == '♕Московский':  # товары под категориями районов для Казань
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard36)
    elif message.text == '♕Кировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard36)
    elif message.text == '♕Вахитовский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard36)
    elif message.text == '♖Октябрьский':  # товары под категориями районов для Омска
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard37)
    elif message.text == '♖Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard37)
    elif message.text == '♖Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard37)
    elif message.text == '♗Куйбышевский':  # товары под категориями районов для Самара
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard38)
    elif message.text == '♗Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard38)
    elif message.text == '♗Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard38)
    elif message.text == '♘Западный':   # товары под категориями районов для Краснодар
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard39)
    elif message.text == '♘Карасунский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard39)
    elif message.text == '♘Прикубанский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard39)
    elif message.text == '♘Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard39)
    elif message.text == '♙Заводской':   # товары под категориями районов для Саратов
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '♙Волжский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '♙Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '♙Фрунзенский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '♙Кировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '♙Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard40)
    elif message.text == '✖Восточный': # товары под категориями районов для Тюмень
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard41)
    elif message.text == '✖Калининский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard41)
    elif message.text == '✖Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard41)
    elif message.text == '✖Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard41)
    elif message.text == '⨻Ленинский':   # товары под категориями районов для Барнаул
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard42)
    elif message.text == '⨻Индустриальный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard42)
    elif message.text == '⨻Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard42)
    elif message.text == '⨻Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard42)
    elif message.text == '⨻Железнодорожный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard42)
    elif message.text == '❖Дзержинский':     # товары под категориями районов для Ярославь
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '❖Заволжский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '❖Кировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '❖Красноперековский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '❖Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '❖Фрунзенский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard43)
    elif message.text == '✤Ленинский': # товары под категориями районов для Владивосток
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard44)
    elif message.text == '✤Первомайский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard44)
    elif message.text == '✤Первореченский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard44)
    elif message.text == '✤Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard44)
    elif message.text == '✤Фрунзенский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard44)
    elif message.text == '✻Дхержинский':       # товары под категориями районов для Оренбуог
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard45)
    elif message.text == '✻Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard45)
    elif message.text == '✻Промышленный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard45)
    elif message.text == '✻Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard45)
    elif message.text == '✔Кировский':         # товары под категориями районов для Томск
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard46)
    elif message.text == '✔Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard46)
    elif message.text == '✔Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard46)
    elif message.text == '✔Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard46)
    elif message.text == '◎Железнодорожный':# товары под категориями районов для Воронеж
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '◎Коминтерновский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '◎Левобережный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '◎Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '◎Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '◎Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == '':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard47)
    elif message.text == 'ΔЦентральный':    #товары под категориями районов для Волгоград
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔТракторозаводский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔСоветский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔКраснооктябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔКрасноармейский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔКировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔДзержинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == 'ΔВорошиловский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard48)
    elif message.text == '◕Кировский':#товары под категориями районов для Уфа
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '◕Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '◕Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '◕Демский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '◕Октябрьский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '◕Калининский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard49)
    elif message.text == '✪Октябрьский':       # товары под категориями районов для Красноярск
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Свердловский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Советский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Ленинский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Кировский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '✪Железнодорожный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard50)
    elif message.text == '◔Автозаводский':          #товары под категориями районов для Тольятии
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard51)
    elif message.text == '◔Комсомольский':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard51)
    elif message.text == '◔Центральный':
        bot.send_message(message.chat.id, 'Выбери товар и кол-во', reply_markup=keyboard51)
    elif message.text == 'СК(син.крис) {0.3г/950 RUB}':   #появление кнопки qivi bitcoin карта
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.3г/900 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.3г/700 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.3г/800 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.3г/850 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.5г/1200 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.5г/1300 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {0.5г/1400 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {1г/2200 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'СК(син.крис) {1г/2000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {1г/1000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {1г/1100 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {1г/1050 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {1г/1150 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {2г/2000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {2г/1900 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {5г/3900 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {5г/4000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ГАШИШ EURO {5г/5000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {1/1200 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {1/1100 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {2/2000 RUB}ШИШКИ':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {2/2100 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {2/2200 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {5/4000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {5/4200 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {5/3900 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'ШИШКИ OG Kush {5/4150 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'MEPHEDRONE крис {1г/1000 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'Кокаин VHQ{5/4800 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text == 'Амфетамин (импорт){2/1750 RUB}':
        bot.send_message(message.chat.id, 'Выберите способ оплаты', reply_markup=keyboard100)
    elif message.text =='QIWI':
        bot.send_message(message.chat.id,
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"Вы зарезервировали товар на 30⌛️ минут.\n"
"Чтобы получить координаты/фото товара - Совершите платёж на QIWI.\n"
"\n"
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"🏷QIWI кошелек: +79870541741\n"
"\n"
"💬Комментарий к платежу:1946294\n"
"\n"
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"Сумма платежа должна быть равна сумме товара."
"\n"
"БЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ", reply_markup=keyboard110)
    elif message.text == 'BITCOIN':
        bot.send_message(message.chat.id,
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"Вы зарезервировали товар на 30⌛️ минут.\n"
"Чтобы получить координаты/фото товара - Совершите платёж на Bitcoin кошелек.\n"
"\n"
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"🏷Bitcoin кошелек:1LDyGwHxv1Z4At975r2WvxbvnVxHnN2F84\n"
"\n"
"➖➖➖➖➖➖➖➖➖➖\n"
"\n"
"Сумма платежа должна быть равна сумме товара."
"\n"
"БЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ", reply_markup=keyboard110)
    elif message.text == 'Оплатил':
        bot.send_message(message.chat.id, "Платеж не найден, попробуйте через 5 минут")
    elif message.text == 'Отмена':
        bot.send_message(message.chat.id, "Как сделать заказ? :\n"
"\n"                                     
"*1 - Выберите свой город\n*"
"\n"                                  
"*2 - Выберите что вас интересует\n*"
"\n"                                     
"*3 - Оплатите выбрыный товар(Строго с прикреплёным комментарием)\n*"
"\n"                                    
"*4 - Бот в течении часа вышлет : фото клада в близи/фото клада отдалёно/точные координаты\n*"
"\n"
"\n"
"\n"
" Хорошего отдыха!!!\n"
"\n"
"\n"
"\n"
"❗️❗️ Внимание работа ❗️❗️\n"
"\n"                                     
"🔵Ищем ответственных людей\n"
"\n"                                     
" 🛑ВАШИ ТАЛАНТЫ НЕ ОСТАНУТСЯ НЕЗАМЕЧЕННЫМИ!\n"
"\n"                                     
"▪️Курьер (от 50.000 руб/неделя)\n"
"\n"                                     
" Окупаемость залога один день!!\n"
"\n"                                     
"▪️Водитель - до 1.000.000 руб/месяц.\n"
"\n"                                      
"▪️Фасовщик на дому - от 50.000 рублей/неделя\n"
"\n"                                      
"▪️Менеджер по подбору персонала - от 500 рублей/1 человек + премии!\n"
"\n"                                      
"📢Обращаться - @aksakall10", parse_mode = 'Markdown', reply_markup=keyboard1)
    elif message.text =='Главная':
        bot.send_message(message.chat.id, "Как сделать заказ? :\n"
"\n"                                     
"*1 - Выберите свой город\n*"
"\n"                                  
"*2 - Выберите что вас интересует\n*"
"\n"                                     
"*3 - Оплатите выбрыный товар(Строго с прикреплёным комментарием)\n*"
"\n"                                    
"*4 - Бот в течении часа вышлет : фото клада в близи/фото клада отдалёно/точные координаты\n*"
"\n"
"\n"
"\n"
" Хорошего отдыха!!!\n"
"\n"
"\n"
"\n"
"❗️❗️ Внимание работа ❗️❗️\n"
"\n"                                     
"🔵Ищем ответственных людей\n"
"\n"                                     
" 🛑ВАШИ ТАЛАНТЫ НЕ ОСТАНУТСЯ НЕЗАМЕЧЕННЫМИ!\n"
"\n"                                     
"▪️Курьер (от 50.000 руб/неделя)\n"
"\n"                                     
" Окупаемость залога один день!!\n"
"\n"                                     
"▪️Водитель - до 1.000.000 руб/месяц.\n"
"\n"                                      
"▪️Фасовщик на дому - от 50.000 рублей/неделя\n"
"\n"                                      
"▪️Менеджер по подбору персонала - от 500 рублей/1 человек + премии!\n"
"\n"                                      
"📢Обращаться - @aksakall10", parse_mode = 'Markdown', reply_markup=keyboard1)

bot.polling()
