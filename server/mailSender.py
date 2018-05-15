import smtplib
from smtplib import SMTP, SMTPException, SMTPAuthenticationError, SMTPServerDisconnected, SMTPResponseException, SMTPSenderRefused, SMTPRecipientsRefused

def sendOfferEmail(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    succes_message = "Mail send with succes"
    fail_message = "Mail sending error"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print(succes_message)

    except (SMTPAuthenticationError, SMTPServerDisconnected, SMTPResponseException, SMTPSenderRefused, SMTPRecipientsRefused) as err:
        print(fail_message)
        print(err)
        print(err.args)

