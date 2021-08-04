
#极性评分
def atomradius_jixing(cname):
    if(cname == 'LYS'):
        return 1
    if(cname == 'ARG'):
        return 1
    if(cname == 'HIS'):
        return 1
    if(cname == 'ASP'):
        return -1
    if(cname == 'GLU'):
        return -1

    return 0

