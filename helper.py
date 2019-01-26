
import smtplib

from email.message import EmailMessage

from credent import secret



tb_headers=["id","przedmiot","wykladowca","forma_zaliczenia","rodz_zajec","ocena1","data1","ocena2","data2"]

def sendEmail(subject,eml_from,eml_to,message):

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = eml_from
    msg['To'] = eml_to

    # Send the message via SMTP server.
    print("SENDING INFO EMAIL...")
    try:
        server = smtplib.SMTP(secret["smtp_host"], secret["smtp_port"])
        server.ehlo()
        server.login(secret["smtp_login"], secret["smtp_password"])
        server.send_message(msg)
        server.quit()
        print("SENDING OK!")
    except:
        #raise
        print("...sending email: somethin went wrong:(")


def preetyGrade(grade):
    if grade=="-":
        return "brak"
    else:
        return str(grade)


def compareT(T1,T2):  #T1,T2 krotka z wierszem z bazy danych (wiersz tabeli z ocenami starymi/nowymi)
    lenT1 = len(T1)
    lenT2 = len(T2)

    if lenT1!=9 and lenT2!=9:
        return {"private":"Błąd E1. Nieodpowiednia ilość kolumn. Być może zmeniła się struktura strony źródłowej ?!","public":""}

    if lenT2 > lenT1 and lenT1==0:
        return {"private":"Dopisano nowy przedmiot: "+T2[1],"public":""}

    if lenT1 == lenT2 and lenT1 == 9:
        zm=""
        L = len(T1)
        for i in range(0,L):
            if(T1[i]!=T2[i]):
                zm = zm +"\r\nZmiana "+tb_headers[i]+" z "+preetyGrade(T1[i])+" na "+preetyGrade(T2[i])+", "
        if len(zm)>1:
            zm = zm[:-2]
        return {"private":"Przedmiot: "+T1[1]+" ("+T1[3]+", "+T1[2]+")"+zm, "public":"Możliwa nowe oceny z przedmiotu: "+T1[1]+" ("+T1[3]+", "+T1[2]+") [powiadomienie automatyczne, grupa WZ_INiN3_PG2]"}

    return {"private":"Nieokreślony błąd. Być moze załadowane zostały przedmioty z nowego semestru lub zmeniła się struktura strony źródłowej ?!","public":""}
