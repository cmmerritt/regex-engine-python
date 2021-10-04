import sys
sys.setrecursionlimit(10000)

reg, comp = input().split("|")

def match_string(reg, comp):
    if reg == comp or reg == '':
        return True
    if reg[0] == "\\":
        stripped_reg = reg.strip("\\")
        return match_string(stripped_reg, comp)
    if reg[0] == "^" and reg[-1] == "$":
        new_reg = reg[1:-1]
        if new_reg == comp:
            return True
        if "+" in new_reg:
            if new_reg[-1] != comp[-1]:
                return False
            else:
                return match_string(new_reg, comp)
        else:
            return False
    if "$" in reg:
        return match_string(reg[-2], comp[-1])
    if "^" in reg:
       return match_string(reg[1], comp[0])
    if len(reg) >= 2 and reg[1] == "?" and not reg[0] == "\\":
        if reg[0] == comp[0]:
            if len(reg[2:-1]) != len(comp[1:-1]):
                return False
            else:
                return match_string(reg[2:-1], comp[1:-1])
        else:
            return match_string(reg[2:], comp)
    if len(reg) >= 2 and reg[1] == "*" and not reg[0] == "\\":
        if reg[0] == comp[0]:
            return match_string(reg, comp[1:])
        else:
            return match_string(reg[2:-1], comp[1:])
    if len(reg) >= 2 and reg[1] == "+" and not reg[0] == "\\":
        if reg[0] == ".":
            return True
        elif reg[0] not in comp:
            return False
        elif reg[0] == comp[0]:
            return match_string(reg[2:-1], comp[1:-1])
        else:
            return match_string(reg, comp[1:])
    elif comp == '':
        return False
    elif reg[0] == comp[0] or reg[0] == ".":
        return match_string(reg[1:], comp[1:])
    elif reg[0] != comp[0]:
        if len(reg) == len(comp):
            return False
        else:
            return match_string(reg[1:], comp[1:])
    else:
        return False


print(match_string(reg, comp))
