#6-rendre monaie
def rendreMonnai(s,sm):
    print(s,sm)
    if sm:
       nbPieceMax=s//sm[0]
       print(list(range(nbPieceMax+1)))
       reste = rendreMonnai(s-(nbPieceMax*sm[0]), sm[1:])
       return {sm[0]:nbPieceMax, **reste}
    else:
        return {}
rendreMonnai(353,(100,50,10,5,1))