from logik import parser
from logik import lexer

from logik.parser import parse
from logik.parser import Lexbuf
from logik.lexer  import lex

def test_parse():

    outputA     = parse(Lexbuf(list(lex("a et b"))))
    expectedA   = ('et', ('symb', 'a'), ('symb', 'b'))

    outputB     = parse(Lexbuf(list(lex("a ou b"))))
    expectedB   = ('ou', ('symb', 'a'), ('symb', 'b'))

    outputC     = parse(Lexbuf(list(lex("a -> b"))))
    expectedC   = ('->', ('symb', 'a'), ('symb', 'b'))

    outputD     = parse(Lexbuf(list(lex("((a et b))"))))
    expectedD   = ('et', ('symb', 'a'), ('symb', 'b'))

    outputE     = parse(Lexbuf(list(lex("non a"))))
    expectedE   = ('non', ('symb', 'a'))

    outputF     = parse(Lexbuf(list(lex("a -> non (b ou c)"))))
    expectedF   = ('->', ('symb', 'a'), ('non', ('ou', ('symb', 'b'), ('symb', 'c'))))

    outputG     = parse(Lexbuf(list(lex("a et b ou c"))))
    expectedG   = ('ou', ('et', ('symb', 'a'), ('symb', 'b')), ('symb', 'c'))

    assert outputA == expectedA, \
        "simple AND expressions should be parsed correctly"
    assert outputC == expectedC, \
        "simple OR expressions should be parsed correctly"
    assert outputC == expectedC, \
        "simple IMPILCATIONS expressions should be parsed correctly"
    assert outputD == expectedD, \
        "over parenthesized expressions should be parsed correctly"
    assert outputE == expectedE, \
        "simple NEGATIONS expressions should be parsed correctly"
    assert outputF == expectedF, \
        "chained expressions should be parsed correctly"
    assert outputG == expectedG, \
        "chained AND, OR expressions should be parsed with correct precedence"


def run():
    print("TEST parse ...")
    test_parse()
    print('-> ok')
