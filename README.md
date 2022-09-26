# Biblioteca

Non siate pigri, i procedimenti da fare per farvi funzionare il programma.

1) creare la webenv (ambiente virtuale)
2) creare un progetto chiamato Biblioteca (ricordate di attivare prima la webenv)
3) crere dentro al progetto Biblioteca una app 'libri'  --> **python .\manage.py startapp libri**
4) inserire 'libri' nelle installed_apps delle settings.py presente nella cartella Biblioteca
5) copiare dai file che ci sono qua su GitLab solo il database e il file models.py e sostituirli a quelli già presenti se ci sono.
*AVVERTENZE* per sicurezza non copiate direttamente il file models.py ma solo il suo contenuto.
6) eseguire i comandi --> **python .\manage.py makemigrations**  --> **python .\manage.py migrate**
7) creare le credenziali per l'admin con --> **python .\manage.py createsuperuser**
8) runnare il server e vedere se tutto è a posto.

Fatti sti passaggi la prima volta avrete il vostro progetto e ogni volta che qualcuno di noi condividerà del materiale basterà sostituire soltanto
i file cambiati.

#############################################################################################################################################

Procedimento da fare per poter usare il progetto pubblicato da Jude (pufu22).

1) entrare nella webenv (ambiente virtuale)
2) fare il comando --> **pip install django-crispy-forms**
3) copiare il contenuto dei seguenti file: 
    *  In Biblioteca copiare il contenuto di settings.py - urls.py     -       e copiare l'intera cartella templates/
    *  In libri copiare il contenuto di views.py - models.py
4) runnare il server e vedere se tutto è a posto.
