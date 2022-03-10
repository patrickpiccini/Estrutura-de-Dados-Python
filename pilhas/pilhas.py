class Pilha:
    def __init__(self):
        self._vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self._vet[-1]
        
       
    def push(self, item): # metodo de inserir item
        self._vet.append(item)

        
        
    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
            if len(self._vet) > 0:
                return self._vet.pop()
        
        
    def is_empty(self): # teste se é vazia
        return False if len(self._vet) > 0 else True
        
        
        
    def __len__(self): # retorna o total de itens
        return len(self._vet)

    def __str__(self): # representacao da pilha como string
        return str(self._vet)

## T