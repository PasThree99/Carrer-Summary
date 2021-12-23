import sympy as sy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64



def parametricPlot(x_expr:str, y_expr:str, z_expr:str, variable:str, range:tuple):
    def evaluate(exp,a,b,step):
        c = a
        lf = []
        while(c <= b):
            n = exp.subs(variable,c)
            n = float(n)
            lf.append(n)
            c += step
        return lf



    i = sy.sympify(x_expr)
    j = sy.sympify(y_expr)
    k = sy.sympify(z_expr)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #print(evaluate(i,0,1000,0.1))

    ax.plot(evaluate(i,int(range[0]),int(range[1]),0.1),evaluate(j,int(range[0]),int(range[1]),0.1),evaluate(k,int(range[0]),int(range[1]),0.1))
    
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String



