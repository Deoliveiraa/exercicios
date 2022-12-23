import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
''' email = outlook.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
email.To = "lucas187ro@gmail.com; lucca187ro@gmail.com"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
<p>Olá Lucas, aqui é o código Python</p>

<p>O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>O ticket Médio foi de R${ticket_medio}</p>

<p>Abs,</p>
<p>Código Python</p>
"""

# anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
# email.Attachments.Add(anexo)

email.Send()
print("Email Enviado") '''


import smtplib
import email.message

def enviar_email(corpo): 
    corpo = '''
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    '''


msg = email.message.Message()
msg['Subject'] = 'Email automatico do Python'
msg['From'] = 'lucas187r0@gmail,com'
msg['To'] = 'lucas187_ro@hotmail.com', 'lucca187ro@gmail.com'
password = 'tintvojznjxgkakl'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(enviar_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')