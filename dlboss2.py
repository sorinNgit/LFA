from graphics import *
f = open("dlboss.in", "r")

nr_noduri = int(f.readline())

noduri = []

for i in f.readline().split():
    noduri.append(i)

valori=[]
for i in f.readline().split():
    valori.append(i)
print(valori)

nod_initial = f.readline()

nod_final = []
for i in f.readline().split():
    nod_final.append(i)

automat = dict()
for i in noduri:
    automat.update({i: []})
for i in f.readlines():
    i = i.split()
    automat.setdefault(i[0], []).append((i[1], i[2]))


print(automat)

cuvant = str(input("Cuvant: "))

nod_curent=nod_initial[0]

for i in cuvant:
    ok = 1
    if i not in valori:
        print("Nu apartine automatului")
        ok=0
        break
    for j in range(len(automat[nod_curent])):
        if i == automat[nod_curent][j][1]:
            nod_curent = automat[nod_curent][j][0]
            ok = 1
            break
        ok = 0
    if ok == 0:
        print("Nu apartine automatului")
        break

if nod_curent not in nod_final and ok!=0:
    print("Nu apartine automatului")
elif ok!=0:
    print("Apartine automatului")


def getpoint(nod):
    global x,y,win

    pt1=Point(x,y)
    cerc_actual=Circle(pt1,30)
    cerc_actual.setWidth(2)
    txt1=Text(pt1,noduri[nod])
    if noduri[nod][0]==nod_initial[0]:
        cerc_actual.setOutline("green")
    elif noduri[nod][0] in nod_final:
        cerc_actual.setOutline("red")
        cerc_final1=Circle(pt1,25)
        cerc_final1.draw(win)
    txt1.draw(win)
    cerc_actual.draw(win)
def getarrow(nod1,nod2,txt):
    global x,y,win
    if nod1==nod2:
        circle1=Circle(Point(nod1[0],nod1[1]+30),20)
    line=Line(Point(nod1[0],nod1[1]),Point(nod2[0],nod2[1]))
    text1=Text(Point(nod2[0]-nod1[0],nod2[1]-nod1[1]),txt)
    line.setArrow("last")
    line.draw(win)
def getarrowSame(nod,txt):
    global win
    if nod in same:
        circle1 = Circle(Point(nod[0]+46, nod[1]), 16)
        text1 = Text(Point(nod[0]+46, nod[1]), txt)
    else:
        circle1 = Circle(Point(nod[0], nod[1] + 46), 16)
        text1 = Text(Point(nod[0], nod[1] + 46), txt)
    same.append(nod)
    circle1.draw(win)
    text1.draw(win)
x=60
y=500
win=GraphWin("My Window",1000,1000)

same=[]
def main():
    global x,y
    coord_noduri=dict()
    arrowInitial=Line(Point(15,500),Point(30,500))
    arrowInitial.setArrow("last")
    for i in range(len(noduri)):
        getpoint(i)
        coord_noduri.update({noduri[i]: (x,y)})
        x+=90
        if i%2==0:
            y+=220
        elif i%3==0:
            y-=120
        else: y-=320

    for i in range(nr_noduri):
        for j in range(len(automat[noduri[i]])):
            if noduri[i]==automat[noduri[i]][j][0]:
                getarrowSame(coord_noduri[noduri[i]],automat[noduri[i]][j][1])
            else:
                getarrow(coord_noduri[noduri[i]],coord_noduri[automat[noduri[i]][j][0]],automat[noduri[i]][j][1])

    #line=Line(Point(270,250),Point(300,250))
    #line.setArrow("last")
    #line.draw(win)
    win.getMouse()
    win.close()
main()