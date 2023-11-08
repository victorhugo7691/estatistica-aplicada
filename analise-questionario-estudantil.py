import csv

with open('tabela1.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor) #pular o cabeçalho
    for linha in leitor:
        print(linha)

#https://pythonacademy.com.br/blog/manipulacao-csv-no-python#:~:text=Para%20ler%20um%20arquivo%20CSV,reader%20.&text=Neste%20exemplo%2C%20usamos%20um%20with,fechado%20corretamente%20ap%C3%B3s%20o%20uso.