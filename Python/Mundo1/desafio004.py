a = input('Digite algo: ')
alnum = a.isalnum
alpha = a.isalpha
ascii = a.isascii
decimal = a.isdecimal
digit = a.isdigit
identifier = a.isidentifier
lower = a.islower
numeric = a.isnumeric
printable = a.isprintable
space = a.isspace
title = a.istitle
upper = a.isupper
print(f'''O valor é alfanumérico? {alnum}
        O valor é alfabético? {alpha}
        O valor é ascii? {ascii}
        O valor é decimal? {decimal}
        O valor é digito? {digit}
        O valor é identificador? {identifier}
        O valor está em letra cursiva? {lower}
        O valor está em caixa alta? {upper}
        O valor é numérico? {numeric}
        O valor é printável? {printable}
        O valor é um espaço?{space}
        O valor é um título? {title}''')