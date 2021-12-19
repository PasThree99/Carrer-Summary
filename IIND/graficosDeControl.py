import numpy as np 
import scipy.stats as ss 
import pandas as pd 
import matplotlib.pyplot as plt
import io
import os
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from IIND.tablas import coeficientesDeControl
from math import sqrt


def graficoX(datos):
    prom = []
    ran = []

    tabla = coeficientesDeControl()

    observaciones = len(datos.columns)-1

    A2 = tabla.getCoeficient(observaciones,"A2")
    D3 = tabla.getCoeficient(observaciones,"D3")
    D4 = tabla.getCoeficient(observaciones,"D4")
    for i in range(len(datos)):
        va=datos.iloc[i][1:]
        prom.append(np.mean(va))
        ran.append(max(va)-min(va))
    datos['Promedio'] = prom
    datos['Rango'] = ran

    granX = np.mean(datos['Promedio'])
    granR = np.mean(datos['Rango'])

    print(A2,D3,D4)

    #A2 = float(input('Ingresa A2_'))
    #D3 = float(input('Ingresa D3_'))
    #D4 = float(input('Ingresa D4_'))

    LCSX = granX + A2 * granR
    LCIX = granX - A2 * granR

    LCSR = granR * D4
    LCIR = granR * D3

    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    #Graficar el X
    #ax.figure(1)
    plt.subplot(2,1,1)
    ax.title.set_text('Gráfico X')
    ax.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*LCSX,label='LCS')
    ax.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*LCIX,label='LCI')
    ax.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*granX,label='LCC')
    ax.plot(np.arange(1,len(datos)+1),datos['Promedio'])
    ax.legend()
    ax.grid()

    #Graficar el R
    plt.subplot(2,1,2)
    ax2.title.set_text('Gráfico R')
    ax2.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*LCSR,label='LCS')
    ax2.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*LCIR,label='LCI')
    ax2.plot(np.arange(1,len(datos)+1),np.ones(len(datos))*granR,label='LCC')
    ax2.plot(np.arange(1,len(datos)+1),datos['Rango'])
    ax2.legend()
    ax2.grid()

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    path = os.getcwd()
    path += "/IIND/static/images/cross.png"
    #plt.savefig(path)
    return pngImageB64String

def graficoP(datos,n):
    def desviacionEstandar(p,n):
        return sqrt(3*(p*(1-p)/n))
   
    n = int(n)
    datos = pd.DataFrame(datos)

    datos = datos.iloc[:,1:]
    cols=datos.columns


    datos[cols[0]] = datos[cols[0]]/n

    p = np.mean(datos[cols[0]])


    LCS = p + desviacionEstandar(p,n)
    LCC = p
    LCI = p - desviacionEstandar(p,n)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(range(len(datos)),np.ones(len(datos))*LCS,label = "LCS")
    ax.plot(range(len(datos)),np.ones(len(datos))*LCI,label = "LCI")
    ax.plot(range(len(datos)),np.ones(len(datos))*LCC,label = "LCC")
    ax.plot(range(len(datos)),datos[cols[0]])
    ax.grid()
    ax.title.set_text('Gráfico P')
    ax.legend()
    #ax.set_ylim(LCI-2,LCS+2)
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    path = os.getcwd()
    path += "/IIND/static/images/cross.png"
    #plt.savefig(path)
    return pngImageB64String