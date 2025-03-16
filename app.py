from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = getenv('SECRET_KEY')

mail = Mail(app)

class Contact:
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContact = Contact(
            request.form['name'],
            request.form['email'],
            request.form['subject'],
            request.form['message']
        )

        msg = Message(
            subject=f'Portfólio - Nova Mensagem: {formContact.subject} - {formContact.name}',
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME'], 'marcelosantostecnologia@gmail.com'],
            body = f'''
            Olá Marcelo,
        
            Você recebeu uma nova mensagem através do seu portfólio.
        
            Detalhes do remetente:
            Nome: {formContact.name}
            E-mail: {formContact.email}
        
            Mensagem:
            {formContact.message}
        
            Atenciosamente,
            Seu Portfólio
            '''
        )

        try:
            mail.send(msg)
            flash('Mensagem enviada com sucesso!', 'success')
        except:
            flash('Erro ao enviar a mensagem. Tente novamente mais tarde.', 'danger')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
