import math

pt1= (0,0)   #(x1,y1)
pt2= (1,1)   #(x2,y2)
pt3= (3,10)   #(x3,y3) bildet mit p1 eine andere Gerade mit anderem y- Durchlauf

# Grundformel linearer Gleichungen: y=mx+n
# Umformen nach n: n=y-mx
# Für x und y wird einer der Punkte eingesetzt
# Durchlauf durch die y- Achse dort, wo x=0, also ist n der Abschnitt auf der y- Achse

def ycross(p1,p2):
 m=(p2[1]-p1[1])/(p2[0]-p1[0])
 n=p1[1]-m*p1[0]
 
 return n, math.degrees(math.atan(m))


print (ycross(pt1,pt2))


