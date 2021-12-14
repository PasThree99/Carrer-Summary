from re import M
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import array,cross
import io
import os
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')


def validateMatrix(mat):
    s = len(mat[0])
    for i in mat:
        if(len(i) != s):
            return False
    return True

def isSquareMatrix(mat):
    s = len(mat[0])
    if(validateMatrix(mat) and s == len(mat)):
        return True
    else:
        return False


def formToMatrix(f):
    Matrix = []
    Matrix.clear()
    aRow = []
    
    a = f.n1.data
    if(a != None):
        aRow.append(a)

    a = f.n2.data
    if(a != None):
        aRow.append(a)
    
    a = f.n3.data
    if(a != None):
        aRow.append(a)
    
    a = f.n4.data
    if(a != None):
        aRow.append(a)
    
    a = f.n5.data
    if(a != None):
        aRow.append(a)


    if(len(aRow) > 0):
        Matrix.append(aRow.copy())
    aRow.clear()
            

    a = f.n6.data
    if(a != None):
        aRow.append(a)

    a = f.n7.data
    if(a != None):
        aRow.append(a)
    
    a = f.n8.data
    if(a != None):
        aRow.append(a)
    
    a = f.n9.data
    if(a != None):
        aRow.append(a)
    
    a = f.n10.data
    if(a != None):
        aRow.append(a)

    
    if(len(aRow) > 0):
        Matrix.append(aRow.copy())
    aRow.clear()

    
    a = f.n11.data
    if(a != None):
        aRow.append(a)

    a = f.n12.data
    if(a != None):
        aRow.append(a)
    
    a = f.n13.data
    if(a != None):
        aRow.append(a)
    
    a = f.n14.data
    if(a != None):
        aRow.append(a)
    
    a = f.n15.data
    if(a != None):
        aRow.append(a)


    if(len(aRow) > 0):
        Matrix.append(aRow.copy())
    aRow.clear()


    a = f.n16.data
    if(a != None):
        aRow.append(a)

    a = f.n17.data
    if(a != None):
        aRow.append(a)
    
    a = f.n18.data
    if(a != None):
        aRow.append(a)
    
    a = f.n19.data
    if(a != None):
        aRow.append(a)
    
    a = f.n20.data
    if(a != None):
        aRow.append(a)

    if(len(aRow) > 0):
        Matrix.append(aRow.copy())
    aRow.clear()
        
    a = f.n21.data
    if(a != None):
        aRow.append(a)

    a = f.n22.data
    if(a != None):
        aRow.append(a)
    
    a = f.n23.data
    if(a != None):
        aRow.append(a)
    
    a = f.n24.data
    if(a != None):
        aRow.append(a)
    
    a = f.n25.data
    if(a != None):
        aRow.append(a)

    if(len(aRow) > 0):
        Matrix.append(aRow.copy())
    aRow.clear()

    return Matrix

def plotVectors(u,v,uxv):
    a = [0,0,0]
    b = [0,0,0]
    a.extend(u)
    b.extend(v)

    m = max(a)
    m2 = max(b)
    m = max(m,m2)
    m+=1

    mi = min(a)
    mi2 = min(b)
    mi = min(mi,mi2)

    m = int(m)
    mi = int(mi)

    l =[i for i in range(0,m+1)]
    c = [0 for i in range(len(l))]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0,0,0,u[0],u[1],u[2],label="u",color='black')
    ax.quiver(0,0,0,v[0],v[1],v[2],label="v",color='purple')
    ax.quiver(0,0,0,uxv[0],uxv[1],uxv[2],label="u x v",color='red')

    ax.plot(l,c,c,label="Eje +x")
    ax.plot(c,l,c,label="Eje +y")
    ax.plot(c,c,l, label="Eje +z")
    
    ax.set_xlim([mi, m])
    ax.set_ylim([mi, m])
    ax.set_zlim([mi, m])
    plt.legend()

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    path = os.getcwd()
    path += "/IIND/static/images/cross.png"
    plt.savefig(path)
    return pngImageB64String




