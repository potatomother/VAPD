
#疏水性评分
def atomradius(cname):
    if(cname == 'ILE'):
        return 99
    if(cname == 'PHE'):
        return 100
    if(cname == 'TRP'):
        return 97
    if(cname == 'LEU'):
        return 97
    if(cname == 'VAL'):
        return 176
    if(cname == 'MET'):
        return 74
    if(cname == 'TYR'):
        return 63
    if(cname == 'CYS'):
        return 49
    if(cname == 'ALA'):
        return 41
    if(cname == 'THR'):
        return 13
    if(cname == 'HIS'):
        return 8
    if(cname == 'GLY'):
        return 0
    if(cname == 'SER'):
        return -5
    if(cname == 'GLN'):
        return -10
    if(cname == 'ARG'):
        return -14
    if(cname == 'LYS'):
        return -23
    if(cname == 'ASN'):
        return -28
    if(cname == 'GLU'):
        return -31
    if (cname == 'APRO'):
        return -46
    if (cname == 'ASP'):
        return -55
    return 0

