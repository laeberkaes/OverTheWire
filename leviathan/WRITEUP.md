# WRITEUP

## Level 1
In der home directory befindet sich ein Ordner `.backup` -- in diesem befindet sich eine .html Datei mit verschiedenen Lesezeichen. `cat bookmarks.html | grep leviathan` does the trick.

```
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A
```
pwd == rioGegei8m


---
## Level 2
Die ausführbare Datei `check` befindet sich im Ordner.
Dank hilfe komme ich auf die Lösung. Mit `ltrace` und `strace` kann man herausfinden, was die Datei macht. In `ltrace` sieht man, dass das eingegebene Passwort mit dem Wort sex verglichen wird. 

```
__libc_start_main(0x804853b, 1, 0xffffd784, 0x8048610 <unfinished ...>
printf("password: ")                                           = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: test
)                          = 116
getchar(1, 0, 0x65766f6c, 0x646f6700)                          = 101
getchar(1, 0, 0x65766f6c, 0x646f6700)                          = 115
strcmp("tes", "sex")                                           = 1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                           = 29
+++ exited (status 0) +++
```

Nun versuchen wir als Passwort sex einzugeben. Das funktioniert und wir bekommen eine neue Shell des Benutzers leviathan2! Dann nur noch das Passwort in `/etc/leviathan_pass/leviathan2` auslesen.

pwd == ougahZi8Ta


---
## Level 3
Man hat eine `printfile` Datei, welcher man eine Datei übergeben muss, welche dann mit `cat` ausgegeben wird.
Wichtig ist hier zu verstehen, wie der `cat` Befehl funktioniert und wie Befehle mit einander verkettet werden können. Bspw. kann man einen weiteren Befehl ausführen, wenn man an den letzten ein Semicolon anhängt --> `cat this; bash` Hier wird nach der Ausführung des cat noch eine Shell eröffnet.
Somit kann eine Shell des Nutzers Leviathan3 eröffnet werden, indem eine Datei erstellt `toch "a;bash"`. Diese Datei wird dann mit dem `printfile` Befehl aufgerufen `/home/leviathan2/printfile "a:bash"` und man gelangt in eine Shell des Nutzers Leviathan3. Dann nur noch die Passwort Datei auslesen.

pwd == Ahdiemoo1j


---
## Level 4
Ich kann nur raten, wie ich es geschafft habe, aber man bekommt eine `level3` Datei. Wenn man diese ausführt wird man nach einem Passwort gefragt. Mit `ltrace` sieht man zu Beginn einen `strcmp()` mit h0no33 und kakaka und nach der Eingabe des Passworts noch die selbe Funktion mit snlprintf.
Wenn man bei `ltrace` das Passwort `snlprintf` eingibt, kommt man in eine Shell von leviathan3. Wenn man nur level3 ausführt und dann das Passwort eingibt in eine Shell von leviathan4. Dann noch die Passwortdatei auslesen.

pwd == vuH0coox6m


---
## Level 5
Es gibt einen Ordner `.trash`. In diesem findet sich eine `bin` Datei. Wenn diese ausgeführt wird, gibt sie binär Zahlen zurück.

```
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 
```

Diese ergeben wohl auch das nächste Passwort.

pwd == Tith4cokei


---
## Level 6
Eine `leviathan5` Datei. Beim Ausführen `Cannot find /tmp/file.log`. Also sucht das Programm nach genannter Datei, welche nicht vorhanden ist. Man kann sie erstellen mit einem Text -- dieser Text wird dann ausgegeben (mit cat). Wenn man jetzt einen symbolischen Link mit `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log` erstellt, wird die Passwortdatei ausgegeben.

pwd == UgaoFee4li


---
## Level 7
Es gibt eine `leviathan6` Datei. Bei Ausführung muss man einen 4 stelligen Code eingbenen.
Mit dem folgenden kleinen Skript kann man den Code Brute Forcen.

```
#!/bin/bash             
    
for i in seq $(0000 9999)
do  
    /home/leviathan6/leviathan6 $i
done
```

Bei korrektem Code gelangt man dann in eine Shell von leviathan7.

pwd == ahy7MaeBo9

---
-- und das wars --