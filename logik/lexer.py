import re

def lex(string : str):
    """
    @brief      Perform lexing on a string.
    
    @param      string   The stringuence
    
    @return     an iterator on tokens
    """
    l = len(string)
    
    while l > 0:
        c = string[0]
        next_position = 0

        if c == ' ':
            string = string[1:]
        
        elif c in ('0', '1'):
            yield ('value', c)
            string = string[1:]

        elif re.match('->|et|ou', string):
            match = re.match('->|et|ou', string)
            yield ('binop', match.group(0))
            next_position = match.end()

        elif re.match('non', string):
            yield ('unop', string[0:4])
            next_position = 4

        elif re.match('[a-zA-Z]+', string, re.M):
            match = re.match('[a-zA-Z]+', string, re.M)
            yield ('symb', match.group(0))
            next_position = match.end()

        elif c in ('(', ')'):
            yield (c, '')
            next_position = 1

        else:
            print('errror')
            break
        
        string = string[next_position:]
        l = len(string)


def pprint(token):
    """
    @brief      Pretty print a token
    
    @param      token  The token
    """
    print('\033[31m'
        + token[0]
        + "\033[0m"
        + (6 - len(token[0]))*" " + ":",
        end=" "
    )
    print(token[1])


if __name__ == '__main__':
    string = input('>>> ')
    for i, tokens in enumerate(lex(string)):
        print(i+1, end=" ")
        pprint(tokens)


