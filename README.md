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



QUI Jude sono le 5:48 di mattina io sono riuscito a fare l'authentication ma solo per gli admin quindi ho implementato anche una lista che visualizza tutti i libri
ora bisogna solo capire come fare le query, come creare dei nuovi oggetti libri nel database ho più o meno capito cercherò di implementare quello domani.
Finora non ho visto niente sul come eliminare roba.
Manca l'authentication per la gente normale per fare i prestiti e https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html 
(credo che questo tutorial sia fatto apposta).
Dovete installare pylint e modificare le preferences di vscode per python se no non funziona Libri.objects.all()
Ho messo il logo dello Zuccante ma secondo me fa schifo troppo grosso 
bootstrap non è poi così male.
Cose da cambiare:
1)togliere il signup come admin perchè se no non ha senso 
2)boh

non vi ho messo il mio database perchè ho inserito un po' di prove di libri chiamati Jude il magnifico solo che quando facevo il submit mi dava errore nel reverse url
che è una cosa che non ho ancora capito

Un'altra cosa è capire come fare più pagine perchè al momento la lista dei libri è tutta su una pagina
Se non mi sveglio e non vi funziona mentite al prof, mentite spudoratamente, dite che siamo a buon punto. 
IO CAPPELLAZZO LO SALTO(forse non lo so,boh,probabile che salto anche info)
PAVAN M***A