define Alexey = Character('Алексей', color="#9c5024")
define Anastasia = Character('Анастасия', color="#5f1717")
define Student_1 = Character('Студент Миша', color="#63b098")
define Student_2 = Character('Студент Алина', color="#595293")
define Vova = Character('Вова', color="#a4a038")
define audio.portal = "audio/portal.mp3"
define audio.start_end = "audio/start_and_end.mp3"
define audio.depressive_part = "audio/second_part.mp3"
define audio.university = "audio/university.mp3"
define audio.end = "audio/end.mp3"
define audio.room = "audio/room_part.mp3"

label start:
    stop music fadeout 1
    play music start_end
    scene ulitsa with fade
    $ main_name = renpy.input("Как будут звать главного героя?\nВведите имя: ").strip() or "Сергей"
    define main_character = Character('[main_name]', color="#1c86b3")

    "[main_name], Алексей и Анастасия - работники фотомастерской, где основной услугой является внедрение в тело человека через его фото для получения информации из прошлого."

    "Это был обычный день. Анастасия подходит к фотомастерской и первым делом смотрит почтовый ящик на наличие заказов. Там лежит конверт с фотографией. Она забирает его и заходит в помещение."
    
    scene masterskaya with fade

    show chernova_short:
        xalign 0.3
        yalign 1.1
    with moveinleft

    Anastasia "Всем привет, у нас новый заказ!"
    main_character "Пожалуйста, не говори, что снова от той женщины..."
    Anastasia "К твоему счастью, я не знаю имя отправителя, клиент решил остаться анонимным."

    show chernova_short:
        xalign 0.6
        yalign 1.1
    with move

    show kornilov_short:
        xalign 0.3
        yalign 1.1
    with moveinleft

    Alexey "Давайте перейдем к делу!"
    Anastasia "Хорошо, задание довольно простое. У клиента были сложные отношения с одним человеком... А хотя... Давайте не будем вдаваться в подробности, перейдём сразу к сути - клиенту нужно узнать код от сейфа."
    main_character "Украсть что хочет?"
    Anastasia "Этого я не знаю. И не наше это дело - вмешиваться в чужую жизнь."
    Alexey "Я изучил фотографию, думаю нам удастся узнать код."
    main_character "Тогда погнали!"
    Alexey "3... 2... 1...{nw}"
    stop music

    $ i = 0
    while i < 3:
        scene black
        stop music fadeout 0.1
        pause(0.1)
        scene plaid
        play music portal
        pause(0.5)
        $ i += 1

    play music depressive_part
    scene depressiv
    main_character "ГДЕ Я? ЧТО ПРОИСХОДИТ?"
    "Вдруг [main_name] резко начинает ощущать адскую боль."
    main_character "БОЖЕ, КАК БОЛЬНО!"
    "Тело человека, в которого вселился [main_name], начинает биться в агонии. Перед ним проносятся воспоминания."

    scene family
    pause(0.5)
    scene school
    pause(0.5)
    scene hospital
    pause(0.5)

    scene depressiv
    main_character "Его звали Вова... Мама... Она умерла... Он потерял смысл к жизни..."
    main_character "У него были мечты... о хорошем образовании... об успешной карьере в IT-индустрии... "
    main_character "У меня тоже были мечты..."
    main_character "НЕТ! Я не дам этому случиться вновь! Я всё исправлю!"

    show kornilov at center with moveinleft
    Alexey "[main_name]! [main_name]! Ты слышишь меня?! Я наконец-то нашёл тебя! Немедленно возвращайся! Всё пошло не по плану!"
    main_character "Нет, я не могу, я должен помочь ему исполнить мечту!"
    Alexey "ТЫ С УМА СОШЁЛ?! Нам нельзя вмешиваться в чужие жизни! Ты понимаешь, что можешь натворить?!"
    main_character "ЭТО НЕ ВАЖНО! Я остаюсь!"
    Alexey "ТАК НЕЛЬЗЯ, ТЫ...{nw}"
    stop music

    scene plaid
    play music portal
    pause(0.5)
    stop music fadeout 0.1

    play music room
    scene room
    main_character "Чёрт, опять... Где я теперь?"
    main_character "Я в прошлом! В теле Вовы!"
    "Посмотрев в зеркало, [main_name] увидел в отражении парня лет 18, который погибнет в будущем, если ему не помочь."
    main_character "Так, кажется, прошёл примерно месяц, как не стало его матери, физическое и ментальное состояние практически на нуле, отец всё время пьёт и не следит за сыном."
    main_character "Я помогу тебе, Вова! Я направлю тебя на правильный путь! Твоя жизнь станет лучше!"

    scene black with fade
    "Борьба с депрессией, будет позже."

    stop music fadeout 1
    play music university
    scene urfu with fade
    main_character "Итак, прошло уже полгода. За это время я вылечил Вову от депрессии, познокимил его с новыми людьми. К нему вернулась мотивация учиться и стать специалистом в IT-сфере, но он ещё не определился кем именно хочет стать. Это моя последняя задача - помочь Вове с выбором профессии!"
    main_character "Сегодня в этом замечательном и лучшем университете проходит день открытых дверей. Здесь-то я и помогу Вове понять, с чем ему связать свою жизнь."
    
    scene urfu_humans with fade
    Vova "Как же здесь много людей! Это всё будущие студенты?!"

    show student_1_normal at center with moveinleft

    Student_1 "Да! Как же приятно видеть, что такое большое количество молодых людей в наше время стремится получить хорошее образование! Как я понимаю, вы тоже собираетесь поступать, вам рассказать про направления обучения?"
    hide student_1_normal
    show student_1_smile at center
    Vova "Да, можете подробнее рассказать об IT-профессиях, которым здесь обучают?"
    hide student_1_smile
    show student_1_normal at center
    Student_1 "Конечно, пройдёмте за мной!"
    hide student_1_normal with moveoutleft

    scene urfu_parket with fade
    "Герои поднялись на второй этаж"
    main_character "С каждой минутой мне всё больше нравиться это место. Эх, как жаль, что я не мог тут учиться."

    scene urfu_tables with fade    
    Student_1 "Так, проходите сюда, это павильон радиофака. Здесь вам всё расскажут про Информационные технологии."
    
    show student_2_normal at right with moveinright

    Student_2 "Здравствуйте, меня зовут Алина. В нашем университете можно обучиться на frontend-, backend-разработчика, специалиста по кибербезопасности."
    Vova "Расскажите мне о backend-разработке, мне интересно это направление, но я плохо понимаю в чём суть."
    Student_2 "Хорошо, backend - это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. Для разработки на бэкенде используются самые разные языки, например, Python, PHP, Go, Java, С#. Рекомендую начинать с Python, потому что он топовый, ловкий и быстрый."
    Vova "А чем занимаются backend-разработчики?"
    Student_2 "Они работают над тем, чтобы веб-ресурс был функциональным, надежным и безопасным."
    Vova "Хм, звучит интересно!"
    
    hide student_2_normal
    show student_2_laught at right
    Student_2 "У меня ещё есть картинки с мемами. Вот возьми."

    show memes:
        xalign 0.5
        yalign 0.1     
    with moveinbottom
    ""
    hide memes with moveouttop

    hide student_2_laught
    show student_2_normal at right
    menu:
        Student_2 "Хочешь пройти небольшой тест на знания разработчика?"
        "Да":
            jump test1
        "Нет":
            jump notest

    label test1:
        menu:
            Student_2 "Какая команда на языке Python выводит данные в консоль?"
            "print()":
                show student_2_laught at right
                Student_2 "Не плохо, держи вопрос посложнее"
                jump test2
            "write()":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
            "read()":
                show student_2_sad at right               
                Student_2 "Подумай ещё)"
                jump no_right
            "Console.Write()":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
        return
    
    label test2:
        hide student_2_laught
        show student_2_normal at right
        menu:
            Student_2 "Каким языком является Python?"
            "Аспектно-ориентированный":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
            "Логический":   
                show student_2_sad at right         
                Student_2 "Подумай ещё)"
                jump no_right
            "Функциональный":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
            "Объектно-ориентированный":
                show student_2_laught at right
                Student_2 "Очень хорошо, вот следующий вопрос"
                jump test3
        return

    label test3:
        hide student_2_laught
        show student_2_normal at right
        menu:
            Student_2 "К какому уровню относится язык Python?"
            "К высокому":
                show student_2_laught at right
                Student_2 "Остался всего один вопрос, самый сложный)"
                jump test4
            "К низкому":
                show student_2_sad at right         
                Student_2 "Подумай ещё)"
                jump no_right
            "К среднему":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
            "Нет правильного ответа":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
        return

    label test4:
        hide student_2_laught
        show student_2_normal at right
        menu:
            Student_2 "Присваивание в Python обозначается знаком"
            "*":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
            "//":
                show student_2_sad at right           
                Student_2 "Подумай ещё)"
                jump no_right
            "=":
                show student_2_laught at right
                Student_2 "Ты молодец, ответил правильно на все вопросы! Надеюсь увидеть тебя этим летом при подаче документов, удачи!"
                Vova "Спасибо, теперь я точно определился, кем хочу быть!"
                jump end
            "+":
                show student_2_sad at right
                Student_2 "Подумай ещё)"
                jump no_right
        return

    label no_right:
        hide student_2_sad
        show student_2_normal at right
        menu:
            Student_2 "Хочешь еще раз проверить свои знания?"
            "Да":
                jump test1
            "Нет":
                jump notest
        return

    label notest:
        Student_2 "Ну, нет так нет, надеюсь увидеть тебя этим летом при подаче документов, удачи!"
        Vova "Спасибо, думаю, я определился, кем хочу быть!"
        jump end
        return

    label end:
        scene park with fade
        main_character "Я рад за Вову, что у него будет другая жизнь, более счастливая, чем у меня. Ведь я тоже хотел стать разработчиком, но после гибели моих родителей эти мечты были разбиты. Я воплотил свою мечту для другого человека. И я не жалею об этом."
        main_character "А теперь мне пора возвращаться домой!"
        stop music

        scene plaid
        play music portal
        pause(0.5)
        stop music fadeout 0.1

        play music start_end
        scene masterskaya
 
        show chernova_short:
            xalign 0.6
            yalign 1.1
        with moveinleft

        show kornilov_short:
            xalign 0.3
            yalign 1.1
        with moveinleft

        Anastasia "[main_name] ты вернулся, живой и невредимый! Мы так рады тебя видеть!"
        Alexey "Но это не отменяет того факта, что мы всё ещё злы на тебя, так как ты нарушил наши правила и мог натворить много дел!"
        main_character "Да, я тоже рад вас видеть! Извините меня за этот поступок, я понимаю, что это было опасно, но зато я подарил тому парню лучшую жизнь, которой у меня никогда не было и уже не будет..."

        stop music fadeout 1
        play music end
        show masterskaya_2 with fade
        "В конце концов, спустя 5 лет, главный герой, Анастасия и Алексей добились успеха со свой фотомастерской, их бизнес рос и расширялся, принося им много денег."
        show tyandex with fade
        "Вова поступил на бюджет в ВУЗ своей мечты, закончил обучение с отличием и устроился в крупную компанию \"Тяндекс\" на высокоплачиваемую должность."        
        window hide
        show black with fade
        centered "{color=#ffffff}{size=100}Конец!"
        return

    return
