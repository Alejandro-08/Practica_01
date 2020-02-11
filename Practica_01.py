"""          Practica 01 - Introducción
           Pedro Fernando Flores Palmeros
                Programación avanzada
                    Febrero 2020 
           Fernández Hernández Alejandro   
                      2RV1 
Ingeneria en Sistemas Energeticos y Redes Inteligentes   """

#Tema # 1    Lista                                       

bicycles=["trek", "cannondale", "readline", "specialized"]
print(bicycles)

"""Pude observar que en estas dos anteriores lineas de codigo que imrprime
la lista de bicycles tal cual esta escrita e inclutendo los corchetes."""

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[1])

"""En la ultima linea de codigo identifique que al ponerle entre corchetes un 
numero, al momento de correr el programa solo enseña el segundo termino de la 
lista"""

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0].title())

"""En este lo que cambia es que el .title() lo que hace es poner la primera
del primer termino (indice 0 de la lista) en mayuscula, si es que la tiene 
minuscula e imprime Cannondale."""

names=["\nirving","tavo","carlos","armando"]
print(names[0].title()),",¿Como has estado bro?"
print(names[1].title()),",¿Que hay más de tarea?"
print(names[2].title()),",¿Que andas haciendo?"
print(names[3].title()),",¿Vas a ir mañana?"

My_wishes=["\nMe gustaria tener unos tennis negros","Me gustaria estar un poco "
           "más alto","Me gustaria viajar por el mundo", "Desearia visitar "
           "Universal Studios", "Desearia tener un Mini Cooperr", "Desearia "
           "que mi abuelo siga en vida","Desearia contarle mi gran triunfo "
           "a dicha persona y decirle que lo logre", "Me gustaria tener mis "
           "dientes parejos"," Me gustaria poder conocer a un idolo en vivo "
           "y a todo color", "Me gustaria aprender a bailar muy bien salsa "
           "y cumbias", "Desaria poder aprender un deporte extremo", "Me "
           "gustaria aprender a tocar el piano, la guitarra, violin, entre "
           "otros instrumentos","Desaria tener una mejor condición fisica",
           "Desearia dejar de ser bipolar(literal)", "Desaria saber si existi "
           "en algun tipo de vida pasada","Me gustaria aprender muy bien el "
           "ingles", "Me gustaria aprender demás idiomas", "Me gustaria que "
           "el tiempo de durase más","Desearia que mis deseos fuesen realidad ",
           "Desearia que los deseos que son más reales se cumplan en verdad ", 
           "Me gustaria ser lampiño de los brazos", "Desaria tener ojos "
           "entre color azul, gris y verde "]
print(My_wishes[0]+ '.')
print(My_wishes[10]+ '.')
print(My_wishes[17]+ '.')
print(My_wishes[18]+ '.')
print(My_wishes[20]+ '.')
print(My_wishes[21]+ '.')


#Tema # 2    Modificando, Agregando y Removiendo elementos de la lista

#Tema # 3    Funciones

#3.4 TAREA

# • • T-Shirt:
def make_shirt(size, text): 
    print("\n Shirt size is " + size + " and " + "the text is "+ text + '.')
make_shirt(size='medium', text='creating functions')

# • Playeras Grandes: 

def make_shirt(sizem, sizes, text, size='large'):
    print(" I have a shirt whose size is " + size + " and a " +sizem + '.')
    print(" My brother's shirt is " + sizes)
make_shirt(text='I <3 Python', sizem='medium', sizes='small')

# • Ciudades:

def describe_city(city,country):
    print("\n París está en " + country.title() + '.')
describe_city('city' ,country='francia')

# • Restaurant:
class Restaurant():
    def __init__(self, name, type, open):
        self.restaurant_name=name
        self.cuisine_type=type
        
    def describe_restaurant(self):
        print("\nThe name of the restaurant is " + self.restaurant_name + '.')
        print("The restaurant is of the " + self.cuisine_type + " type" + '.')
        
    def open_restaurant(self):
        print("The restaurant is " + str('open') + '.')

Restaurante=Restaurant('the flavor cellar','cuisine traditional','open')
Restaurante.describe_restaurant()
Restaurante.open_restaurant()

# • Tres restaurantes: 

Restaurante=Restaurant('The Olympus of flavor','cuisine traditional','open')
print("\nRestaurante 1")
print(Restaurante.restaurant_name + '.')
print(Restaurante.cuisine_type + '.')

Restaurante=Restaurant('Rich Delirium','cuisine traditional','open')
print("\nRestaurante 2")
print(Restaurante.restaurant_name + '.')
print(Restaurante.cuisine_type + '.')

Restaurante=Restaurant('Ols','Cuisine traditional','open')
print("\nRestaurante 3")
print(Restaurante.restaurant_name + '.')
print(Restaurante.cuisine_type + '.')
# • Usuarios:
class User():
    def __init__(self, first, last, email, password):
        self.first_name=first
        self.last_name=last
        self.email=email
        self.password=password
        
    def describe_user(self):
        print ("\n•••••••••••••••••••••••••••••"
               "\n••••••••••USER DATA••••••••••"
               "\n•••••••••••••••••••••••••••••"
               "\nYour username is: " + self.first_name + '.'
               +"\nYour user's last name is: " + self.last_name + '.'
               +"\nYour user email is: " + self.email + '.'
               +"\nYoyr user password is: " + self.password + '.')
    def greet_user(self):
        print("-----------------------------------")
        print("-  Welcome, how can we help you?  -")
        print("-----------------------------------")
Usuario=User('Alejandro_08','Fernández','ale08@gmail.com','ipnporsiempre')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Brenda-476','Peña','Brenda476@hotmail.com','amolosgatitos')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Andrés00012','Fernández','andres987.789@live.com.mx','cruzazuleño')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Carlos.4_78','Gordillo','soyelpaps_201@hotmail.es','CarlosolraC')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('0_Alan_784','Hernandez','alanwuero147@gmail.com','Tigrevolador')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Lilia_147852','Gonzales','bebeshita_2000@gmail.com','micontraesesta')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Paolaaa_356','Ortega','secductoraalmil555@hotmail.es','aloap159ILOVE')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('Marian78_87','Lopez','gghhjjkk_maria@gmail.com','Ratoncitoalcuadrado')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('FernandoXX_chela','Dosamantes','megalodon_1999@hotmail.com.mx','HoLa_PiCacHu')
Usuario.describe_user()
Usuario.greet_user()

Usuario=User('BellakitaLiz2000','Figueroa','Lizfigue3256@gmail.com','locAAportuamoRR')
Usuario.describe_user()
Usuario.greet_user()