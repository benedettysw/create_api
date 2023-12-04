from flask import render_template
from basededato import  main







from model.regsitro import login






@main.route('/')
def inicio():
    titulo ="hola esto es muy"
    return render_template('inicio.html' , titulo=titulo)






if __name__ == '__main__':
    main.run(port=500 , debug=True)

