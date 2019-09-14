from . lexer import *


def priority(operator):
    """
    @brief      Return operator priority
    
    @param      operator  The operator
    
    @return     the priority
    """
    if operator == "non":
        return 5
    if operator == "et":
        return 4
    if operator == "ou":
        return 3
    if operator == "->":
        return 1


class Lexbuf:
    """
    @brief      Lexbuf class for token analysis.
    """
    def __init__(self, string):
        self.str = string
        self.index = -1

    def next_char(self):
        self.index += 1
        if self.index < len(self.str):
            return self.str[self.index]
        return None

    def see_next(self):
        if self.index+1 < len(self.str):
            return self.str[self.index+1]
        return None


def parse(lexbuf, end=None):

    expr = [] # expression stack
    oper = [] # operator stack

    # read the current token
    c = lexbuf.next_char()

    while c not in (end, (end, '')):

        if c[0] == 'symb':
            # token c is a symbol
            expr.append(('symb', c[1]))

        elif c[0] == 'value':
            expr.append(('value', int(c[1])))

        elif c[0] == "(":
            # token c is '(', parse until token ')'
            expr.append(parse(Lexbuf, ")"))

        elif c[0] == 'binop':
            # token c is an operator
            if len(oper) > 0:
                t = oper[-1]
                while len(oper) > 0 and priority(t) >= priority(c[1]):
                    op = oper.pop()  # binary operator
                    op2 = expr.pop() # operand 1
                    op1 = expr.pop() # operand 2
                    expr.append((op, op1, op2))
            # add operator c to the stack
            oper.append(c[1])

        elif c[0] == 'unop':
            # token c is the unary operator
            if lexbuf.see_next() is None:
                # syntax error
                raise Exception("'non' token must be followed \
                    by an expression or a symbol")
            elif lexbuf.see_next()[0] == "(":
                # apply the operator to the next expression
                lexbuf.next_char()
                e = parse(Lexbuf, ')')
                expr.append(('non', e))
            elif lexbuf.see_next()[0] == "symb" or Lexbuf.see_next()[0] == 'value':
                # apply the operator to the next symbol
                e = lexbuf.next_char()
                expr.append(('non', e))

        # move to then next token
        c = lexbuf.next_char()

    # fill the AST
    while len(oper) != 0:
        op = oper.pop()
        op2 = expr.pop()
        op1 = expr.pop()
        expr.append((op, op1, op2))

    # return the AST
    return expr.pop()


def pprint(ast):
    """
    @brief      Pretty print an AST
    
    @param      ast   The ast
    """
    def red(string):
        # format a string to be printed in red
        return '\033[31m' + string + '\033[0m'

    def print_rec(ast, i):
        # recursively print the AST
        if ast[0] == "symb" or ast[0] == 'value':
            print("  "*i + str(ast[1]))
        elif ast[0] == "non":
            print("  "*i + red(ast[0]))
            print_rec(ast[1], i+1)
        else:
            print("  "*i + red(ast[0]))
            print_rec(ast[1], i+1)
            print_rec(ast[2], i+1)

    print_rec(ast, 0)


if __name__ == '__main__':
    # input
    string = input('>>> ')
    # lexing
    tokens = lex(string)
    # parsing
    Lexbuf = Lexbuf(list(tokens))
    # display the AST
    # pprint(parse(Lexbuf))
    print(parse(Lexbuf))
