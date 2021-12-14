from IIND import app, forms
from flask import render_template,url_for,redirect
from IIND.forms import matrixForm, crossProductForm, dotProductForm, systemForm
from IIND.useful import isSquareMatrix, validateMatrix,formToMatrix, plotVectors
from numpy.linalg import det,inv
from numpy import cross,dot
from flask import request
import pandas as pd


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

@app.route("/estadistica")
def estadistica():
    return render_template("menu_estadistica.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        return data_xls.to_html()
    return render_template("upload.html")

@app.route("/error")
def error():
    return render_template("error.html",item = error_string)