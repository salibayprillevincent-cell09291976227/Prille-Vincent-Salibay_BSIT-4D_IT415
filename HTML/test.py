import smtplib 
import schedule 
import time 
import random 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
 
# Gmail credentials (  must enable App Passwords in Google account) 
EMAIL_ADDRESS = "delossantos.markbryan@dnsc.edu.ph" 
EMAIL_PASSWORD = "dzvg nhez zisa djtr" 
 
RECIPIENTS = ["valentinlovejoy26@gmail.com"] 
 
QUOTES = [ 
    "  Believe in yourself and all that you are.", 
    "  Push yourself, because no one else is going to do it for you.", 
    "  Success is not for the lazy.", 
    "  Every day is a chance to grow stronger.", 
    "  Don’t limit your challenges. Challenge your limits.", 
    "  Start where you are. Use what you have. Do what you can.", 
    "  Dreams don’t work unless you do.", 
] 
def send_email(subject, message, recipient): 
    msg = MIMEMultipart()     
    msg["From"] = EMAIL_ADDRESS     
    msg["To"] = recipient 



    msg["Subject"] = subject 
 
   
    msg.attach(MIMEText(message, "plain")) 
 
    try:         
        with smtplib.SMTP("smtp.gmail.com", 587) as server:             
            server.starttls() 
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)             
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())             print(f"  Email sent to {recipient}")     except Exception as e:         print(f"  Error: {e}") 
 
def job(): 
    quote = random.choice(QUOTES)     
    print("  Today's Motivation:", quote)     
    for recipient in RECIPIENTS: 
        send_email("  Today's Motivation", quote, recipient) 
 
schedule.every().day.at("13:06").do(job) 
 
print("  Motivational Email Sender started... (CTRL+C to stop)")
while True: 
    schedule.run_pending()    
    time.sleep(60) 
 
