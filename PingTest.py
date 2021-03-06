from pythonping import ping
import time
import smtplib, ssl
from socket import gaierror

def main():

    ############################################
    #Open IP address file and separate ip addresses by comma
    camIpDocument = open("CamIpAddresses.txt","r")
    hostsList = str(camIpDocument.read())
    hostsList = hostsList.rstrip()
    #split string into list from commas
    HOSTS = list(hostsList.split(","))
    camIpDocument.close()

    ############################################
    #open cam names document this includes all the hostnames you want to pair with the ip addresses
    nameDocument = open("CamName.txt","r")
    hostsNames = str(nameDocument.read())
    hostsNames = hostsNames.rstrip()
    #split cam names into list
    cameraNames = list(hostsNames.split(","))
    nameDocument.close()
    ############################################
    emailDocument = open("EmailAddresses.txt","r")
    emailNames = str(emailDocument.read())
    emailNames = emailNames.rstrip()
    #split cam names into list
    emailAddressList = list(emailNames.split(","))
    emailDocument.close()
    ############################################

    #send cam names and IP addresses to ping function
    Ping_Test(HOSTS,cameraNames,emailAddressList)
def Ping_Test(hosts,camHostName,recipients):
    #ping every ip address in the CamIpAddresses.txt file
    i = 0
    while i < len(hosts):
        response = ping(hosts[i], verbose=True)
        if 'Request timed out' in str(response):
            #if request times out send email
            Send_Email(hosts[i],camHostName[i],recipients)

        time.sleep(5)
        i+=1
    

def Send_Email(ip,name,receiver):
    #define the SMTP server separately here:
    port = 25 
    smtp_server = "email.server.com"
    login = "user.name" # paste your login
    password = "password" # paste your password 

    # specify the sender’s and receiver’s email addresses
    sender = "user.name@server.com"
    # type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
    SUBJECT = "ALERT! Mach536 Cameras Down!"
    TEXT = f"""\
    
    Ip Address: {ip}
    Camera Name: {name}

    One of the Mach536 Check Fixture Cameras are not connected!"""
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    try:
        #send your message with credentials specified above
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(login, password)
            server.sendmail(sender, receiver, message)

        # tell the script to report if your message was sent or which errors need to be fixed 
        print('Sent')
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))


main()