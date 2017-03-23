
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("navaneethmalingan@gmail.com", "navaneeth@spatika16")
msg = "This is a simple email test!"
server.sendmail("navaneethmalingan@gmail.com", "shrihari.8788@gmail.com", msg)
server.quit()
