import os
from . lexer import *
from . parser import *
from . evaluator import *
from . sat import process_ast
from . sat import solver

def display_info():
    print("------------------------------------")
    print("Logik toolkit v0.2")
    print("<https://github.com/64bit-lab/Logik>")
    print("------------------------------------")


def display_help():
    print("-- help ----------------------------")
    print("Memo :")
    print("[ Conjunction ]  a or b")
    print("[ Disjunction ]  a et b")
    print("[ Implication ]  a -> b")
    print("Features :")
    print("[ command - \033[1msolve\033[0m ] input a set of clauses and apply resolution to it")
    print("[ command - \033[1mtree\033[0m  ] input a formula and display its syntax tree")
    print("[ command - \033[1mtable\033[0m ] input a formula and display its truth table (the formula is considered as a function of each free variable)")


def cmd(c):
    if c == "help":
        display_help()
        return
    
    if c in ["quit", "exit"]:
        exit()
        
    if c == "tree":
        form = input('formula >> ')
        pprint(parse(Lexbuf(list(lex(form)))))
        return

    if c == "table":
        form = input('formula >> ')
        evaluate_all(parse(Lexbuf(list(lex(form)))))
        return

    if c == "solve":
        print(" feature not yet implemented ! ")
        return

    if c == "clear":
        os.system("clear")
        return

    if c == "cnf":
        form = input('formula >> ')
        ast = parse(Lexbuf(list(lex(form))))
        ast = process_ast.prepare_for_cnf(ast)
        pprint(ast)
        return

    if c == "clauses":
        form = input('formula >> ')
        ast = parse(Lexbuf(list(lex(form))))
        print(solver.extract_clauses(ast))
        return

    print("\033[1m/!\\\033[0m unknown command '" + c + "'")

