def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verificar de origem e destino são iguais """
    if origem == destino:
        lista_de_erros['destino'] = 'destino', 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verificar se possue algum digito númerico """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'