
def remove_implications(ast):
    """
    @brief      Removes implications in an AST.
    
    @param      ast   The ast
    
    @return     another AST
    """
    if len(ast) == 3:
        op, oper1, oper2 = ast
        if op == '->':
            oper1 = remove_implications(oper1)
            oper2 = remove_implications(oper2)
            return ('ou', ('non', oper1), oper2)
        else:
            return ast
    return ast


def remove_and(ast):
    if len(ast) == 3:
        op, oper1, oper2 = ast
        oper1 = remove_and(oper1)
        oper2 = remove_and(oper2)
        if op == 'et':
            oper1 = distribute(oper1)
            oper2 = distribute(oper2)