
import os

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
    print("""Typing an expression will provide the value of it.
If the expression contains free variables, a Truth table is displayed. 
By default, a syntax tree will be printed too.""")


def cmd(c):
    if c == "help":
        display_help()
        return True
    if c in ["quit", "exit"]:
        exit()

    return False



