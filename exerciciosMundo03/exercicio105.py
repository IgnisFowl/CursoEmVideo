def notas(*n,sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: 1 ou mais notas.
    :param sit: valor opcional indicando situação do aluno.
    :return: dicionário com várias informações.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média']>7:
            r['situação'] = 'APROVADO'
        elif r['média'] >= 5:
            r['situação'] = 'RECUPERAÇÃO'
        else:
            r['situação'] = 'REPROVADO'
    return r


resp = notas(5.5, 4, 6.5, 9, sit=True)
print(resp)
print()
help(notas)