def invertir(sim):
    if sim == '+':
        return '-'
    
    elif sim == '-':
        return '+'

def nrz_l(sec):
    """
    Codifica una secuencia electrica a binaria en NRZ-L 

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "NRZ-L"

    code = []

    for i in sec:
        if i == '0':
            code.append('+')

        elif i == '1':
            code.append('-')

        else:
            raise(ValueError("Secuencia invalida"))

    return code, NAME

def nrz_i(sec):
    """
    Codifica una secuencia electrica a binaria en NRZ-I 

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "NRZ-I"

    code = ['+']

    for i in range(len(sec)):
        if sec[i] == '0':
            code.append(code[-1])

        elif sec[i] == '1':
            code.append(invertir(code[-1]))

        else:
            raise(ValueError("Secuencia invalida"))

    return code[1:], NAME

def rz(sec):
    """
    Codifica una secuencia electrica a binaria en RZ

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "RZ"
    
    code = []

    for i in sec:
        if i == '0':
            code.extend(['-', '0'])

        elif i == '1':
            code.extend(['+', '0'])

        else:
            raise(ValueError("Secuencia invalida"))
        
    return code, NAME

def manchester(sec):
    """
    Codifica una secuencia electrica a binaria en Manchester 

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "Manchester"

    code = []

    for i in sec:
        if i == '0':
            code.append('+')
            code.append('-')

        elif i == '1':
            code.append('-')
            code.append('+')

        else:
            raise(ValueError("Secuencia invalida"))
        
    return code, NAME

def manchester_dif(sec):
    """
    Codifica una secuencia electrica a binaria en Manchester Diferencial

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "Manchester Diferencial"

    code = ['+', '-']

    for i in range(len(sec)):
        if sec[i] == '0':
            code.extend([code[-2], code[-1]])

        elif sec[i] == '1':
            code.extend([code[-1], code[-2]])
        
    return code[2:], NAME
        
def ami(sec, last_sign='+'):
    """
    Codifica una secuencia electrica a binaria en AMI

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "AMI"

    code = []

    for i in sec:
        if i == '0':
            code.append('0')

        elif i == '1':
            last_sign = invertir(last_sign)
            code.append(last_sign)

        else:
            raise(ValueError("Secuencia invalida"))
        
    return code, NAME
        
def pseudoternario(sec, last_sign='+'):
    """
    Codifica una secuencia electrica a binaria en Pseudoternario

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "Pseudoternario"

    code = []

    for i in sec:
        if i == '0':
            last_sign = invertir(last_sign)
            code.append(last_sign)

        elif i == '1':
            code.append('0')

        else:
            raise(ValueError("Secuencia invalida"))
        
    return code, NAME

def hdb3(sec, last_sign = '+'):
    """
    Codifica una secuencia electrica a binaria en HDB3

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """
    
    NAME = "HDB3"

    code = []

    pulsos = 0

    i = 0
    while i < len(sec):
        if sec[i] == '1':
            last_sign = invertir(last_sign)
            code.append(last_sign)
            pulsos += 1

        elif sec[i] == '0':
            if i + 3 < len(sec):
                for j in range(4):
                    if sec[i + j] != '0':
                        code.append('0')
                        break

                else:
                    if pulsos % 2 == 0:
                        last_sign = invertir(last_sign)
                        code.extend([last_sign] + ['0'] * 2 + [last_sign])

                    else:
                        code.extend(['0'] * 3 + [last_sign])

       

                    pulsos = 0
                    i += 3  
            
            else:
                code.append('0')
        
        i += 1
        
    return code, NAME

def b8zs(sec, last_sign='+'):
    """
    Codifica una secuencia electrica a binaria en B8ZS

    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "B8ZS"

    code = []

    i = 0
    while i < len(sec):
        if sec[i] == '1':
            last_sign = invertir(last_sign)
            code.append(last_sign)

        elif sec[i] == '0':
            if i + 7 < len(sec):
                for j in range(8):
                    if sec[i + j] != '0':
                        code.append('0')
                        break

                else:
                        code.extend(['0'] * 3 + [last_sign, invertir(last_sign), '0', invertir(last_sign), last_sign])
                        i += 7
            
            else:
                code.append('0')
        
        i += 1
        
    return code, NAME

def mlt_3(sec, last_sign='+'):
    """
    Codifica una secuencia electrica a binaria en MLT-3
    
    Parametros: Secuencia binaria

    Retornos: Pulsos electrica
    """

    NAME = "MLT-3"

    class Ciclo():
        orden = ['+', '0', '-']
        now = 0
        sentido = 1

        def actualizar_sentido(self):
            if self.now == 0:
                self.sentido = 1

            elif self.now == len(self.orden) - 1:
                self.sentido = -1

        def next(self):
            self.now += self.sentido
            self.actualizar_sentido()
            return self.actual()

        def actual(self):
            return self.orden[self.now]
        
    ciclo = Ciclo()
    code = []

    for i in sec:
        if i == '0':
            code.append(ciclo.actual())

        elif i == '1':
            code.append(ciclo.next())

    return code, NAME

if __name__ == '__main__':
    pass