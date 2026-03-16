import sys

class MaquinaTuringNinja:
    def __init__(self, entrada):
        self.fita = list(entrada)
        self.cabecote = 0
        self.estado = 'q0'
        self.alfabeto_origem = ['T', 'N', 'G']
        self.finalizado = False
        self.aceito = False

    def exibir_passo(self):
        conteudo = "".join(self.fita)
        print(f"Estado: {self.estado} | Fita: {conteudo}")

    def executar(self):
        while not self.finalizado:
            self.exibir_passo()
            
            if self.estado == 'q0':
                if self.fita[self.cabecote] == 'T':
                    self.fita[self.cabecote] = 'X'
                    self.cabecote += 1
                    self.estado = 'q1'
                elif self.fita[self.cabecote] == 'Y':
                    self.estado = 'q4'
                else:
                    self.finalizado = True

            elif self.estado == 'q1':
                if self.fita[self.cabecote] in ['T', 'Y']:
                    self.cabecote += 1
                elif self.fita[self.cabecote] == 'N':
                    self.fita[self.cabecote] = 'Y'
                    self.cabecote += 1
                    self.estado = 'q2'
                else:
                    self.finalizado = True

            elif self.estado == 'q2':
                if self.fita[self.cabecote] in ['N', 'Z']:
                    self.cabecote += 1
                elif self.fita[self.cabecote] == 'G':
                    self.fita[self.cabecote] = 'Z'
                    self.cabecote -= 1
                    self.estado = 'q3'
                else:
                    self.finalizado = True

            elif self.estado == 'q3':
                if self.fita[self.cabecote] in ['T', 'N', 'Y', 'Z']:
                    self.cabecote -= 1
                elif self.fita[self.cabecote] == 'X':
                    self.cabecote += 1
                    self.estado = 'q0'
                else:
                    self.finalizado = True

            elif self.estado == 'q4':
                if self.cabecote < len(self.fita) and self.fita[self.cabecote] == 'Y':
                    self.cabecote += 1
                elif self.cabecote < len(self.fita) and self.fita[self.cabecote] == 'Z':
                    self.cabecote += 1
                elif self.cabecote == len(self.fita) or self.fita[self.cabecote] == '_':
                    self.estado = 'ACCEPT'
                    self.aceito = True
                    self.finalizado = True
                else:
                    self.finalizado = True

        if self.aceito:
            self.exibir_passo()
            print("Resultado: ACEITO")
        else:
            print("Resultado: REJEITADO")

def simulador():
    entrada = input("Insira a sequência de nomes (T, N, G): ").upper()
    if not entrada:
        return
    
    processamento = entrada + "_"
    mt = MaquinaTuringNinja(processamento)
    mt.executar()

if __name__ == "__main__":
    simulador()