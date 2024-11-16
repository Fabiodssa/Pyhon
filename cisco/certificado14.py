def intro(a="James Bond", b=""):
    print("Meu nome é", b + ".", a + ".")
 
intro(b="Sean Connery")
 

def intro(a, b="Bond"):
    print("Meu nome é", b + ".", a + ".")
 
intro("Susan")

def add_numbers(a, c, b=2):  # valores obrigatorios devem ser adicionado antes dos valores padrões
    print(a + b + c)
 
add_numbers(a=1, c=3)