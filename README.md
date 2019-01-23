# wsb-oceny
Powiadomienia e-mail o nowych ocenach z Extranetu WSB.
Skrypt z założenia powinien być uruchamiany za pomocą crontab, także na serwerach bez interfejsu graficznego.

Obecnie jako *proof-of-concept*.

# Zależności
	apt-get install firefox-esr
	pip3 install beautifulsoup4
	pip3 install -U selenium
	gecodriver

<b>Geckodriver:</b>
a) pobrać właściwy sterownik https://github.com/mozilla/geckodriver/releases
b) rozpakować
c) skopiować wypakowany sterownik do /usr/local/bin   (dotyczy Linux)

# Konfiguracja
Plik <b>credent_empty.py</b> należy uzpupełnić danymi do logowania do Extranetu, SMTP i zmienić jego nazwę na <b>credent.py</b>

    'url_oceny' 	: '',
    'wsb_login' 	: '',
    'wsb_password' 	: '',
    'email_from'	: '',
    'email_to'		: '',
    'smtp_login'	: '',
    'smtp_password'	: '',
    'smtp_host'		: '',
    'smtp_port'		: 587

# Użycie
python oceny.py
