# wsb-oceny
Powiadomienia e-mail oraz Messenger(FB) o nowych ocenach z Extranetu WSB.
Skrypt z założenia powinien być uruchamiany za pomocą crontab, także na serwerach bez interfejsu graficznego.

Obecnie jako *proof-of-concept*.

# Zależności
    apt-get install xvfb
    apt-get install fbchat
    apt-get install firefox-esr
    pip install beautifulsoup4
    pip install -U selenium
    
    gecodriver

<b>Geckodriver:</b><br>
a) pobrać właściwy sterownik https://github.com/mozilla/geckodriver/releases<br>
b) rozpakować<br>
c) skopiować wypakowany sterownik do /usr/bin   (dotyczy Linux)<br>

# Konfiguracja
Plik <b>credent_empty.py</b> należy uzpupełnić danymi do logowania do Extranetu, SMTP i zmienić jego nazwę na <b>credent.py</b>

    'url_oceny': '',
    'wsb_login': '',
    'wsb_password': '',
    'email_from': '',
    'email_to': '',
    'smtp_login': '',
    'smtp_password': '',
    'smtp_host': '',
    'smtp_port': 587,
    'fb_login' : '',
    'fb_password': '',
    'fb_thread_id': ''

# Użycie
python oceny.py
