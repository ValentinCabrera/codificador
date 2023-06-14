from .codes import *
from .graphic import save_graphic

def code(binario, metodo="nrz_i"):
    if metodo == "nrz_i":
        encoded, name = nrz_i(binario)

    elif metodo == "rz":
        encoded, name = rz(binario)

    elif metodo == "manchester":
        encoded, name = manchester(binario)

    elif metodo == "manchester_dif":
        encoded, name = manchester_dif(binario)

    elif metodo == "ami":
        encoded, name = ami(binario)

    elif metodo == "pseudoternario":
        encoded, name = pseudoternario(binario)

    elif metodo == "hdb3":
        encoded, name = hdb3(binario)

    elif metodo == "b8zs":
        encoded, name = b8zs(binario)

    elif metodo == "mlt_3":
        encoded, name = mlt_3(binario)


    file_name = save_graphic(binario, encoded, name)
    return file_name

    
if __name__ == '__main__':
    sec = '1100001000000000100000'
    code(sec)