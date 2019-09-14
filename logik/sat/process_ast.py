"""
Submodules for AST manipulation.
"""


def remove_implications(ast):
    """
    @brief      Removes implications in an AST.
    
    @param      ast   The ast
    
    @return     another AST
    """
    if len(ast) == 3:
        op, oper1, oper2 = ast
        oper1 = remove_implications(oper1)
        oper2 = remove_implications(oper2)
        if op == '->':
            return ('ou', ('non', oper1), oper2)
        else:
            return ast
    return ast


def _is_node_op(ast, op):
    return ast[0] == op

def _is_litteral(ast):
    return ast[0] == 'sym' or ast[0] == 'value'


def distribute_or(ast):
    """
    @brief      Distributes or on and if needed.
    
    @param      ast   The ast
    
    @return     another ast
    """
    
    assert not _is_node_op(ast, '->'), \
        "Or can only be distributed on implication free AST"
    assert ast is not None, "Empty ast"

    if _is_node_op(ast, 'or'):
        _, exprA, exprB = ast
        exprA = distribute_or(exprA)
        exprB = distribute_or(exprB)

        if  _is_node_op(exprB, 'and'):
            _, exprC, exprD = exprB
            exprC = distribute_or(exprC)
            exprD = distribute_or(exprD)

            left  = distribute_or(('or', exprA, exprC))
            right = distribute_or(('or', exprA, exprD))
            return ('and', left, right)

        if _is_node_op(exprA, 'and'):
            _, exprC, exprD = exprA
            exprC = distribute_or(exprC)
            exprD = distribute_or(exprD)

            left  = distribute_or(('or', exprC, exprB))
            right = distribute_or(('or', exprD, exprB))
            return ('and', left, right)

    if len(ast) == 2:
        return ast

    if len(ast) == 3:
        a, b, c = ast
        return (a, distribute_or(b), distribute_or(c))


def remove_negations(ast):
    """
    @brief      Removes all negations.
    
    @param      ast   The ast
    
    @return     another ast
    """

    assert not _is_node_op(ast, '->'), \
        "Negations can only be removed on implication free AST"
    assert ast is not None, "Empty ast"

    if _is_node_op(ast, 'non'):
        _, exprA = ast
        if _is_node_op(exprA, 'or'):
            _, exprB, exprC = exprA
            exprB = remove_negations(('non', exprB))
            exprC = remove_negations(('non', exprC))
            return ('and', exprB, exprC)

        if _is_node_op(exprA, 'and'):
            _, exprB, exprC = exprA
            exprB = remove_negations(('non', exprB))
            exprC = remove_negations(('non', exprC))
            return ('or', exprB, exprC)

        if _is_litteral(exprA):
            return ('non', exprA)

        if _is_node_op(exprA, 'non'):
            _, exprB = exprA
            exprB = remove_negations(exprB)
            return exprB
    
    if len(ast) == 3:
        op, A, B = ast
        A = remove_negations(A)
        B = remove_negations(B)
        return (op, A, B)

    if len(ast) == 2:
        return ast


def prepare_for_cnf(ast):
    """
    @brief      Prepare an ast to be converted in Conjuntive Normal Form.
    
    @param      ast   The ast
    
    @return     another AST ready to be converted in CNF.
    """
    ast = remove_implications(ast)
    ast = remove_negations(ast)
    ast = distribute_or(ast)

    return ast





# print(distribute_or(('or', ('and', ('value', 'a'), ('value', 'b')), ('value', 'c'))))
# print(distribute_or(('or', 
#     ('value', 'a'), 
#     ('or',  ('value', 'b'),
#             ('and', ('value', 'c'), ('value', 'd'))))))

# print(remove_negations(('non', ('and', ('value', 'a'), ('value', 'b')))))
print(remove_negations(('non', ('non', ('non', ('non', ('value', 'b')))))))