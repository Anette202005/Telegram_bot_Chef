# 5684149153:AAFw-btPG2Ag8GXAHWLEbnlWG1K9Kns_pvk

import telebot
from telebot import types

token ='5684149153:AAFw-btPG2Ag8GXAHWLEbnlWG1K9Kns_pvk'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    one_btn = types.InlineKeyboardButton(text="ЧИЗКЕЙК", callback_data='1')
    two_btn = types.InlineKeyboardButton(text="СЫРНИКИ", callback_data='2')
    three_btn = types.InlineKeyboardButton(text="ШОКОЛАДНЫЕ ЭКЛЕРЫ", callback_data='3')
    four_btn = types.InlineKeyboardButton(text="ШАРЛОТКА", callback_data='4')
    five_btn = types.InlineKeyboardButton(text="ПАНКЕЙКИ", callback_data='5')
    keyboard.add(one_btn)
    keyboard.add(two_btn)
    keyboard.add(three_btn)
    keyboard.add(four_btn)
    keyboard.add(five_btn)

    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите приготовить:",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == "1":
            img = open('static/img/1.jpg', 'rb')
            img1 = open('static/img/1_1.jpg', 'rb')
            img2 = open('static/img/1_2.jpg', 'rb')
            img3 = open('static/img/1_3.jpg', 'rb')
            img4 = open('static/img/1_4.jpg', 'rb')
            img5 = open('static/img/1_5.jpg', 'rb')
            img6 = open('static/img/1_6.jpg', 'rb')
            img7 = open('static/img/1_7.jpg', 'rb')
            img8 = open('static/img/1_8.jpg', 'rb')
            img9 = open('static/img/1_9.jpg', 'rb')
            img10 = open('static/img/1_10.jpg', 'rb')
            img11 = open('static/img/1_11.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,)
            bot.send_photo(
                caption='Шаг 1. Как сделать чизкейк без творожного сыра? Подготовьте продукты. Сначала для основы. Печенье возьмите песочное, типа Юбилейного, К кофе, Топленое молоко. Сливочное масло выбирайте качественное, натуральное, без растительных жиров в составе.',
                chat_id=call.message.chat.id,
                photo=img1)
            bot.send_photo(
                caption='Шаг 2. Как сделать основу для чизкейка? Измельчите печенье любым удобным способом. Проще всего это сделать в измельчителе. За неимением можно воспользоваться скалкой, как это сделала я. Сложите печенье в плотный пакет и прокатайте его скалкой. Оно легко превратится в мелкую крошку.',
                chat_id=call.message.chat.id,
                photo=img2)
            bot.send_photo(
                caption='Шаг 3. Сливочное масло растопите любым удобным способом. Можно в микроволновке, можно на водяной бане. Как это сделать читайте в конце рецепта.',
                chat_id=call.message.chat.id,
                photo=img3)
            bot.send_photo(
                caption='Шаг 4. Вылейте масло в песочную крошку и перемешайте. Получится масса похожая на мокрый песок, которая будет слепляться в комок, но потом рассыпаться. Возьмите подходящую форму для выпечки. Удобнее, если она будет разъемной (у меня диаметр 20см). Дно застелите пергаментом. Высыпьте в нее крошку. Стаканом утрамбуйте крошку, формируя основу с дном и бортиками. Поставьте основу запекаться в духовку, предварительно разогретую до 180°С на 10 минут..',
                chat_id=call.message.chat.id,
                photo=img4)
            bot.send_photo(
                caption= 'Шаг 5. Пока запекается основа для чизкейка, приготовьте начинку. Подготовьте продукты для нее. Сметану выбирайте натуральную, без растительных жиров, жирностью минимум 20%. Количество сахара можно уменьшить, начинка получается достаточно сладкой. Крахмал возьмите кукурузный.',
                chat_id=call.message.chat.id,
                photo=img5)
            bot.send_photo(
                caption= 'Шаг 6. Как сделать начинку? Сметану вылейте в миску, всыпьте к ней сахар. Вбейте яйца. Обязательно мойте яйца перед использованием, так как даже на кажущейся чистой скорлупе могут находиться вредные бактерии. Лучше всего использовать моющие средства для пищевых продуктов и щетку. Добавьте крахмал и щепотку ванилина.',
                chat_id=call.message.chat.id,
                photo=img6)
            bot.send_photo(
                caption='Шаг 7. Обычным ручным венчиком перемешайте продукты до однородности. Миксер не понадобится — для чизкейков не важна пышность.',
                chat_id=call.message.chat.id,
                photo=img7)
            bot.send_photo(
                caption='Шаг 8. По прошествии времени (10 минут) достаньте запеченную основу из духовки. Нагрев не выключайте, температуру уменьшите до 160°С.',
                chat_id=call.message.chat.id,
                photo=img8)
            bot.send_photo(
                caption='Шаг 9. Вылейте в нее подготовленную начинку. Запекайте чизкейк от 45 минут до 1 часа до стабилизации серединки. Когда это произойдет выключите духовку и оставьте его до остывания.',
                chat_id=call.message.chat.id,
                photo=img9)
            bot.send_photo(
                caption='Шаг 10. Остывший чизкейк выньте из духовки. Начинка осядет, не пугайтесь, это нормально. Уберите его минимум на 2 часа в холодильник, а еще лучше на всю ночь — тогда чизкейк окончательно стабилизируется и будет хорошо резаться.',
                chat_id=call.message.chat.id,
                photo=img10)
            bot.send_photo(
                caption='Шаг 11. Подавайте чизкейк к столу к чаю или кофе. Можете украсить его ягодами. Приятного аппетита!',
                chat_id=call.message.chat.id,
                photo=img11,
                reply_markup=keyboard)
            img.close()
            img1.close()
            img2.close()
            img3.close()
            img4.close()
            img5.close()
            img6.close()
            img7.close()
            img8.close()
            img9.close()
            img10.close()
            img11.close()


        if call.data == "2":
            img = open('static/img/2.jpg', 'rb')
            img1 = open('static/img/2_1.jpg', 'rb')
            img2 = open('static/img/2_2.jpg', 'rb')
            img3 = open('static/img/2_3.jpg', 'rb')
            img4 = open('static/img/2_4.jpg', 'rb')
            img5 = open('static/img/2_5.jpg', 'rb')
            img6 = open('static/img/2_6.jpg', 'rb')
            img7 = open('static/img/2_7.jpg', 'rb')
            img8 = open('static/img/2_8.jpg', 'rb')
            img9 = open('static/img/2_9.jpg', 'rb')
            img10 = open('static/img/2_10.jpg', 'rb')
            img11 = open('static/img/2_11.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img, )
            bot.send_photo(
                caption='Шаг 1. Как сделать сырники из творога на сковороде? Отмерьте необходимые ингредиенты. Творог подойдет любой жирности. Ванильный сахар можно заменить на ванилин.',
                chat_id=call.message.chat.id,
                photo=img1)
            bot.send_photo(
                caption='Шаг 2. Очень важно выбрать подходящий творог. Он не должен быть влажным. Иначе придется добавлять излишнее количество муки, что сделает тесто тугим и плотным. По этой же причине не стоит использовать мягкий, пастообразный творог. Такой для сырников не подойдет. Если творог крупинчатый или хлопьями, пропустите его через блендер, чтобы получить однородную структуру. Тогда сырники получатся нежными. Можно взять творог в брикетах.',
                chat_id=call.message.chat.id,
                photo=img2)
            bot.send_photo(
                caption='Шаг 3. Выложите творог в подходящую по размеру миску. Добавьте соль, сахар, ванильный сахар, перемешайте. Количество сахара берите по вкусу.',
                chat_id=call.message.chat.id,
                photo=img3)
            bot.send_photo(
                caption='Шаг 4. Добавьте к творогу взбитое яйцо, хорошо перемешайте.',
                chat_id=call.message.chat.id,
                photo=img4)
            bot.send_photo(
                caption='Шаг 5. Всыпьте через сито муку, тщательно перемешайте. Если тесто получается слишком вязкое, добавьте еще совсем немного муки (0,5 ст.л., не более).',
                chat_id=call.message.chat.id,
                photo=img5)
            bot.send_photo(
                caption='Шаг 6. Творожное тесто оставьте на столе на 15 минут. Клейковина в муке разойдется, и сырники будет легче формировать.',
                chat_id=call.message.chat.id,
                photo=img6)
            bot.send_photo(
                caption='Шаг 7. Стол присыпьте немного мукой, скатайте из теста колбаску. Разделите тесто на равные части в зависимости от желаемого размера сырников.',
                chat_id=call.message.chat.id,
                photo=img7)
            bot.send_photo(
                caption='Шаг 8. Каждую часть теста скатайте в колобок, затем прижмите, чтобы получился круглый, средней толщины сырничек. Если тесто прилипает к рукам, припудривайте их мукой.',
                chat_id=call.message.chat.id,
                photo=img8)
            bot.send_photo(
                caption='Шаг 9. На сковороде разогрейте растительное масло, выложите сырники. На умеренном огне обжарьте сырники до румяного цвета.',
                chat_id=call.message.chat.id,
                photo=img9)
            bot.send_photo(
                caption='Шаг 10. Когда сырники зарумянятся, переверните их на другую сторону и жарьте до готовности на медленном огне.',
                chat_id=call.message.chat.id,
                photo=img10)
            bot.send_photo(
                caption='Шаг 11. Подавайте сырники со сметаной, любыми сладкими добавками: вареньем, джемом, сгущенкой. Приятного аппетита!',
                chat_id=call.message.chat.id,
                photo=img11,
                reply_markup=keyboard)
            img.close()
            img1.close()
            img2.close()
            img3.close()
            img4.close()
            img5.close()
            img6.close()
            img7.close()
            img8.close()
            img9.close()
            img10.close()
            img11.close()


        if call.data == "3":
            img = open('static/img/3_6.jpg', 'rb')
            img1 = open('static/img/3_1.jpg', 'rb')
            img2 = open('static/img/3_3.jpg', 'rb')
            img3 = open('static/img/3_2.jpg', 'rb')
            img4 = open('static/img/3_4.jpg', 'rb')
            img5 = open('static/img/3_5.jpg', 'rb')
            img6 = open('static/img/3_6.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img, )
            bot.send_photo(
                caption='Шаг 1. Воду залить в кастрюлю с толстым дном, добавить шоколад, слив. масло и соль щепотку. Довести до кипения на медленном огне, постоянно помешивая.',
                chat_id=call.message.chat.id,
                photo=img1)
            bot.send_photo(
                caption='Шаг 2. Огонь убавить еще, всыпать муку и быстро перемешать.',
                chat_id=call.message.chat.id,
                photo=img2)
            bot.send_photo(
                caption='Шаг 3. Размешивать, пока тесто не будет отлипать от стенок. Вбить яйца по одному, постоянно размешивая.',
                chat_id=call.message.chat.id,
                photo=img3)
            bot.send_photo(
                caption='Шаг 4. Слегка остудить тесто, переложить в мешок кондитерский. И отсадить из него эклеры на застеленный пергаментом противень. Духовку прогреть до 200С и печь эклеры 20 минут.',
                chat_id=call.message.chat.id,
                photo=img4)
            bot.send_photo(
                caption='Шаг 5. Для крема в этом рецепте идут взбитые сливки, но вы можете сделать любой другой крем. Сливки должны быть холодными. Нужно взбивать их миксером до густоты, постепенно добавляя сахарную пудру.',
                chat_id=call.message.chat.id,
                photo=img5)
            bot.send_photo(
                caption='Шаг 6. Каждый эклер наполнить взбитыми сливками через узкую насадку кондитерского мешка. Украсить глазурью из белого шоколада.',
                chat_id=call.message.chat.id,
                photo=img6,
                reply_markup=keyboard
            )
            img.close()
            img1.close()
            img2.close()
            img3.close()
            img4.close()
            img5.close()
            img6.close()


        if call.data == "4":
            img = open('static/img/4.jpg', 'rb')
            img1 = open('static/img/4_1.jpg', 'rb')
            img2 = open('static/img/4_2.jpg', 'rb')
            img3 = open('static/img/4_3.jpg', 'rb')
            img4 = open('static/img/4_4.jpg', 'rb')
            img5 = open('static/img/4_5.jpg', 'rb')
            img6 = open('static/img/4_6.jpg', 'rb')
            img7 = open('static/img/4_7.jpg', 'rb')
            img8 = open('static/img/4_8.jpg', 'rb')
            img9 = open('static/img/4_9.jpg', 'rb')
            img10 = open('static/img/4_10.jpg', 'rb')
            img11 = open('static/img/4_11.jpg', 'rb')
            img12 = open('static/img/4_12.jpg', 'rb')
            img13 = open('static/img/4_13.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img, )
            bot.send_photo(
                caption='Шаг 1. Как сделать простой яблочный пирог шарлотку? Отмерьте необходимые ингредиенты. Яйца возьмите крупные. Для пирога хорошо подойдут кисло-сладкие сорта яблок. Если яблоки мелкие, можно взять 3 плода.',
                chat_id=call.message.chat.id,
                photo=img1)
            bot.send_photo(
                caption='Шаг 2. Муку смешайте с разрыхлителем и просейте через сито. Это увеличит насыщенность муки кислородом, вследствие чего тесто будет лучше подниматься во время выпечки. И пирог получится пышным и воздушным.',
                chat_id=call.message.chat.id,
                photo=img2)
            bot.send_photo(
                caption='Шаг 3. Яблоки помойте, обсушите. Очистите яблоки от семян. Кожицу можно тоже срезать, если она слишком толстая и грубая. Я кожицу не очищала. Нарежьте яблоки средними кубиками.',
                chat_id=call.message.chat.id,
                photo=img3)
            bot.send_photo(
                caption='Шаг 4. Яйца соедините с сахаром и ванильным сахаром. Ванильный сахар можно заменить на ванилин. В этом случае ванилин добавляйте в мучную смесь.',
                chat_id=call.message.chat.id,
                photo=img4)
            bot.send_photo(
                caption='Шаг 5. Взбейте яйца с сахаром на высоких оборотах миксера до пышной, светлой массы. Когда в процессе взбивания венчики миксера будут оставлять видимые, четкие следы, значит, яйца взбились достаточно хорошо и можно прекратить взбивание.',
                chat_id=call.message.chat.id,
                photo=img5)
            bot.send_photo(
                caption='Шаг 6. К взбитой яичной массе постепенно, небольшими порциями всыпьте просеянную с разрыхлителем муку. Можно это делать через сито, тем самым просеивая муку дважды. Всыпая муку, одновременно перемешивайте тесто лопаткой аккуратными зачерпывающими движениями, чтобы максимально сохранить воздушность.',
                chat_id=call.message.chat.id,
                photo=img6)
            bot.send_photo(
                caption='Шаг 7. Тесто получается однородное, воздушное, легкое.',
                chat_id=call.message.chat.id,
                photo=img7)
            bot.send_photo(
                caption='Шаг 8. Дно формы для выпечки (диаметром 22 см) застелите пергаментом. По необходимости смажьте пергамент небольшим количеством масла, бока формы смазывать не нужно. Вылейте в форму треть теста, аккуратно разровняйте.',
                chat_id=call.message.chat.id,
                photo=img8)
            bot.send_photo(
                caption='Шаг 9. Сверху распределите половину нарезанных яблок.',
                chat_id=call.message.chat.id,
                photo=img9)
            bot.send_photo(
                caption='Шаг 10. Затем выложите еще треть теста и сверху оставшиеся кубики яблок.',
                chat_id=call.message.chat.id,
                photo=img10)
            bot.send_photo(
                caption='Шаг 11. Вылейте остальное тесто, аккуратно разровняйте. Можно сразу выложить все яблоки в тесто и перемешать.',
                chat_id=call.message.chat.id,
                photo=img11)
            bot.send_photo(
                caption='Шаг 12. Сразу поставьте пирог в заранее разогретую до 180С духовку примерно на 35-40 минут. Время и режим выпечки могут отличаться, ориентируйтесь на работу своей духовки. Первые 25 минут духовку не открывайте, чтобы от резкого перепада температуры шарлотка не осела. Готовность проверяйте шпажкой. Если она из середины пирога выходит сухой, значит, шарлотка готова. Дайте ей постоять немного в форме, затем вынимайте и остудите на решетке.',
                chat_id=call.message.chat.id,
                photo=img12)
            bot.send_photo(
                caption='Шаг 13. Нарежьте пирог на порционные кусочки и подавайте к столу. Приятного аппетита!',
                chat_id=call.message.chat.id,
                photo=img13,
                reply_markup=keyboard
            )
            img.close()
            img1.close()
            img2.close()
            img3.close()
            img4.close()
            img5.close()
            img6.close()
            img7.close()
            img8.close()
            img9.close()
            img10.close()
            img11.close()
            img12.close()
            img13.close()

    if call.data == "5":
        img = open('static/img/5.jpg', 'rb')
        img1 = open('static/img/5_1.jpg', 'rb')
        img2 = open('static/img/5_3.jpg', 'rb')
        img3 = open('static/img/5_2.jpg', 'rb')
        img4 = open('static/img/5_4.jpg', 'rb')
        img5 = open('static/img/5_5.jpg', 'rb')
        img6 = open('static/img/5_6.jpg', 'rb')
        img7 = open('static/img/5_7.jpg', 'rb')
        img8 = open('static/img/5_8.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img, )
        bot.send_photo(
            caption='Шаг 1. Как сделать пышные панкейки на молоке? Подготовьте ингредиенты. Молоко и яйцо берите свежие, оливковое масло - рафинированное (масло экстра вирджин не подойдет, т.к. будет давать горечь). Оливковое масло можно заменить на любое другое рафинированное масло без выраженного вкуса и запаха.',
            chat_id=call.message.chat.id,
            photo=img1)
        bot.send_photo(
            caption='Шаг 2. В глубокой миске смешайте все сухие ингредиенты - возьмите венчик и секунд 30 мешайте их. Это нужно для правильного и равномерного распределения всех составляющих.',
            chat_id=call.message.chat.id,
            photo=img2)
        bot.send_photo(
            caption='Шаг 3. Добавьте яйцо, перемешайте миксером, затем молоко, снова перемешайте. Добавьте 3 столовых ложки оливкового масла и окончательно перемешайте всё минуты две.',
            chat_id=call.message.chat.id,
            photo=img3)
        bot.send_photo(
            caption='Шаг 4. У вас должно получиться довольно густое тесто (если перевернуть ложку, оно скорее будет падать комками, чем стекать с неё). На самом деле уже после первого раза Вы сразу будете знать правильную консистенцию теста. При необходимости добавьте немного муки или молока, чтобы отрегулировать консистенцию до нужной.',
            chat_id=call.message.chat.id,
            photo=img4)
        bot.send_photo(
            caption='Шаг 5. Разогрейте сковороду на среднем огне БЕЗ МАСЛА и ложкой выкладывайте будущие блинчики.',
            chat_id=call.message.chat.id,
            photo=img5)
        bot.send_photo(
            caption='Шаг 6. Как понять, что пора переворачивать? Дождитесь появления пузырьков по всей поверхности блинчика, а затем можно перевернуть. Обычно на обжарку уходит по 2-3 минуты с каждой стороны.',
            chat_id=call.message.chat.id,
            photo=img6)
        bot.send_photo(
            caption='Шаг 7. Вот и всё, выкладывайте готовые панкейки на тарелку и добавляйте варенье/джемы/сиропы, ягоды, мёд — всё, что нравится.',
            chat_id=call.message.chat.id,
            photo=img7)
        bot.send_photo(
            caption='Шаг 8. Приятного аппетита!',
            chat_id=call.message.chat.id,
            photo=img8,
            reply_markup=keyboard
        )
        img.close()
        img1.close()
        img2.close()
        img3.close()
        img4.close()
        img5.close()
        img6.close()
        img7.close()
        img8.close()


if __name__ == "__main__":
    bot.polling(none_stop=True)