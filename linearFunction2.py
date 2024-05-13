import linearIntegral


pt1= (1,1)   #(x1,y1)
pt2= (5,3)   #(x2,y2)

pt3= (2,4)   #(x3,y3) bildet mit p1 eine andere Gerade mit anderem y- Durchlauf
pt4= (5,7)

# Grundformel linearer Gleichungen: y=mx+n
# Umformen nach n: n=y-mx
# Für x und y wird einer der Punkte eingesetzt
# Durchlauf durch die y- Achse dort, wo x=0, also ist n der Abschnitt auf der y- Achse

def ycross(p1,p2):
 anstieg=(p2[1]-p1[1])/(p2[0]-p1[0])
 ycross=p1[1]-anstieg*p1[0]
 
 return [ycross, anstieg, p2]

#x, y, z = ycross(pt3,pt4)

print (ycross(pt3,pt4))


print (linearIntegral.linearIntegral(ycross(pt3,pt4)))