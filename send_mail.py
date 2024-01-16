import smtplib
from email.mime.text import MIMEText

def send_mail(user, movie, genres, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'b14b64f16eb8b2'
    password = '0141d89741c7df'
    message = f"<h3>New Feedback Received</h3><ul><li>User: {user}</li><li>Movie: {movie}</li><li>Genres: {genres}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
        
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Netflix movie feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
