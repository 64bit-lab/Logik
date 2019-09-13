from . evaluator import *
from . utils import *
"""
Module : Logik

Description :

Logik provide a simple way to manipulate propositionnal logic in python !

Author : Arthur Correnson
Email  : arthur.correnson@gmail.com

-------------------------------------------------------------------------------

This software may be freely distributed under the MIT license :


MIT License

Copyright (c) 2019 Arthur Correnson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Main function
def main():
    display_info()
    while True:
        # input
        string = input('>> ')
        if not cmd(string):
            # lexing
            tokens = lex(string)
            # parsing
            seq = Seq(list(tokens))
            ast = parse(seq)
            # display the AST
            print('\nSyntax tree :\n')
            pprint(ast)
            evaluate_all(ast)