import numpy as np

speed=int(input())
acc=int(input())

def leftOpen(x,alpha,beta):
    if x<alpha:
        return 1
    elif x>alpha and x<=beta:
        return (beta-x)/(beta-alpha)
    else:
        return 0

def rightOpen(x,alpha,beta):
    if x<alpha:
        return 0
    elif x>alpha and x<=beta:
        return (x-alpha)/(beta-alpha)
    else:
        return 1

def triangleArea(x,a,b,c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)),0)

def splitting(x):
    NL = 0;  NM = 0; NS = 0; ZE = 0; PS = 0; PM = 0; PL = 0
    if x> 0 and x<61:
        NL = leftOpen(x,31,61)
    if x> 31 and x<95:
        NM = triangleArea(x,31,61,95)
    if x> 61 and x<127:
        NS = triangleArea(x,61,95,127)
    if x> 95 and x<159:
        ZE = triangleArea(x,95,127,159)
    if x> 127 and x<191:
        PS = triangleArea(x,127,159,191)
    if x> 159 and x<223:
        PM = triangleArea(x,127,159,191)
    if x> 191 and x<255:
        PL = rightOpen(x,191,255)
    return NL,NM,NS,ZE,PS,PM,PL

NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD = splitting(speed)
NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC = splitting(acc)

res = [[NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD],
          [NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC]]
print("The fuzzy values of the crisp inputs")
print(["NL","NM","NS","ZE","PS","PM","PLSD"])
print(np.round(res,2))

def compare(TC1, TC2):
    TC = 0
    if TC1>TC2 and TC1 !=0 and TC2 !=0:
        TC = TC2
    else:
        TC = TC1
    if TC1 == 0 and TC2 !=0:
        TC = TC2
    if TC2 == 0 and TC1 !=0:
        TC = TC1
    return TC

def rule(NLSD, NMSD, NSSD, ZESD, PSSD, PMSD, PLSD, NLAC, NMAC, NSAC, ZEAC, PSAC, PMAC, PLAC):
    PLTC1 = min(NLSD, ZEAC) 
    PLTC2 = min(ZESD, NLAC)
    PLTC = max(PLTC1, PLTC2)

    PMTC1 = min(NMSD, ZEAC)
    PMTC2 = min(ZESD, NMAC)
    PMTC = max(PMTC1, PMTC2)

    PSTC1 = min(NSSD, PSAC)
    PSTC2 = min(ZESD, NSAC)
    PSTC = max(PSTC1, PSTC2)

    NSTC = min(PSSD, NSAC)
    NLTC = min(PLSD, ZEAC)

    return PLTC, PMTC, PSTC, NSTC, NLTC


PLTC, PMTC, PSTC, NSTC, NLTC = rule(NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD,NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC)

resRules = [[PLTC, PMTC, PSTC, NSTC, NLTC ]]
print("The fuzzy output: ")
print(["PLTC", "PMTC", "PSTC", "NSTC", "NLTC"])
print(np.round(resRules,2))


def areaTR(mu, a,b,c):
    x1 = mu*(b-a) + a
    x2 = c - mu*(c-b)
    d1 = (c-a); d2 = x2-x1
    a = (1/2)*mu*(d1 + d2)
    return a 

def areaOL(mu, alpha, beta):
    xOL = beta -mu*(beta - alpha)
    return 1/2*mu*(beta+ xOL), beta/2

def areaOR(mu, alpha, beta):
    xOR = (beta - alpha)*mu + alpha
    aOR = (1/2)*mu*((255 - alpha) + (255 -xOR))
    return aOR, (255 - alpha)/2 + alpha

def defuzzyfication(PLTC, PMTC, PSTC, NSTC, NLTC):
    areaPL = 0; areaPM = 0; areaPS = 0; areaNS = 0; areaNL = 0;
    cPL = 0; cPM = 0; cPS = 0; cNS = 0; cNL = 0;
    if PLTC != 0:
        areaPL, cPL = areaOR(PLTC, 191, 223)
    if PMTC != 0:
        areaPM = areaTR(PMTC, 159, 191, 223)
        cPM = 191
    if PSTC != 0:
        areaPS = areaTR(PSTC, 127, 159, 191)
        cPS = 159
    if NSTC != 0:
        areaNS = areaTR(NSTC, 61, 95, 127)
        cNS = 95
    if NLTC !=0:
        areaNL, cNL = areaOL(NLTC, 31, 61)
        
    numerator = areaPL*cPL + areaPM*cPM + areaPS*cPS + areaNS*cNS + areaNL*cNL
    denominator = areaPL + areaPM + areaPS + areaNS + areaNL
    if denominator ==0:
        print("No rules exist to give the result")
        return 0
    else:
        crispOutput = numerator/denominator
        return crispOutput
crispOutputFinal = defuzzyfication(PLTC, PMTC, PSTC, NSTC, NLTC)

if crispOutputFinal !=0:
    print("\nThe crisp TC value is: ", crispOutputFinal)