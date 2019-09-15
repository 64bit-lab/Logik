"""
Submodule implenting a solver based on the resolution algorithm.
"""

from . process_ast import *

def extract_clauses(ast):
    
    if ast[0] == 'symb':
        return [ast]

    if is_node_op(ast, 'non'):
        return [ast]

    if is_node_op(ast, 'ou'):
        clause = []
        clause += extract_clauses(ast[1])
        clause += extract_clauses(ast[2])
        return [clause]

    if is_node_op(ast, 'et'):
        clauses = []
        clauses += extract_clauses(ast[1])
        clauses += extract_clauses(ast[2])
        return clauses

    else:
        print(ast)
        raise Exception('Bound variable error')



