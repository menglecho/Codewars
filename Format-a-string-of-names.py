def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


def namelist(names):
    #your code here
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    else:
        sep = ', '
        result = []
        for n in range(len(names) - 2):
            result.append(names[n]['name'])
        return sep.join(result) + ', ' + names[n+1]['name'] + ' & ' + names[n+2]['name']   