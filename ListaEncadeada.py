class NODE:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None

class ListaEncadeada():
    def __init__(self):
        self.inicio = None
    
    def AddListaComeço(self, elemento):
        node_novo = NODE(elemento)
        proximo_node = self.inicio
        self.inicio = node_novo

    def AddListaFinal(self, elemento):
        node_novo = NODE(elemento)
        if not self.inicio:
            self.inicio = node_novo
            print('Nenhum outro valor encontrado')
            return
        while self.inicio.proximo:
            self.inicio = self.inicio.proximo
        self.inicio = node_novo

    def AddListaEspecifico(self,elemento, posicao):
        if posicao == 0:
            ListaEncadeada.AddListaComeço()
            return 
        node_novo = NODE(elemento)
        for c in range(posicao - 1):
            if not self.inicio:
                print("Posição inválida")
                return 
        node_novo.proximo = self.inicio.proximo
        node_novo.proximo = node_novo
    def ListarLista(self):
        print('Lista: ', end='')
        while self.inicio:
            print(self.inicio.elemento)
            self.inicio.proximo
        print()

        
def main():
    lista = ListaEncadeada()
    while True:
        node = int(input('Digite um número: '))
        lista.AddListaFinal(node)
main()