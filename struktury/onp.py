@@ -1,5 +1,5 @@
def pierwszenstwo(operator):
    if  operator in ['-']:
    if  operator in ['-', '(']:
        return 0
    elif operator in ['+']:
        return 1
@@ -12,10 +12,16 @@ def infiksowa_do_postfiksowej(wejscie):
    stos = []

    for token in wejscie:
        if token in ['+', '-', '*', "/"]:
        if token in ['+', '-', '*', '/']:
            while stos and pierwszenstwo(stos[-1]) >= pierwszenstwo(token):
                wyjscie.append(stos.pop())
            stos.append(token)
        elif token == '(':
            stos.append(token)
        elif token == ')':
            while stos and stos[-1] != '(':
                wyjscie.append(stos.pop())
            stos.pop() # na pewno '('
        else:
            wyjscie.append(token)

@@ -27,6 +33,6 @@ def infiksowa_do_postfiksowej(wejscie):


if __name__ == '__main__':
    wyrazenie = "12 + 1 + a * b"# * ( b * c + d / e )"
    wyrazenie = "12 + 2 * ( 3 * 4 + 10 / 5 )"
    wyrazenie = wyrazenie.split(" ")
    print(" ".join(infiksowa_do_postfiksowej(wyrazenie)))
