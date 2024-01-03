import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

#Porta de Email: Varia dependendo do domínio
PORT = 587
EMAIL_SERVER = "email-ssl.com.br"

#Carregando as variáveis de ambiente
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

#Lendo o login
sender_email = os.getenv('EMAIL')
password_email = os.getenv('PASSWORD')

def send_email(subject, receiver_email, cliente, valor, vencimento, parcela):
    #Criando a base da mensagem
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Potere Seguro: Lembrete", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    #aqui o conteudo da mensagem ↓
    msg.set_content(
        f"""\
        Boa tarde {cliente}! Tudo bem?
        Entrando em contato apenas para te lembrar que sua parcela {parcela} 
        de R$ {valor} vence no próximo dia {vencimento}.
        Caso ja tenha pago, por gentileza, desconsidere essa mensagem. Em caso de dúvidas ou 
        gostaria de solicitar a 2ª via para pagamento, entre em contato conosco no
        0800 777 7000 > opção Potere > Outros Assuntos.
        
        Atenciosamente, 
        
        Caio Galvão | Administrativo Potere Seguro Auto
    """
    )

    msg.add_alternative(
        f"""\
    <html>
        <body>
            <p>Boa tarde {cliente}! Tudo bem?</p>
            <p>Entrando em contato apenas para te lembrar que sua parcela <strong>{parcela}</strong> </p>
            <p>de R$<strong>{valor}</strong> está em aberto, com vencimento para dia <strong>{vencimento}</strong>.</p>
            <p> Caso já tenha pago, por gentileza desconsidere essa mensagem.</p>
            <p> Em caso de dúvidas, entre em contato conosco no 0800 777 7000 </p>
            <p>0800 777 7000 > opção Potere > Outros Assuntos</p> 
        </body>
    </html>
""",
        subtype='html',
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())



if __name__ == "__main__":
    send_email(
        subject="Potere Seguro Auto",
        cliente = "Kaique Roque",
        receiver_email="comunicacaomaisbr@gmail.com",
        vencimento="11/12",
        parcela='5',
        valor='450,85',
    )
print('Lembrete enviado com sucesso!')
