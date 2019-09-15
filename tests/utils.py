import logik as lgk


def equivalent(exprA, exprB):
    vars1 = lgk.get_vars(exprA)
    vars2 = lgk.get_vars(exprB)
    vars1.sort()
    vars2.sort()
    
    if vars1 == vars2:
        envs, _ = lgk.make_envs(vars1)
        eq = True
        i = 0
        while i < len(envs) and eq == True:
            eq = eq and (lgk.evaluate(exprA, envs[i]) == lgk.evaluate(exprB, envs[i]))
            i += 1

        return eq
    
    else:
        return False
