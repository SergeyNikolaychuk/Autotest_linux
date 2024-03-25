# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess

def get_text(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if not result.returncode and text in result.stdout:
        return True
    else:
        return False
    mport
    smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.base import MIMEBase
    from email import encoders

    with open("testdata.yaml") as f:
        testdata = yaml.safe_load(f)

    from_email = testdata["from_email"]
    to_email = testdata["to_email"]
    pass_email = testdata["pass_email"]
    filename = 'log.txt'
    subject = f'report {filename}'
    message_body = 'Здесь наш текст с отчетом о тестировании'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message_body, 'plain'))

    with open(filename, 'rb') as f:
        attach = MIMEBase('application', 'octet-stream')
        attach.set_payload(f.read())
        encoders.encode_base64(attach)
        attach.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(attach)

    smtp_server = 'smtp.mail.ru'
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(from_email, pass_email)

        server.sendmail(from_email, to_email, msg.as_string())

        print('Отчет отправлен')
    except Exception as e:
        print(f'Ошибка {str(e)}')

    finally:
        server.quit()

    21: 01
