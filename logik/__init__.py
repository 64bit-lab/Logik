####################################################################################
#                         _                 _ _                                    #
#                        | |               (_) |                                   #
#                        | |     ___   __ _ _| | __                                #
#                        | |    / _ \ / _` | | |/ /                                #
#                        | |___| (_) | (_| | |   <                                 #
#                        |______\___/ \__, |_|_|\_\                                #
#                                      __/ |                                       #
#                                     |___/                                        #
#                                                                                  #
#                                                                                  #
#                A python module for propositionnal logik.                         #
#                                                                                  #
#  Author : Arthur Correnson                                                       #
#  Email  : arthur.correnson@gmail.com                                             #
#                                                                                  #
#                                                                                  #
#  This software may be freely distributed under the MIT license :                 #
#                                                                                  #
#                                                                                  #
#  MIT License                                                                     #
#                                                                                  #
#  Copyright (c) 2019 Arthur Correnson                                             #
#                                                                                  #
#  Permission is hereby granted, free of charge, to any person obtaining a copy    #
#  of this software and associated documentation files (the "Software"), to deal   #
#  in the Software without restriction, including without limitation the rights    #
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       #
#  copies of the Software, and to permit persons to whom the Software is           #
#  furnished to do so, subject to the following conditions:                        #
#                                                                                  #
#  The above copyright notice and this permission notice shall be included in all  #
#  copies or substantial portions of the Software.                                 #
#                                                                                  #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      #
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        #
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     #
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          #
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   #
#  SOFTWARE.                                                                       #
####################################################################################

from . evaluator import *
from . CLI import *
from . sat import *

# Main function (REPL)
def main():
    display_info()
    while True:
        string = input('[ command ] @ ')
        cmd(string)

