
def uncensor(txt, vowels):
    
    #para cada vogal substitui '*' pela vogal v
    for v in vowels:
        #substituindo somente a primeira ocorrencia de '*'
        #txt recebe string modificada
        txt = txt.replace('*', v, 1)
	
    return txt
