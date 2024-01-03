# Biblioteca

Procedimenti da fare per far funzionare il programma.

1) creare la webenv (ambiente virtuale)
2) creare un progetto chiamato Biblioteca (ricordate di attivare prima la webenv)
3) crere dentro al progetto Biblioteca una app 'libri'  --> **python .\manage.py startapp libri**
4) inserire 'libri' nelle installed_apps delle settings.py presente nella cartella Biblioteca
5) copiare dai file che ci sono qua su GitLab solo il database e il file models.py e sostituirli a quelli già presenti se ci sono.
*AVVERTENZE* per sicurezza non copiate direttamente il file models.py ma solo il suo contenuto.
6) eseguire i comandi --> **python .\manage.py makemigrations**  --> **python .\manage.py migrate**
7) creare le credenziali per l'admin con --> **python .\manage.py createsuperuser**
8) runnare il server e vedere se tutto è a posto.
