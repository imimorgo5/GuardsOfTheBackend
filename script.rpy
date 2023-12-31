﻿define Alexey = Character('Алексей', color="#9c5024")
define Anastasia = Character('Анастасия', color="#5f1717")
define Student_1 = Character('Студент Миша', color="#63b098")
define Student_2 = Character('Студент Алина', color="#595293")
define Vova = Character('Вова', color="#a4a038")
define Autor = Character('Автор', color="#000000")

define audio.portal = "audio/portal.mp3"
define audio.start_end = "audio/start_and_end.mp3"
define audio.depressive_part = "audio/second_part.mp3"
define audio.university = "audio/university.mp3"
define audio.end = "audio/end.mp3"
define audio.room = "audio/room_part.mp3"
define audio.memories = "audio/memories.mp3"
define audio.atraction = "audio/atrpark.mp3"
define audio.restaurant = "audio/citycafe.mp3"
define audio.kino = "audio/kino.mp3"
define audio.badend = "audio/badend.mp3"

define v = 0
define flag = False

label start:
    stop music fadeout 1
    play music start_end fadein 0.5
    scene ulitsa with fade
    $ main_name = renpy.input("Как будут звать главного героя?\nВведите мужское имя: ", length = 20).strip() or "Сергей"
    define main_character = Character('[main_name]', color="#1c86b3")

    Autor "[main_name], Алексей и Анастасия - работники фотомастерской, где основной услугой является внедрение в сознание человека через его фото для получения информации из прошлого."

    Autor "Это был обычный день. Анастасия подходит к фотомастерской и первым делом смотрит почтовый ящик на наличие заказов. Там лежит конверт с фотографией. Она забирает его и заходит в помещение."
    
    scene masterskaya with dissolve

    show chernova:
        xalign 0.3
        yalign 1.1
    with easeinleft

    Anastasia "Всем привет, у нас новый заказ!"
    main_character "Пожалуйста, не говори, что снова от той женщины..."
    Anastasia "К твоему счастью, имени я не знаю, клиент решил остаться анонимным."

    show chernova:
        xalign 0.55
        yalign 1.1
    with ease

    show kornilov:
        xalign 0.3
        yalign 1.1
    with easeinleft

    Alexey "А какая у клиента проблема? Чем мы можем помочь?"
    Anastasia "Это странно... Но в конверте только фотография и больше ничего..."
    main_character "Действительно странно... Но загадочно... Может я попробую погрузиться в сознание человека на фото?"
    Alexey "Это может быть опасно."
    Anastasia "Ты точно уверен, что хочешь сделать это?"
    main_character "Да что может пойти не так! Уверен, это просто какая-то шутка! Не переживайте!"
    Alexey "Ну, тогда погнали!"
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

    play music depressive_part fadein 0.5
    scene depressiv
    main_character "Где я? Что происходит?"
    Autor "Вдруг [main_name] резко начинает ощущать адскую боль."
    main_character "БОЖЕ, КАК БОЛЬНО!"
    Autor "Тело человека, в которого вселился [main_name], начинает биться в агонии. Перед ним проносятся воспоминания."

    play sound memories fadein 0.5
    scene family with dissolve
    pause(0.35)
    scene school with dissolve
    pause(0.35)
    scene hospital with dissolve
    pause(0.35)
    stop sound fadeout 0.5

    scene depressiv with dissolve
    main_character "Его звали Вова... Мама... Она умерла... Он потерял смысл к жизни..."
    main_character "У него были мечты... о хорошем образовании... об успешной карьере в IT-индустрии... "
    main_character "У меня тоже были мечты..."
    main_character "НЕТ! Я не дам этому случиться вновь! Я всё исправлю!"

    Alexey "[main_name]! [main_name]! Ты слышишь меня?!"
    show kornilov_seriously at center with dissolve
    Alexey "Я наконец-то нашёл тебя! Немедленно возвращайся!"   
    main_character "Нет, я не могу, я должен помочь ему исполнить мечту!"
    hide kornilov_seriously
    show kornilov_scream at center
    Alexey "ТЫ С УМА СОШЁЛ?! Нам нельзя вмешиваться в чужие жизни! Ты понимаешь, что можешь натворить?!"
    hide kornilov_scream
    show kornilov_angry at center

    menu:
        "Остаться":
            jump stay
        "Вернуться":
            main_character "Ладно, извини, Алексей, ты прав, о чём я вообще думаю, это действительно опасно, я возвращаюсь..."
            jump bad_end
    return

label stay:        
    main_character "ЭТО НЕ ВАЖНО! Я остаюсь!"
    hide kornilov_angry
    show kornilov_scream at center
    Alexey "ТАК НЕЛЬЗЯ, ТЫ...{nw}"
    stop music

    scene plaid
    play music portal
    pause(0.5)
    stop music fadeout 0.1

    play music room fadein 0.5
    scene room
    main_character "Чёрт, опять... Где я теперь?"
    main_character "Я в прошлом! В сознании Вовы!"
    Autor "В зеркале [main_name] увидел парня лет 18, который погибнет в будущем, если ему не помочь."
    main_character "Кажется, прошёл примерно месяц, как не стало его матери, физическое и ментальное состояние практически на нуле, отец всё время пьёт и не следит за сыном."
    main_character "Я помогу тебе, Вова! Я направлю тебя на правильный путь! Твоя жизнь станет лучше!"
    jump depressiv_war
    return

label depressiv_war:
    stop music fadeout 1
    scene black with dissolve
    centered "{cps=15}{font=carbonara.ttf}{color=#ffffff}{size=100}На следующий день...{p=0.5}{nw}"
    play music start_end fadein 0.5
    scene park_2 with dissolve
    show zero_progress:
        xalign 0.5
        yalign 0.05

    menu:
        main_character "Итак, мне нужно помочь Вове справиться с депрессией. Что же сделать?" 
        "Сходить в парк развлечений":
            $ v = 1
            jump atraction_park
        "Погулять и пообщаться с друзьями":
            $ v = 2
            jump walk
        "Сходить в кино":
            $ v = 3
            jump cinema
        "Ничего не делать":
            main_character "Алексей был прав, что я тут забыл, пора возвращаться домой, Вова справится и без моей помощи..."
            jump bad_end
    return

label depressive_war_2:
    $ flag = True
    show past_progress:
        xalign 0.5
        yalign 0.05

    if v == 1:
        menu:
            main_character "Этого оказалось недостаточно, нужно сделать что-то ещё."
            "Погулять и пообщаться с друзьями":
                jump walk
            "Сходить в кино":
                jump cinema
            "Ничего не делать":
                main_character "Алексей был прав, что я тут забыл, пора возвращаться домой, Вова справится и без моей помощи..."
                jump bad_end
    
    elif v == 2:
        menu:
            main_character "Этого оказалось недостаточно, нужно сделать что-то ещё."
            "Сходить в парк развлечений":
                jump atraction_park
            "Сходить в кино":
                jump cinema
            "Ничего не делать":
                main_character "Алексей был прав, что я тут забыл, пора возвращаться домой, Вова справится и без моей помощи..."
                jump bad_end        
    
    elif v == 3:
        menu:
            main_character "Этого оказалось недостаточно, нужно сделать что-то ещё."
            "Сходить в парк развлечений":
                jump atraction_park
            "Погулять и пообщаться с друзьями":
                jump walk
            "Ничего не делать":
                main_character "Алексей был прав, что я тут забыл, пора возвращаться домой, Вова справится и без моей помощи..."
                jump bad_end
    return

label atraction_park:
    play sound atraction fadein 0.5
    scene atrpark with fade
    pause(1)
    scene rail with dissolve
    pause(1)
    scene atr with dissolve
    pause(1)
    scene circle with dissolve
    pause(1)
    stop sound fadeout 0.5
    scene atrpark with dissolve
    if flag:
        jump univercity
    jump depressive_war_2
    return

label walk:
    play sound restaurant fadein 0.5
    scene city1 with fade
    pause(1)
    scene city2 with dissolve
    pause(1)
    scene table_hand with dissolve
    pause(1)
    scene table_high with dissolve
    pause(1)
    scene night_city with dissolve
    stop sound fadeout 0.5
    if flag:
        jump univercity
    jump depressive_war_2
    return

label cinema:
    play sound kino fadein 0.5
    scene out_cinema with fade
    pause(1)
    scene cinema_1 with dissolve
    pause(1)
    scene cinema_0 with dissolve
    pause(1)
    scene cinema_2 with dissolve
    pause(1)
    scene out_cinema with dissolve
    stop sound fadeout 0.5
    if flag:
        jump univercity
    jump depressive_war_2
    return

label bad_end:
    scene plaid
    play music portal
    pause(0.5)
    stop music fadeout 0.1

    play music room_part fadein 0.5
    scene masterskaya
    pause(0.1)

    show chernova:
        xalign 0.6
        yalign 1.1
    with easeinleft

    show kornilov:
        xalign 0.3
        yalign 1.1
    with easeinleft

    Anastasia "Ты вернулся! Я рада тебя видеть!"
    Alexey "Хорошо, что ты одумался и не стал рисковать!"
    main_character "Но правильно ли я поступил? Я сделал только хуже..."

    play music badend fadein 1
    scene forest with dissolve
    $ renpy.notify("Вы открыли плохую концовку...")
    Autor "В конце концов, [main_name] не смог справиться с чувством вины и стал потреблять много спиртного, что полностью разрушило его жизнь. Он, Анастасия и Алексей не добились успеха со свой фотомастерской, их бизнес рухнул и они перестали общаться."
    Autor "Вова не смог справиться с чувствами после гибели матери и покончил жизнь самоубийством."      
    window hide
    scene black with dissolve
    centered "{font=carbonara.ttf}{color=#ffffff}{size=100}Конец...{p=1.0}{nw}"
    return

label univercity:
    show full_progress:
        xalign 0.5
        yalign 0.05
    main_character "Теперь Вове стало намного лучше."
    scene black with dissolve
    stop music fadeout 1
    centered "{cps=15}{font=carbonara.ttf}{color=#ffffff}{size=100}Пару недель спустя...{p=0.5}{nw}"
    play music university fadein 0.5
    scene urfu with fade
    main_character "Итак, я вылечил Вову от депрессии, познокомил его с новыми людьми. К нему вернулась мотивация учиться и стать специалистом в IT-сфере, но он ещё не определился кем именно хочет стать. Это моя последняя задача - помочь Вове с выбором профессии!"
    main_character "Сегодня в этом замечательном и лучшем университете проходит день открытых дверей. Здесь-то я и помогу Вове понять, с чем ему связать свою жизнь."

    scene urfu_humans with dissolve
    Vova "Как же здесь много людей! Это всё будущие студенты?!"

    show student_1_normal at center with easeinleft

    Student_1 "Да! Как же приятно видеть, что такое большое количество молодых людей в наше время стремится получить хорошее образование! Как я понимаю, вы тоже собираетесь поступать, вам рассказать про направления обучения?"
    hide student_1_normal
    show student_1_smile at center
    Vova "Да, можете подробнее рассказать об IT-профессиях, которым здесь обучают?"
    hide student_1_smile
    show student_1_normal at center
    Student_1 "Конечно, пройдёмте за мной!"
    hide student_1_normal with easeoutleft

    main_character "С каждой минутой мне всё больше нравиться это место. Эх, как жаль, что я не мог тут учиться."

    scene urfu_tables with dissolve    
    Student_1 "Так, проходите сюда, это павильон радиофака. Здесь вам всё расскажут про Информационные технологии."

    show student_2_normal at right with easeinright

    menu:
        Student_2 "Привет, меня зовут Алина. В нашем университете можно обучиться на frontend-, backend-разработчика и специалиста по кибербезопасности. О какой из этих профессий тебе рассказать?"
        "О Frontend-разработке":
            jump frontend
        "О Backend-разработке":
            jump backend
        "О профессии специалиста по кибербезопасности":
            jump cybersecurity
    return

label cybersecurity:
    Vova "Расскажите мне о профессии специалиста по кибербезопасности, мне интересно это направление, но я плохо понимаю в чём суть."
    Student_2 "Хорошо, начнём с того, что специалист по кибербезопасности — это тот, кто обеспечивает защиту IT-системы от взломов, которые приводят к сбоям в работе и утечкам данных."
    Student_2 "90 процентов всех мошеннических действий сейчас совершается в киберпространстве, поэтому кибербезопасность – очень перспективная IT-специализация."
    Vova "А что умеет такой специалист?"
    Student_2 "Cпециалист по безопасности обладает знаниями и навыками в следующих сферах: разработка и тестирование, построение архитектуры, управление рисками, психология, правовая база."
    Student_2 "Проще говоря, кибербезопасник – это и айтишник, и разработчик, и тестировщик, и риск-менеджер, и психолог, и юрист, и человек, который может рассказать понятным языком о каждой из этих областей знания."
    Vova "Хм, звучит интересно! Но не уверен, что это для меня. Чтобы точно определиться, я хочу узнать ещё об одной профессии, о backend-разработке."
    Student_2 "Без проблем!"
    jump second_backend
    return

label frontend:
    Vova "Расскажите мне о frontend-разработке, мне интересно это направление, но я плохо понимаю в чём суть."
    Student_2 "Хорошо, начнём с того, что frontend - это разработка пользовательского интерфейса и функций, которые работают на клиентской стороне веб-сайта или приложения. Проще говоря, это всё, что видит пользователь, открывая веб-страницу, и с чем он взаимодействует."
    Vova "А в чём заключается работа frontend-разработчика, что именно входит в его задачи?"
    Student_2 "Задача frontend-разработчика - воплотить техническое содержание сайта в форме, которую предлагает дизайнер. Для этого он, делает дизайн-макет, как бы, живым: верстает сервис, добавляет текст, изображения, кнопки, иконки, настраивает интерактивность страниц, адаптирует сервис для разных устройств."
    Student_2 "Считается, что для frontend-разработки необходимы знания в таких сферах, как язык HTML (разметка), язык CSS (стили) и язык JavaScript (скрипты)."
    Vova "Хм, звучит интересно! Но не уверен, что это для меня. Думаю, чтобы точно определиться с профессией, мне нужно узнать и о backend-разработке тоже."
    Student_2 "Конечно, ведь эти направления неразрывно связаны между собой. Бэкенд отвечает за взаимодействие пользователя с внутренними данными, которые потом отображает фронтенд."
    jump second_backend
    return

label backend:
    Vova "Расскажите мне о backend-разработке, мне интересно это направление, но я плохо понимаю в чём суть."
    Student_2 "Хорошо, начнём с того, что backend - это внутренняя часть продукта, отвечающая за логику и хранение данных, она находится на сервере и скрыта от пользователя."
    Student_2 "Для разработки на бэкенде используются самые разные языки, например, Python, PHP, Go, Java, С#. Рекомендую начинать с Python, потому что он топовый, ловкий и быстрый."
    Vova "А чем занимаются backend-разработчики?"
    Student_2 "Они работают над тем, чтобы веб-ресурс был функциональным, надежным и безопасным, реализуют внутреннюю логику работы приложения, обеспечивает его взаимодействие с базами данных и внешними сервисами."
    Vova "Хм, звучит интересно!"
    jump test
    return

label second_backend:
    Student_2 "Backend - это внутренняя часть продукта, она находится на сервере и скрыта от пользователя."
    Student_2 "Разработчики здесь делают так, чтобы веб-ресурс был функциональным, надежным и безопасным, реализуют внутреннюю логику работы приложения, обеспечивают его взаимодействие с базами данных и внешними сервисами."
    Student_2 "Для разработки на бэкенде используются самые разные языки, например, Python, PHP, Go, Java, С#. Рекомендую начинать с Python, потому что он топовый, ловкий и быстрый."        
    Vova "Кажется, это то, что я и искал, теперь я точно определился."
    jump test
    return

label test:
    hide student_2_normal
    show student_2_laught at right
    Student_2 "У меня ещё есть картинки с мемами про backend. Вот возьми."

    show memes:
        xalign 0.5
        yalign 0.1     
    with easeinbottom
    "\"XD\""
    hide memes with easeouttop

    hide student_2_laught
    show student_2_normal at right
    menu:
        Student_2 "Хочешь пройти небольшой тест на общие знания об IT?"
        "Да":
            jump test1
        "Нет":
            jump notest
    return

label test1:
    menu:
        Student_2 "Какое из этих расширений используется для хранения видео?"
        ".mp4":
            show student_2_laught at right
            Student_2 "{color=#15ff00}Правильно!{/color} Категория видео файлов включает в себя огромный спектр видео форматов, которые используют различные кодеки для кодирования и сжатия данных. Самые распространённые из них: .mp4, .MPG, .MOV, .WMV, и .AVI."
            Student_2 "Теперь держи вопрос посложнее"
            jump test2
        ".jpg":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test1
        ".mp3":
            show student_2_sad at right               
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test1
        ".txt":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test1
    return

label test2:
    hide student_2_laught
    show student_2_normal at right
    menu:
        Student_2 "Каким языком является Python?"
        "Аспектно-ориентированный":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test2
        "Логический":   
            show student_2_sad at right         
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test2
        "Функциональный":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test2
        "Объектно-ориентированный":
            show student_2_laught at right
            Student_2 "{color=#15ff00}Правильно!{/color} Помимо Python, к объектно-ориентированным языкам также относятся Java, C, C#, Ruby и др."
            Student_2 "Хорошо, вот следующий вопрос"
            jump test3
    return

label test3:
    hide student_2_laught
    show student_2_normal at right
    menu:
        Student_2 "Какие бывают разрядности у современных процессоров?"
        "32 и 64 бита":
            show student_2_laught at right
            Student_2 "{color=#15ff00}Правильно!{/color} Остался всего один вопрос, самый сложный)"
            jump test4
        "12 и 32 бита":
            show student_2_sad at right         
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test3
        "15 и 32 бита":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test3
        "86 и 64 бита":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test3
    return

label test4:
    hide student_2_laught
    show student_2_normal at right
    menu:
        Student_2 "Что такое API?"
        "Это система вывода текста в командную оболочку.":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test4
        "Это ядро операционной системы.":
            show student_2_sad at right           
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test4
        "Это программный интерфейс, с его помощью программы общаются друг с другом.":
            show student_2_laught at right
            Student_2 "{color=#15ff00}Правильно!{/color} Ты молодец, ответил правильно на все вопросы! Надеюсь увидеть тебя этим летом при подаче документов, удачи!"
            Vova "Спасибо, благодаря вам я теперь знаю, кем хочу стать!"
            jump end
        "Это интерфейс подключенного к компьютеру принтера.":
            show student_2_sad at right
            Student_2 "{color=#f00}Не правильно...{/color} Подумай ещё)"
            jump test4
    return

label notest:
    Student_2 "Ну, нет так нет, надеюсь увидеть тебя этим летом при подаче документов, удачи!"
    Vova "Спасибо, благодаря вам я теперь знаю, кем хочу стать!"
    jump end
    return

label end:
    scene park with dissolve
    main_character "Я рад за Вову, что у него будет другая жизнь, более счастливая, чем у меня. Ведь я тоже хотел стать разработчиком, но после гибели моих родителей эти мечты были разбиты. Я воплотил свою мечту для другого человека. И не жалею об этом!"
    main_character "А теперь мне пора возвращаться домой!"
    stop music

    scene plaid
    play music portal
    pause(0.5)
    stop music fadeout 0.1

    play music start_end fadein 0.5
    scene masterskaya
    pause(0.1)

    show chernova:
        xalign 0.6
        yalign 1.1
    with easeinleft

    show kornilov:
        xalign 0.3
        yalign 1.1
    with easeinleft

    Anastasia "[main_name] ты вернулся, живой и невредимый! Мы так рады тебя видеть!"

    hide kornilov
    show kornilov_angry_short:
        xalign 0.3
        yalign 1.1

    Alexey "Но это не отменяет того факта, что мы всё ещё злы на тебя, так как ты нарушил наши правила и мог натворить много дел!"

    hide chernova
    show chernova_seriously:
        xalign 0.6
        yalign 1.1

    Anastasia "Да, это был безответственный и необдуманный поступок, который мог всех нас погубить!"

    main_character "Я тоже рад вас видеть! Извините меня, я понимаю, что это было опасно, но зато я подарил тому парню лучшую жизнь, которой у меня никогда не было и уже не будет..."

    stop music fadeout 1
    play music end fadein 0.5
    scene masterskaya_2 with dissolve
    $ renpy.notify("Вы открыли хорошую концовку!")
    Autor "В конце концов, спустя 5 лет, [main_name], Анастасия и Алексей добились успеха со свой фотомастерской, их бизнес рос и расширялся, принося им много денег."
    show tyandex with dissolve
    Autor "Вова поступил на бюджет в ВУЗ своей мечты, закончил обучение с отличием и устроился в крупную компанию \"Тяндекс\" на высокоплачиваемую должность."        
    window hide
    scene black with dissolve
    centered "{cps=15}{font=carbonara.ttf}{color=#ffffff}{size=100}Конец!{p=1.0}{nw}"
    return