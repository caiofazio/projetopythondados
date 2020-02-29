class Carro:
    def __init__(self):
        self.ano = "";
        self.cor = "";
        self.motor = "";
        self.marca = "";
        self.transmissao = "";

    def getInfo(self):
        return self;


    def setInfo(self, ano, cor, motor, marca, transmissao):
        self.ano = ano;
        self.cor = cor;
        self.motor = motor;
        self.marca = marca;
        self.transmissao = transmissao;
