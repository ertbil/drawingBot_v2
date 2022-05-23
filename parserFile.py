import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER', 'LEFTBRACKET', 'RIGHTBRACKET', 'KIRMIZI', 'YESIL',
    'MAVI', 'SIYAH', 'FORWARD', 'ROTATE', 'LOOP', 'COLOR', 'PEN'
)

t_ignore = r' '
t_FORWARD = r'F'
t_ROTATE = r'R'
t_LOOP = r'L'
t_COLOR = r'COLOR'
t_PEN = r'PEN'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_KIRMIZI = r'K'
t_YESIL = r'Y'
t_MAVI = r'M'
t_SIYAH = r'S'


def t_NUMBER(t):
    r'\d+'  # bu d meselesi şuradan geliyor https://www.w3schools.com/python/python_regex.asp r de regex'in r'si
    t.value = int(t.value)
    return t


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


lexer = lex.lex()

# expression kısmı (yacc)

'''
yazdığım bnf
<forward> =: F <NUM>
<rotate> =: R <NUM>
<COLORINIT> =: COLOR K|Y|M|S
<peninit> =: PEN <NUM>
<init> =: <forward>|<rotate>|<peninit>|<colorinit>|<init><init>
<loop> =: L <NUM> [ <loop>|<init>|<loop><init>|<init><loop> ]

'''


def p_result(p):
    '''
    result : expression
           | empty
    '''
    print(p[1])


def p_expression(p):
    '''
    expression : expression FORWARD NUMBER
         | expression ROTATE NUMBER
         | expression COLOR KIRMIZI
         | expression COLOR YESIL
         | expression COLOR MAVI
         | expression COLOR SIYAH
         | expression PEN NUMBER
    '''
    p[0] = p[1], p[2], p[3]


def p_expression1(p):
    '''
     expression : loop
                | loop_with_loop
                | empty

    '''
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    pass


def p_loop(p):
    '''
    loop : LOOP NUMBER LEFTBRACKET expression RIGHTBRACKET
         | LOOP NUMBER LEFTBRACKET loop RIGHTBRACKET
         | empty
    '''
    p[0] = p[4], p[3], p[1], p[2],


def p_loop_with_loop(p):
    '''
    loop_with_loop : LOOP NUMBER LEFTBRACKET loop expression RIGHTBRACKET
    '''
    p[0] = p[5], p[4], p[1], p[2], p[3]


isSyntaxError = False


def p_error(p):
    global isSyntaxError
    if p:
        print("Syntax error")
    else:
        isSyntaxError = True
        print("Syntax error at EOF")


def crateTokenList():
    tokenList = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokenList.append(token.value)
    return tokenList


def parseIt(data):
    a = lexer.input(data)

    parser = yacc.yacc()

    result = parser.parse(a)
    if not isSyntaxError:
        a = lexer.input(data)
        tokenList = crateTokenList()

    return tokenList
