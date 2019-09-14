"""
Submodule implenting a solver based on the resolution algorithm.
"""

from . process_ast import *

def extract_clauses(ast):
    
    if ast[0] == 'symbol':
        return [ast]

    if _is_node_op(ast, 'non'):
        return [ast]

    if _is_node_op(ast, 'or'):
        clause = []
        clause += extract_clauses(ast[1])
        clause += extract_clauses(ast[2])
        return [clause]

    if _is_node_op(ast, 'and'):
        clauses = []
        clauses += extract_clauses(ast[1])
        clauses += extract_clauses(ast[2])
        return clauses

    else:
        raise Exception('Bound variable error')



