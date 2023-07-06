class Pessoa():
    nome = None
    sobrenome = None

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
        
erick = Pessoa()
erick.nome = 'Erick'
erick.sobrenome = 'Monteiro'

renato = Pessoa()
renato.nome = 'Renato'
renato.sobrenome = 'Carvalho'

#print(f'{erick.nome} {erick.sobrenome}')
print(erick)
print(renato)