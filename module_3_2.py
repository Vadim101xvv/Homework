def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if ('@' or ('.com', '.ru', '.net')) not in recipient:
        print('невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('письмо успешно отправленно с адреса', sender, 'на адрес', recipient)
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправленно с адреса', sender, 'на адрес', recipient)
send_email('это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')