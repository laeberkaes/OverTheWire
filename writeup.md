OverTheWire Writeups:

---
Level 0

flag = boJ9jbbUNNfktd78OOpsqOltutMc3MY1


---
Level 1

flag = CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


---
Level 2

flag = UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK


---
Level 3

flag = pIwrPrtPN36QITSp3EQaw936yaFoFgAB


---
Level 4

flag = koReBOKuIDDepwhWk7jZC0RTdopnAYKh


---
Level 5

flag = DXjZPULLxYr17uwoI01bNLQbtFemEgo7


---
Level 6

Command find >> mit -size >bytegröße<c -user >USER< -group >GROUP< kann man nach Besitz und Größe suchen

flag = HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs4


---
Level 7

flag = cvX2JJa4CFALtqS87jk27qwqGhBM9plV


---
Level 8

mit sort kann man die Strings sortieren - sodass immer die gleichen gruppiert sind. Dann piped man sie zu uniq -u sodass der String ausgegeben wird, der nur einmal vorkommt.
Man muss sort davor verwenden, weil uniq -u nur nachfolgende Strings betrachtet - kann also nicht sage, ob ein String schon an einer ganz anderen Stelle schonmal vorgekommen ist.

flag = UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR


---
Level 9

mit grep einfach die '=' suchen.

flag = truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk


---
Level 10

der Text ist mit base64 encoded - zum decoden: base64 -d data.txt

flag = IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR


---
Level 11

der Text ist mit ROT13 codiert - um zu decoden einfach tr (translate) verwenden: tr 'A-Za-z' 'N-ZA-Mn-za-m' dadurch, werden jeweils die einzelnen Zeichen (egal ob groß oder klein geschrieben >> deshalb der erste Part 'A-Za-z' - um 13 Stellen verrückt - das würde dann dem nächsten Part entsprechen 'N-ZA-Mn-za-m').

flag = 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu


---
Level 12

Ich habe keine fucking Ahnung...

Ist ein hexdump -- wenn man ihn mit xxd zurück in eine Binärdatei konvertiert, gibt file zurück, dass es sich um eine gzip Datei handelt. Dann mit gunzip entpacken. Liefert eine bzip2 Datei. Auch diese wird umbenannt und entpackt. Dann kommt ein POSIX TAR Archiv. Dieses wird mit tar -xf >file< entpackt. Dies wiederholt man nocheinmal. Dann kommt eine bzip2 Datei. Woraus wieder eine POSIX TAR Datei kommt. Darauf eine gzip Datei und schließlich ist es wieder ein ASCII Text.

flag = 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL


---
Level 13

Gegeben ist ein Private Key RSA für SSH. Auch gegeben ist, dass die flag im Verzeichnis /etc/bandit_pass/bandit14 liegt und nur vom user bandit14 gelesen werden kann.
Versuchen mit dem privateKey per ssh anzumelden.

	ssh -i >filename< bandit14@host -p 2220 >> hat nicht funktioniert!
	Lösung war, dass man statt des Hostnamen von extern localhost nimmt:

		ssh -i >file< bandit14@localhost

flag = wurde mit privatekey gelöst - das PW kann aber aus /etc/bandit_pass/bandit14 ausgelesen werden = 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e


---
Level 14

Gegeben ist eine authorized_keys Datei. file gibt
Password kann aus /etc/bandit_pass/bandit14 ausgelesen werden = 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

Man konnte sich per telnet localhost 30000 verbinden. Das Passwort war korrekt. Dann bekommt man das nächste Password

flag = BfMYroe26WYalil77FoDi9qh59eK5xNr


---
Level 15

man muss sich per SSL mit dem Service auf Port localhost:30001 verbinden.

openssl s_client -connect localhost:30001

dann muss man ein Password eingeben. Das Password ist das von Level 14.

flag = cluFn7wTiGryunymYOu4RcffSxQluehd


---
Level 16

In der range von Port 31000 bis 32000 sollen zwei Server sein. Einer davon verwendet SSL. Man muss ihn finden.

Einer der Server gibt das zurück, was man ihm schickt - shell script attack??
Der andere gibt einen RSA Key zurück, wenn man ihm das aktuelle Passwort übergibt.

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

dieser Key wird in einer Datei gespeichert - Name ist nicht relevant - habe sie einfach sshkey.private genannt.
Man muss noch die Berechtigungen ändern chmod 600 >file<, damit niemand außer dem Besitzer die Datei verändern kann - ansonsten wird es vom SSH nicht genommen.

Dann ssh -i >file< bandit17@loaclhost.


---
Level 17

es sind zwei Dateien gegeben:

	passwords.old und passwords.new

gegeben ist, dass die nächste flag die einzige Zeile ist, die sich in den beiden Dateien geändert hat.

	diff passwords.old passwords.new

gibt genau eine Zeile aus.

flag = kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd


---
Level 18

Die flag ist in der Datei >readme< in der home directory.
Per SSH kann man sich nicht verbinden, weil man direkt wieder ausgeloggt wird.
Per SSH kann man aber Befehle ausführen, auch wenn man nicht in die Shell kommt

	ssh bandit18@localhost cat readme

flag = IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x


---
Level 19

Mit der Datei bandit20-do kann man mit anderen Privilegien Befehle ausführen.

ls -al gibt statt dem x ein s zurück - so kann man setuid files erkennen.

mit ./bandit20-do whoami kann man sehen, welche userrechte man jetzt hat. Dann kann man das Passwort von Bandit20 einfach auslesen - ./bandit20-do cat /etc/bandit_pass/bandit20

flag = GbKksEFF4yrVs6il55v6gwY5aVje5f0j


---
Level 20

Es ist gegeben, dass des setuid Programm ./suconnect [PORT] sich mit einem Port verbindet. Dort dann eine Zeile liest und diese mit dem aktuellen Passwort vergleicht. Wenn diese übereinstimmen, dann wird das nächste Password ausgegeben.

Dazu nimmt man netcat:

	nc -l -p [PORT] localhost >> damit erzeugt man einen Prozess (-l = listender), mit welchem man in ein anderes Terminal "kommunizieren" kann.

	nc localhost [PORT] ist dann das zweite Terminal

nun kann man als zweites Terminal auch ./suconnect verwenden und durch das erste Terminal dann das aktelle Password ausgeben lassen!!

flag =  gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr


---
Level 21

Gegeben ist, dass ein Programm in regelmäßigen Abständen ausgeführt wird. Dieses Programm liegt in der directory - /etc/cron.d/

Darin waren 3 Dateien abgelegt.
Diese verwiesen wiederum auf drei bash Skripte in /usr/bin/cronjob_bandit22(23,24).
Und diese wiederum speichern das Passwort des jewiligen Bandits im Ordner /tmp/ in einer bestimmten directory ab.

flag1 = Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI


---
Level 22

Wie oben wird jetzt auf das zweite Bash Skript eingegangen.
Diese kopiert das Passwort des aktuellen Nutzers in eine gegebene Directory.

Wenn man sich da Bash Skript anschaut, welches ausgeführt wird, sieht man, dass die Datei, in welcher das Passwort gespeichert wird, aus dem MD5 Hash des Nutzernames benannt wird.

So kann man dann die Datei herausfinden, in welcher das Passwort für den User Bandit23 gespeichert wird.

	echo I am user bandit23 | md5sum | cut -d ' ' -f 1

flag = jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n


---
Level 23

Auch hier geht man wieder in /etc/cron.d/ und schaut sich den Code von cronjob_bandit24 an. Dieser führt das dort angegebene Skript aus, welches immer alle Dateien in dem Verzeichnis /var/spool/bandit24 ausführt und anschließend löscht.

Wenn man sich weiter umschaut ist in dem Verzeichnis /var/spool/bandit24 ein test Ordner, in welchem sich ein bash skript befindet. In diesem ist das Password im Klartext gespeichert.

flag = UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

---
Level 24

Man muss ein Skript schreiben, welches dem Daemon auf Port 30002 das aktuelle Passwort und eine 4 stellige Zahl von 0-9999 mit einem Leerzeichen getrennt übergibt. Bei der richtigen Kombination antwortet dieser mit dem Passwort des Bandit 25.

	import socket

	password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
	pin = 0

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', int(30002)))
	s.recv(4096)
	while True:
	    print("[+] Sending PIN " + str(pin))
	    content = password + " " + str(pin)
	    s.sendall(content.encode())
	    data = s.recv(4096)
	    print(repr(data))
	    pin = pin + 1
	s.close()

Dann muss man nur noch warten, bis alle kombinationen durchprobiert wurden. Das dauert sehr lange :D

Wenn man das Programm in mehreren Terminals laufen lässt geht es dann auch schneller.

flag = uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG


---
Level 25

Hier wird angegeben, dass bandit26 nicht die normale bash Shell verwendet. Im home Verzeichnis von bandit24 sieht man einen sshkey. Man kann sich damit auch mit ssh bandit26@localhost -i file verbinden, jedoch wird die Verbindung sofort unterbrochen.
Man kann in /etc/passwd alle vorhandenen Nutzer und deren verwendete Shell anschauen. Dort ist eine text Datei angegeben als Shell. Wenn man diese mit cat aufruft, sieht man folgendes:

	#!/bin/sh

	export TERM=linux

	more ~/text.txt
	exit 0

Wenn man jetzt das Terminal so klein macht, dass die Textdatei nicht ganz angezeigt werden kann -- bei der SSH Verbindung, dann wird die Verbindung nicht sofort beendet. Nun öffnet man mit 'v' den vim Editor. Dort gibt man dann :set shell=/bin/bash ein, damit die bash Shell verwendet wird. Dann :sh damit ruft man die Shell auf. Schon ist man angemeldet.

flag = 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z


---
Level 27

Hier werden uns keine Tipps gegeben. Mit ls -l sieht man eine ausführbare Datei mit s anstatt x -- wir erinnern uns -- damit kann man Befehle als anderer User ausführen.

also ./bandit27-do whoami == bandit17
Wir sind damit also bandit27

Mit ./bandit27-do cat /etc/bandit-pass/bandit27 bekommt man dann die flag.

flag = 3ba3118a22e93127a4ed485be72ef5ea


---
Level 28

so hier ist gegeben, dass es ein git repository gibt. Man kann aber nur im tmp Ordner schreiben. Also einen neuen Ordner machen und mit git clone ssh://bandit27-git@localhost/home/bandit27-git/repo alles herunterladen.
Man bekommt einen Ordner mit einer README Datei. Darin steht das neue Passwort.

flag = 0ef186ac70e04ea33b4c1853d2526fa2

28 --> 29
man muss wieder die angegebene git repo clonen. Darin befindet sich eine Datei. Dort ist das Passwort jedoch unkenntlich gemacht.
Wenn man sich in dem heruntergeladenen Ordner repo befindet, kann man mit `git log -p`  kann man jedoch vorher commitete Versionen der repo sehen. Und dort ist dann auch das Passwort zu sehen.

flag = bbc96594b4e001778eee9975372716b2


---
Level 29

Wieder eine repo. Dort sieht man kein Passwort. Mit `git log -p` sieht man hier, dass bandit30 in bandit29 geändert wurde? Mit `git branch` sieht man dann in welchen branch man sich befindet. Wir sind im Master. Vielleicht gibt es ja andere branches, in welchem das Passwort schon eingefügt wurde. Mit `git show-branch -- all` sieht man alle branches. 

Dann mit `git remote show` --> origin `git remote show origin` -->  `git checkout dev` in den dev branch wechsel und schon sieht man auch das Passwort.

flag = 5b90576bedb2cc04c86a9e924ce42faf


---
Level 30

Die nächste repo enthält eine Datei. `+just an epmty file... muahaha`
Mehr bekommt man mit `git show` auch nicht. Dann aber mit `git tag` findet man einen tag `secret`.
Dann mit `git show secret` findet man dann das Passwort.

flag = 47e603bb428404d265f59c42920d81e5


---
Level 31

Hier muss dann eine Datei `key.txt` erstellt werden mit dem Text `May I come in?`. Diese muss man dann in die master branch pushen.
Das macht mann dann mit `git add -f key.txt` --> `git commit -m "."` --> `git push` 
Dann erhält man auch das Passwort.

flag = 56a9bf19c63d650ce78e6ec0354ee45e


---
Level 32

Hier kommt man in eine Shell, die nicht viele Befehle kennt. Mit `$0` wechselt man in die normale bash shell.
Dann mit `cat /etc/bandit_pass/bandit33` einfach das Passwort abfragen.

flag = c9c3199ddf4121b10cf581a98d51caee


---
Level 33

kein weitere Level bis jetzt.