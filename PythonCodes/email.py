import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.login('zoheb.412010.cs@mhssce.ac.in', 'artificiallearning&machineintelligence')
    server.sendmail('zoheb.412010.cs@mhssce.ac.in', to, content)
    server.close()
    print("Email has been sent.")

try:
    content = str(input("Enter text which you want to send: "))
    to = str(input("Please enter the gmail where you want to send the email: "))
    sendEmail(to, content)
except Exception as e:
    print(e)
    print("Sorry Sir, I can't send the email...")

# Read contents of URL

from http.client import HTTPConnection
conn = HTTPConnection("https://www.mhssce.ac.in/")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)