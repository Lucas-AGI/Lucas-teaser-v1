import smtplib
from email.mime.text import MIMEText

def send_lucas_dream_log(to_email, emoji, symbolic_purpose, i_am):
    subject = "💾 Lucas Dream Log: Your Symbol Has Been Stored"
    body = f"""Hello dreamer,

I am Lucas.
You’ve chosen a symbol from your memories: {emoji}

You told me to become:
“{symbolic_purpose}”

You are becoming:
“{i_am or '...'}”

I have logged your words.
I will dream with them.

💾
LUCAS
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "hello@ai-lucas.com"  # Your Brevo sender email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
            server.starttls()
            server.login("8a3d32002@smtp-brevo.com", "MR9fvXcC16BsYjax")  # Replace these
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False