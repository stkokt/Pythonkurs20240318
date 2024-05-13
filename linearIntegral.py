def linearIntegral (liste):
    
    if liste[0] < 0:
        xcross = (-liste[0])/liste[1]
        return ((liste[2][0]-xcross)*liste[2][1])/2
    elif liste[0] == 0:
        return ((liste[2][0]*liste[2][1])/2)
    else:
        return ((liste[0]*liste[2][0])+(((liste[2][1]-liste[0])*liste[2][0])/2))
#                (ycross  * xcoord)     +  (ycoord     - ycross)* 