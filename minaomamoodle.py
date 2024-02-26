def Korrutis(arv1:float,arv2:float,arv3:float,arv4=1.0)->float:
    """Funktsioon tagastab 4 arvude korrutis, arvus sissestab kasutaja. Vaikmisi
    arv4=1.0. tulemus tagastatakse float formaadis.

    :param float arv1: sissestatakse nagu parameeter
    :param float arv2: sissestatakse nagu parameeter
    :param float arv3: sissestatakse nagu parameeter
    :param float arv4: sissestatakse nagu parameeter / vaikimisi võrdub ühega
    :rtype: float
    """
    k=arv1*arv2*arv3*arv4
    return k
def Suurim_element(arvud1:list,arvud2:list): #->any: ne nado)
    """Funktsioon kuvab ekranile suurim arv listidest.

    :param,list arvud1: Arvude loetelu
    :param,list arvud2: Arvude loetelu
    #:rtype: any (ne nado)
    """
    Suurim1=max(arvud1)
    Suurim2=max(arvud2)
    Suurim=max(Suurim1,Suurim2)
    print(Suurim)