
class Professor():
 
    
    def __init__(self):
        self.notasHist = [] 
        self.notasMat = []
        
        
        
    def hist(self, addNota):
       self.addNota = addNota
       self.notasHist.append(addNota)
    
    
    def mat(self, addNota):
       self.addNota = addNota
       self.notasMat.append(addNota)


    def boletim(self):
       global x
       x = print(f'Suas notas em Historia: {self.notasHist}')
       print(f'Suas notas em Matematica: {self.notasMat}')
       


class Aluno(Professor):

    def mostrarBoletim(self):
       pass
        
        
        
        


ana = Professor()
ana1 = Aluno()

ana.hist(10)
ana.mat(5)

ana.boletim(x)

print(x)



    