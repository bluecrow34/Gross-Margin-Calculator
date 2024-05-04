def calRevenue(x,y):
    return x * y

def calTotalPay(x,y):
    return x*y

def calTotalBurden(x,y):
    return x+y

def calTotalComp(x,y):
    return x+y

def calTotalCost(x,y):
    return x*y

def calTotalGM(x,y):
    return x-y

def calGM(x,y):
    return x/y


def highlight_values(x):
    if x <0:
        return 'color: green'
    else:
        return 'color: red'
    
# Burden includes FICA(social Security & medicare), FUTA, SUTA, Projected Health
# Statutory + health
def calBurden(x,y):
    if y == 'AL':
        z = .0985
    elif y == 'AR':
        z = .1015
    elif y == 'AZ':
        z = .1104
    elif y == 'CA':
        z = .1355
    elif y == 'CO':
        z = .1151
    elif y == 'CT':
        z = .1145
    elif y == 'DC':
        z = .1255
    elif y == 'DE':
        z = .0995
    elif y == 'FL':
        z = .0988
    elif y == 'GA':
        z = .1048
    elif y == 'IA':
        z = .1065
    elif y == 'ID':
        z = .1034
    elif y == 'IL':
        z = .1110
    elif y == 'IN':
        z = .1325
    elif y == 'KS':
        z = .1234
    elif y == 'KY':
        z = .1065
    elif y == 'LA':
        z = .0974
    elif y == 'MA':
        z = .1356
    elif y == 'MD':
        z = .1275
    elif y == 'ME':
        z = .1315
    elif y == 'MI':
        z = .1225
    elif y == 'MN':
        z = .0985
    elif y == 'MO':
        z = .0965
    elif y == 'MS':
        z = .0985
    elif y == 'MT':
        z = .1105
    elif y == 'NC':
        z = .0971
    elif y == 'ND':
        z = .1090
    elif y == 'NE':
        z = .1010
    elif y == 'NH':
        z = .1155
    elif y == 'NJ':
        z = .1275
    elif y == 'NM':
        z = .1116
    elif y == 'NV':
        z = .1115
    elif y == 'NY':
        z = .1265
    elif y == 'OH':
        z = .1045
    elif y == 'OK':
        z = .0995
    elif y == 'OR':
        z = .1215
    elif y == 'PA':
        z = .1325
    elif y == 'RI':
        z = .1275
    elif y == 'SC':
        z = .1511
    elif y == 'SD':
        z = .0965
    elif y == 'TN':
        z = .1235
    elif y == 'TX':
        z = .1128
    elif y == 'UT':
        z = .0995
    elif y == 'VA':
        z = .1040
    elif y == 'VT':
        z = .1285
    elif y == 'WA':
        z = .1115
    elif y == 'WI':
        z = .1295
    elif y == 'WV':
        z = .1315
    elif y == 'WY':
        z = .1013
    else:
        z=0
    return x * z


## Complete at some point, will vary
def calWorkComp(x,y):
    if y == 'RI':
        z = .0509
    else:
        z=0
    return x*z

def calSick(x,y):
    if y == 'AZ':
        z = .019
    elif y == 'CA':
        z = .016
    elif y == 'CO':
        z = .023
    elif y == 'CT':
        z = .019
    elif y == 'DC':
        z = .012
    elif y == 'IL':
        z = .019
    elif y == 'MA':
        z = .019
    elif y == 'MD':
        z = .031
    elif y == 'ME':
        z = .019
    elif y == 'MI':
        z = .019
    elif y == 'MN':
        z = .023
    elif y == 'NJ':
        z = .019
    elif y == 'NM':
        z = .019
    elif y == 'NV':
        z = .019
    elif y == 'NY':
        z = .019
    elif y == 'OR':
        z = .019
    elif y == 'PA':
        z = .019
    elif y == 'RI':
        z = .019
    elif y == 'VT':
        z = .019
    elif y == 'WA':
        z = .021
    else:
        z=0
    return x*z


def calPerm(x,y):
    z= x /100
    return z*y