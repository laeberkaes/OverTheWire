---
title: CTF Writeup
subtitle: Krypton
---

# Level1
Entschlüsseln von ROT13 mit `echo 'cipher' | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
ROT13 ist eine Sonderform des Ceasarchiffre. Der Buchstabe wird durch den 13 Stellen weiter ersetzt. Dadurch kann mit der selben Funktion der Text chiffriert und das Chiffre entschlüsselt werden.

PW == LEVEL TWO PASSWORD ROTTEN


# Level2
Der Anleitung in README folgen. Man findet heraus, dass die encrypt Datei den Text um 12 Stellen nach hhinten verschiebt. Mit dem Verschlüsselungsskript für Caesarchiffren kann man den Text entschlüsseln.

PW == CAESARISEASY


# Level3

