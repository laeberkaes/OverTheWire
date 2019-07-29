# Writeup -- Natas Wargame

## natas0

pw == natas0


---
## natas1

Passwort ist auf der Seite versteckt -- Inspect Element

pw == gtVrDuiDfck831PqWsLEZy5gyDz1clto


---
## natas2

Rechtsklick deaktiviert -- dann eben mit Shortcut (außerdem war bei mir der Rechtsklick nicht mal deaktiviert)

pw == ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi


---
## natas3

Nichts auf dieser Seite?? Im Code ist die Referenz auf ein "Bild" ./files/pixel.jpg

Ist tatsächlich nur ein Pixel -- aber was ist denn in dem übergeordneten Ordner?

`users.txt`

Darin sind mehrere Benutzer aufgeführt -- auch natas3

pw == sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14


---
## natas4

Wieder nichts?? Nichtmal Google soll es finden?

Mal in die `robots.txt` schauen.

```
User-agent: *
Disallow: /s3cr3t/
```

Na dann schauen wir mal in den Ordner rein. Und wieder eine `users.txt`. Mit dem Nutzer `natas4`

pw == Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ


---
## natas5

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/" 

mhh .. also muss ich irgendwie von einer anderen Seite auf diese Seite zugreifen? Sollte mit einem Proxy gehen.

Einfach mit der burp suite einen Proxy auf machen. Dann die Anfrage beim erneuern der Seite abfangen. Bei headers den referer auf natas5.--- ändern. Dann weiterleiten und man hat es.

pw == iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq 


---
## natas6

Wie oben, nur wissen wir nicht, warum wir keinen Zugang haben. Hier geht es um Cookies. Im loggedin Cookie den Wert auf 1 == true setzen. Dann neu laden und fertig.

pwd == aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1


---
## natas7

So hier bekommen wir ein php Skript und müssen ein secret eingeben.

Das ist der php code:
```
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas6", "pass": "<censored>" };</script></head>
<body>
<h1>natas6</h1>
<div id="content">

<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Wir suchen also das Pondant zu $secrets. Ganz oben sehen wir, dass eine Datei eingebunden wird, die sich in `./includes/secret.inc` befindet.

Erstmal sieht man auf der Seite nichts. Aber wenn man den Quellcode anschaut, sieht man das secret.

`FOEIUWGHFEEUHOFUOIU`

Das gibt man dann ein und schon bekommt man das Passwort.

pwd == 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9


---
## natas8

Hier sind zwei Seiten verlinkt. Home und About. Im Quelltext steht dann der Hinweis, dass das Passwort im Verzeichnis `/etc/natas_webpass/natas8` ist.

Wie komme ich jetzt dahin? Wenn wir auf die verschiedenen Links klicken, kann man sehen, wie auf der Seite andere Seiten aufgerufen werden (in der URL). Man sieht nach dem `?` den Aufruf `page=`. Dahinter werden dann die Verzeichnisse aufgerufen, in welchen die Seiten liegen. Dort gibt man dann den oben angegebenen Pfad ein. Schon  bekommt man das Passwort.

pwd == DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 


---
## natas9

Okay wieder ein `secret` das eingegeben werden muss.

Der Quellcode:

```
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas8", "pass": "<censored>" };</script></head>
<body>
<h1>natas8</h1>
<div id="content">

<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Hier geht es darum verschiedene Codierungen zu verschachteln. Einfach ein kurzes Skript schreiben:

```
import base64

def natas9decoder(secret):
    var = bytes.fromhex(secret).decode('utf-8')
    var = str(var)[::-1]
    var = base64.b64decode(var)
    print(var)

natas9decoder('3d3d516343746d4d6d6c315669563362')
```

Man bekommt dann das `secret`:

`oubWYf2kBq`

Das übergibt man dann und schon bekommt man das nächste Passwort.

pwd == W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl


---
## natas10

Ich denke hier geht es um SQL injection.
Hier der Quellcode:

```
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas9", "pass": "<censored>" };</script></head>
<body>
<h1>natas9</h1>
<div id="content">
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>


Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

