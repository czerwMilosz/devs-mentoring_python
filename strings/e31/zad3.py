def pato_deweloperka(dom = 'DOM'):
    domek = dom.lower()
    pomniejszacz_domkow = 'ek'
    for l in pomniejszacz_domkow:
        domek += l
    return domek

print(pato_deweloperka())