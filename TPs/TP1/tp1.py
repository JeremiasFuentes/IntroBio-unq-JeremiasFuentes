#   Reto 1: ¿Podés descubrir y anotar el orden en que se ha ejecutado cada operación?
((4+5)*2)/5
# Se ejecuta dandole prioridad a los parentesis, primero 4+5 luego lo multiplica por 2 y por ultimo divide por 5

# RETO II: Creá una variable llamada doble, que sea el doble de la suma entre a y b.
a = 5
b = 2
doble = (a+b)*2

#RETO III: Digamos que el ADN no es más que un mensaje en clave, que debe ser descifrado o interpretado para la síntesis de proteínas.
# El mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G y C.
# Dentro de la célula, el mensaje es transportado por otra molécula, el ARN, muy similar al ADN pero con U en vez de T.
# En este mensaje, cada triplete o grupo de tres letras del ARN se denomina codón, y cada aminoácido de las proteínas está codificado por uno o varios codones.
# Así por ejemplo el codón ‘AUG’ codifica para el aminoácido Metionina , el codón ‘AAA’ para Lisina, el codón ‘CUA’ para Leucina, etc.
# ¿Podrías escribir una cadena de ARN que codifique para el péptido (una cadena corta de aminoácidos) ‘Met-Lis-Lis-Lis-Leu-Leu-Met’ combinando las variables
met = 'AUG'
lis = 'AAA'
leu = 'CUA'
# utilizando operadores matemáticos?
peptido = met + lis + lis + lis + leu + leu + met

#RETO IV:

secuencia = 'TGATAAGAGTACCCAGAATAAAATGAATAACTTTTTAAAGACAAAATCCTCTGTTATAATATTGCTAAAATTATTCAGAGTAATATTGTGGATTAAAGCCACAATAAGATTTATAATCTTAAATGATGGGACTACCATCCTTACTCTCTCCATTTCAAGGCTGACGATAAGGAGACCTGCTTTGCCGAGGAGGTACTACAGTTCTCTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTGGTGGTTTGTGATTTAGTTGATTTTATAGGCTAGTGGGAGAATTTACATTCAAATGTCTAAATCACTTAAAATTTCCCTTTATGGCCTGACAGTAACTTTTTTTTATTCATTTGGGGACAACTATGTCCGTGAGCTTCCATCCAGAGATTATAGTAGTAAATTGTAATTAAAGGATATGATGCACGTGAAATCACTTTGCAATCAT'

def porcentajeDeSecuenciaCG(secuencia):
    cantC = secuencia.count('C')
    cantG = secuencia.count('G')
    porcentaje = (cantG + cantG) / len(secuencia)

#RETO V:
def sorbosParaMaravilla(cadena):
    genNormal = cadena
    genMaravilla = 'GTTTGTGGTTG'
    sorbos = [('C','T'), ('A','G'),('C','A')]
    cantSorbos = 0
    for s in sorbos:
        if genMaravilla in genNormal:
            return cantSorbos
        genNormal = genNormal.replace(s[0], s[1])
    raise Exception("No se pudo convertir en inmortal")

#RETO VI:
#append(),remove(),count(),sort(),reverse()

#RETO VII:
def compararLongitudGenes(gen1,gen2):
    longGen1 = len(gen1)
    longGen2 = len(gen2)
    if longGen1>longGen2:
        print('El primer gen es mas largo')
    elif longGen2>longGen1:
        print('El segundo gen es mas largo')
    else:
        print('Los dos genes son iguales de largos')

#RETO VIII:
def imprimirClones():
    for i in range(0, 20):
        print('¡Somos 2 clones nuevos!')

#RETO IX:
def imprimirClones():
    celulas = 1
    for i in range(0, 20):
        celulas = celulas * 2
        print('¡Somos '+celulas+' clones nuevos!')





