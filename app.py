# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Замените на случайный ключ

# Настройки почты
SMTP_SERVER = 'smtp.mail.ru'
SMTP_PORT = 587
EMAIL_ADDRESS = 'oni007@mail.ru'
EMAIL_PASSWORD = 'пароль'  # Замените на пароль от почты


@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        # Получаем данные из формы
        name = request.form['name']
        phone = request.form['phone']
        email = request.form.get('email', 'Не указан')
        message = request.form['message']

        # Создаем сообщение
        subject = f'Новое сообщение от {name}'
        body = f"""
        Имя: {name}
        Телефон: {phone}
        Email: {email}

        Сообщение:
        {message}

        ---
        Это сообщение отправлено с сайта ProAuto
        """

        # Настраиваем email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Отправляем email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        flash('Сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.', 'success')
        return redirect(url_for('contacts'))

    except Exception as e:
        flash('Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.', 'error')
        return redirect(url_for('contacts'))


# Остальные маршруты остаются без изменений
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/key_selection')
def key_selection():
    return render_template('key_selection.html')


@app.route('/expert')
def expert():
    return render_template('expert.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/urgent_buyout')
def urgent_buyout():
    return render_template('urgent_buyout.html')


@app.route('/diagnostic')
def diagnostic():
    return render_template('diagnostic.html')


@app.route('/expert_on_duty')
def expert_on_duty():
    return render_template('expert_on_duty.html')


if __name__ == '__main__':
    app.run(debug=True)
