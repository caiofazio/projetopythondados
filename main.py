from Carro import Carro
import matplotlib.pyplot as plt
import os
import re

def AnoGraph():
    nomes = []
    valores = []
    for carros in CarrosComputados:
        if carros.ano in nomes:
            tempindex = nomes.index(carros.ano)
            valores[tempindex] += 1
        else:
            nomes.append(carros.ano)
            valores.append(1)

    plt.bar(nomes, valores, 0.4, color='red', edgecolor ='green', linewidth = 3)
    plt.title('Ano de lançamento', y = 1.05, backgroundcolor = 'red')
    plt.xlabel('Ano do carro', labelpad= 15, backgroundcolor = 'red')
    plt.show()
def MarcaGraph():
    nomes = []
    valores = []
    for carros in CarrosComputados:
        if carros.marca in nomes:
            tempindex = nomes.index(carros.marca)
            valores[tempindex] += 1
        else:
            nomes.append(carros.marca)
            valores.append(1)

    plt.bar(nomes, valores, 0.4, color='blue', edgecolor='yellow', linewidth=3)
    plt.title('Marca dos carros', y = 1.05, backgroundcolor = 'blue')
    plt.xlabel('Marca', labelpad= 15, backgroundcolor = 'blue')
    plt.show()
def MotorGraph():
    nomes = []
    valores = []
    for carros in CarrosComputados:
        if carros.motor in nomes:
            tempindex = nomes.index(carros.motor)
            valores[tempindex] += 1
        else:
            nomes.append(carros.motor)
            valores.append(1)

    plt.bar(nomes, valores, 0.4, color='pink', edgecolor='black', linewidth=2)
    plt.title('Cilindrada do motor', y = 1.05, backgroundcolor = 'pink')
    plt.xlabel('Cilindrada',labelpad= 15, backgroundcolor = 'pink')
    plt.show()
def CorGraph():
    nomes = []
    valores = []
    for carros in CarrosComputados:
        if carros.cor in nomes:
            tempindex = nomes.index(carros.cor)
            valores[tempindex] += 1
        else:
            nomes.append(carros.cor)
            valores.append(1)

    plt.bar(nomes, valores, 0.4, color='cyan', edgecolor='red', linewidth=2)
    plt.title('Cor dos carros', y = 1.05, backgroundcolor = 'cyan')
    plt.xlabel('Cor',labelpad= 15, backgroundcolor = 'cyan')
    plt.show()
def TransmissaoGraph():
    nomes = []
    valores = []
    for carros in CarrosComputados:
        if carros.transmissao in nomes:
            tempindex = nomes.index(carros.transmissao)
            valores[tempindex] += 1
        else:
            nomes.append(carros.transmissao)
            valores.append(1)
    plt.bar(nomes, valores, 0.4, color='black', edgecolor='cyan', linewidth=2)
    plt.title('Tipo de transmissao', y = 1.05)
    plt.xlabel('Transmissao',labelpad= 15)
    plt.show()



def list_files(files):

    for entry in files:
        if(entry.endswith('.txt')):
            print(entry)

def compute_file(file):
    tempCarro = Carro()
    f = open(file, "r", encoding=('utf-8'))
    text = f.read().title()
    f.close();
    marca = re.findall("Chevrolet|Jeep|Bmw|RENAULT|Honda|Toyota|Fiat|Hyundai|Mitsubishi", text, flags=re.IGNORECASE)
    manual = re.findall("Manual", text, flags=re.IGNORECASE)
    transmissao = "";
    ano = "";
    cor = "";
    motor = "";
    if(manual):
        transmissao = "Manual";
    else:
        transmissao = "Automatica";
    text1 = text.splitlines()
    index = 0;
    FoundAno = False;
    FoundCor = False;
    FoundMotor = False;
    for index, lineString in enumerate(text1): #Pegar Ano e Cor
        if not(FoundAno):
            testAno = re.findall("^Ano$", lineString, flags=re.IGNORECASE)
        if not(FoundCor):
            testCor = re.findall("^Cor$", lineString, flags=re.IGNORECASE)
        if not(FoundMotor):
            testMotor = re.findall("Motor$", lineString, flags=re.IGNORECASE)
            testMotor1 = re.findall("Motor:+", lineString, flags=re.IGNORECASE)

        if (testAno):
            ano = text1[index + 1]
            FoundAno = True;
            testAno = []
            if (FoundCor and FoundMotor):
                break
        elif(testCor):
            cor = text1[index + 1]
            testCor = []
            FoundCor = True
            if(FoundAno and FoundMotor):
                break
        elif(testMotor):
            motor = text1[index + 1]
            testMotor = []
            FoundMotor = True
            if(FoundAno and FoundCor):
                break
        elif(testMotor1):
            testMotor1 = []
            txt1 = lineString.split(' ')

            for index, lineString in enumerate(txt1):
                testMotor2 = re.findall("^Motor:$", lineString, flags=re.IGNORECASE)

                if (testMotor2):
                    motor = txt1[index + 1]
                    testMotor2 = []
                    break
            if (FoundAno and FoundCor):
                break
    motor = motor.replace(' ', '')
    ano = ano.replace('   ', ' ')
    tempCarro.setInfo(ano, cor, motor, marca[0], transmissao)
    CarrosComputados.append(tempCarro)
    #print(text)



dirfound = False;
while not (dirfound):
    basepath = input("Digite o diretorio dos arquivos de entrada: ")
    basepath = basepath.replace('\\', '/')

    exists = os.path.isdir(basepath)
    if not (exists):
        print("Diretorio não encontrado")
    else:
        #print(os.listdir(basepath))
        dirfound = True;

graphics = {
    'Cor': CorGraph,
    'Marca': MarcaGraph,
    'Transmissao': TransmissaoGraph,
    'Motor': MotorGraph,
    'Ano': AnoGraph,
    }
filesIncluded = False;
computedFiles = 0;
CarrosComputados = [];
filesInDir = os.listdir(basepath);
includedFiles = [];
print("Listando arquivos no diretorio:")
list_files(filesInDir)
while not (filesIncluded):
    file = input("Digite o nome do arquivo para ser computado e F para finalizar ou A para todos os arquivos no diretorio\n")
    if(file == 'A'):
        for entry in filesInDir:
            if(entry.endswith('.txt')):
                compute_file(basepath + "/" + entry)
                print('Computado {}'.format(entry))
            else:
                print('{} não computado, formato inválido'.format(entry))
        filesIncluded = True;

    elif(file == 'F'):
        filesIncluded = True;
    else:
        if(file.endswith('.txt')):
            if file in filesInDir:
                if file not in includedFiles:
                    print('Computado {}'.format(file))
                    compute_file(basepath + "/" + file)
                    includedFiles.append(file)
                    filesInDir.remove(file)
                else:
                    print('Arquivo ja incluso')
            elif file in includedFiles:
                print('Arquivo ja incluso')
            else:
                print('File not found')
        else:
            print('Formato não suportado, por favor selecione um arquivo txt')

userOut = False;
while not (userOut):
    avaliableGraphs = ['Cor', 'Marca', 'Ano', 'Motor', 'Transmissao']
    graphInput = input('Digite o gráfico desejado ou S para sair: \nCor;\nMarca;\nTransmissao;\nAno;\nMotor;\n').title()
    if(graphInput in avaliableGraphs):
        graphics[graphInput]()
    else:
        print('Gráfico não disponível tente novamente')






