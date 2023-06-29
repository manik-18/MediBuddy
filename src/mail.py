import smtplib


def mail(receiver_mail_id, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("mail_id", "your_password")
    s.sendmail("mail_id", receiver_mail_id, message)
    s.quit()
