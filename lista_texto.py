

lista_texto = ['Hola:', '¡Cómo!', 'está-', 'oK_', '¡Hola!', 'holA!', '¿Cómo?', 'OK!', 'HOLA', 'OK']

def main(lista_texto):
    import re
    from operator import itemgetter
    
    def limpiar_lista_texto(lista_texto):
        n_lista_texto = []    
        new_lista_texto = []    
        
        for k in lista_texto:
            word = re.sub(r'[?|$|.|!]',r'',k)          
            n_lista_texto += [word]
        
        for i in n_lista_texto:
            word = re.sub(r'[^a-zA-Z0-9áéíóú ]',r'',i)
            new_lista_texto += [word]    

        lista_texto = new_lista_texto    
    
        return lista_texto

    def poner_texto_minuscula(lista_texto):
        new_lista_texto = []
        for k in lista_texto:
            word = k.lower()
            new_lista_texto += [word]

        lista_texto = new_lista_texto

        return lista_texto
    
    def contar_palabras_repetidas(lista_texto):
        lista_palabra = []
        new_lista_texto = []
        
        for i in lista_texto:
            word1 = i

            counter = 0
            for j in lista_texto:
                word2 = j

                if word1 == word2:
                    counter = counter + 1
                    lista_palabra = [word1, counter]

            if not lista_palabra in new_lista_texto:
                new_lista_texto += [lista_palabra]

        lista_texto = new_lista_texto
    
        return lista_texto

    def odernar_descendente_lista (lista_texto):
        new_list = []
        new_list = sorted(lista_texto, key=itemgetter(1), reverse=True)

        lista_texto = new_list

        return lista_texto
    
    def slice_ultimos_20valores(lista_texto):
        new_list =lista_texto [-20::]
        lista_texto = new_list
        return lista_texto

    lista_texto = limpiar_lista_texto(lista_texto)
    lista_texto = poner_texto_minuscula(lista_texto)
    lista_texto = contar_palabras_repetidas(lista_texto)
    lista_texto = odernar_descendente_lista(lista_texto)
    lista_texto = slice_ultimos_20valores(lista_texto)

    lista_conteo = lista_texto

    return lista_conteo

print(main(lista_texto))