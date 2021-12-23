from IIND import app, forms
from flask import render_template,url_for,redirect
from IIND.forms import matrixForm, crossProductForm, dotProductForm, systemForm
from IIND.useful import isSquareMatrix, validateMatrix,formToMatrix, plotVectors
from numpy.linalg import det,inv
from numpy import cross,dot
from flask import request
import pandas as pd
import IIND.graficosDeControl as gc
import IIND.numerosAleatorios as na


error_string = ""

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Algebra_lineal") 
def menu_algebra_lineal():
    return render_template('menu_algebra_lineal.html')

@app.route("/Algebra_lineal/determinante",methods= ["GET","POST"])
def determinante():
    f = matrixForm()
   
    if (f.validate_on_submit()):
        
        Matrix = formToMatrix(f)
        
        if(isSquareMatrix(Matrix)):
            res = det(Matrix)
        else:
            global error_string
            error_string = "Error: Verifique la matriz ingresada"
            return redirect(url_for("error"))

        return render_template('determinente_respuesta.html',item = res)
       
    return render_template('determinante.html', form = f)

@app.route("/Algebra_lineal/producto_cruz",methods= ["GET","POST"])
def producto_cruz():
    f = crossProductForm()

    if(f.validate_on_submit()):
        vectors = f.getVectors()
        u = vectors[0]
        v = vectors[1]
        uxv = cross(u,v)
        s = plotVectors(u,v,uxv)
        return render_template('producto_cruz_respuesta.html',items = uxv, image = s)


    return render_template('producto_cruz.html',form = f)

@app.route("/Algebra_lineal/producto_punto",methods=["GET","POST"])
def producto_punto():
    f = dotProductForm()
    if f.validate_on_submit():
        vectors = f.getVectors()
        u = vectors[0]
        v = vectors[1]
        udv = dot(u,v)
        return render_template("producto_punto_respuesta.html",item = udv)


    return render_template("producto_punto.html",form = f)

@app.route("/Algebra_lineal/sistema", methods = ["GET","POST"])
def sistema():
    f = systemForm()
    if f.validate_on_submit():
        mat = formToMatrix(f)
        extended = []

        g = f.r1.data
        if(g != None):
            extended.append(g)
        g = f.r2.data
        if(g != None):
            extended.append(g)
        g = f.r3.data
        if(g != None):
            extended.append(g)
        g = f.r4.data
        if(g != None):
            extended.append(g)
        g = f.r5.data
        if(g != None):
            extended.append(g)

        matInv = inv(mat)
        r = dot(matInv,extended)
        return render_template("sistema_respuesta.html",items = r)

    return render_template("sistema.html",form = f)

@app.route("/control_estadistico")
def menu_control_estadistico():

    return render_template("menu_control_estadistico.html")

@app.route("/control_estadistico/GraficoX",methods=["POST","GET"])
def graficoX():
    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.DataFrame(pd.read_excel(f))
        a2 = request.values.get('A2')
        d3 = request.values.get('D3')
        d4 = request.values.get('D4')
        image = gc.graficoX(data_xls)
        
        return render_template('resultado_grafico_de_control.html', image= image)
    return render_template("graficoX.html")

@app.route("/control_estadistico/GraficoP",methods=["POST","GET"])
def graficoP():
    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.DataFrame(pd.read_excel(f))
        n = request.values.get('n')
        
        image = gc.graficoP(data_xls,n)
        
        return render_template('resultado_grafico_de_control.html', image= image)
    return render_template("graficoP.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        return data_xls.to_html()
    return render_template("upload.html")

@app.route("/numeros_aleatorios")
def numeros_aleatorios():
    return render_template('menu_numeros_aleatorios.html')

@app.route("/numeros_aleatorios/cuadrados_de_enmedio",methods=["POST","GET"])
def cuadrados_de_enmedio():
    if request.method == "POST":
        n = int(request.values.get("n"))
        seed = int(request.values.get("semilla"))
        res = na.cuadradosDeEnmedio(seed,n)
       
        if(res[1] == True):
            return render_template('resultado_numeros_aleatorios.html',mylist = res[0],item="Los numeros siguen una distribución uniforme con α=0.05")
        else:
            return render_template('resultado_numeros_aleatorios.html',mylist = res[0],item="Los numeros NO soguen una distribución uniforme con α=0.05")

    return render_template('cuadrados_de_enmedio.html')

@app.route("/numeros_aleatorios/congruencial_multiplicativo",methods=["POST","GET"])
def congruencial_multiplicativo():
    if request.method == "POST":
        n = int(request.values.get("n"))
        seed = int(request.values.get("semilla"))
        mod = int(request.values.get("mod"))
        a = int(request.values.get("a"))
        res = na.congruencialMultiplicativo(seed,mod,a,n)
        if(res[1] == True):
            return render_template('resultado_numeros_aleatorios.html',mylist = res[0],item="Los numeros siguen una distribución uniforme con α=0.05")
        else:
            return render_template('resultado_numeros_aleatorios.html',mylist = res[0],item="Los numeros NO soguen una distribución uniforme con α=0.05")

    return render_template('congruencial_multiplicativo.html')


@app.route("/error")
def error():
    return render_template("error.html",item = error_string)