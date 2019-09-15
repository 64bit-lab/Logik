from logik import *
from logik.sat import *
from utils import equivalent


def test_remove_implications():
    # base expression
    expr  = ('->', ('symb', 'a'), ('symb', 'b'))
    # base expression without implications
    exprA = sat.remove_implications(expr)
    # expected result
    exprB = ('ou', ('non', ('symb', 'a')), ('symb', 'b'))

    # chain base expression with an implication
    exprC = sat.remove_implications(('->', expr, expr))
    # expected result
    exprD = ('ou', ('non', exprB), exprB)


    assert equivalent(exprA, exprB), \
        "(a -> b) should be equivalent to (non a ou b)\n"
    assert equivalent(exprC, exprD), \
        "multiple implications shoud be distributed and converted to or expressions\n"


def test_distribute_or():
    # base expression
    exprA = sat.distribute_or(('ou', ('symb', 'a'), ('symb', 'b')))
    # expected result
    exprB = ('ou', ('symb', 'a'), ('symb', 'b'))

    exprC = ('ou', ('et', ('symb', 'a'), ('symb', 'b')), ('symb', 'c'))
    exprD = ('et', 
        ('ou', ('symb', 'a'), ('symb', 'c')),
        ('ou', ('symb', 'b'), ('symb', 'c')))

    exprE = ('ou', ('symb', 'c'), ('et', ('symb', 'a'), ('symb', 'b')))
    exprF = ('et',
        ('ou', ('symb', 'c'), ('symb', 'a')),
        ('ou', ('symb', 'c'), ('symb', 'b')))

    assert equivalent(exprA, exprB), \
        "nothing to distribute in expression (a or b)\n"
    assert equivalent(exprC, exprD), \
        "((a or b) and c) is equivalent to (a or c) and (b or c)\n"
    assert equivalent(exprE, exprF), \
        "(c or (a and b)) is equivalent to (c or a) and (c or b)\n"


def test_remove_negations():
    exprA = sat.remove_negations(('non', ('et', ('symb', 'a'), ('symb', 'b'))))
    exprB = ('ou', ('non', ('symb', 'a')), ('non', ('symb', 'b')))

    exprC = sat.remove_negations(('non', ('ou', ('symb', 'a'), ('symb', 'b'))))
    exprD = sat.remove_negations(('et', ('non', ('symb', 'a')), ('non', ('symb', 'b'))))

    exprE = sat.remove_negations(('non', ('non', ('symb', 'a'))))
    exprF = ('symb', 'a')

    assert equivalent(exprA, exprB), \
        "(non (a et b)) is equivalent to ((non a) ou (non b))\n"
    assert equivalent(exprC, exprD), \
        "(non (a ou b)) is equivalent to ((non a) et (non b))\n"
    assert equivalent(exprE, exprF), \
        "(non (non a)) is equivalent to (a)\n"


def test_prepare_for_cnf():
    return


def test_extract_clauses():
    exprA    = ('ou', ('symb', 'a'), ('symb', 'b'))
    clausesA = sat.solver.extract_clauses(exprA)

    assert clausesA == [[('symb', 'a'), ('symb', 'b')]]


def run():
    print('TEST remove_implications :')
    test_remove_implications()
    print('-> ok')

    print('TEST distribute_implications :')
    test_distribute_or()
    print('-> ok')

    print('TEST remove_negations :')
    test_remove_negations()
    print('-> ok')

    print('TEST extract_clauses :')
    test_extract_clauses()
    print('-> ok')




    