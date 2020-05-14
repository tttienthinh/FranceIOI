def deplacement(nbrPiece, source, destination, tempory):
    if nbrPiece <= 0:
        return
    deplacement(nbrPiece-1, source, tempory, destination)
    print(str(source)+" -> "+str(destination))
    deplacement(nbrPiece-1, tempory, destination, source)
nbrPiece = int(input())
deplacement(nbrPiece, 1, 3, 2)