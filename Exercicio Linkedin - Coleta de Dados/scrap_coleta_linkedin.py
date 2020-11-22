#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Todas as importações
from selenium import webdriver
from time import sleep
## Parametros, varieaveis, constantes...
URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'


# Execução do código
if __name__ == '__main__':
    driver = webdriver.Chrome()
    
    ##acessar url do linkedin
    driver.get(URL_LINKEDIN_DS)
    
    ##pegar lista de resultados do linkeidn
    resultados = driver.find_elements_by_class_name('result-card')    
    lista_descricoes = []
    
    ##looping para carregamento da pagina e pegar mais de 25
    while True:
        ##loop para coletar descricao das vagas
        for r in resultados[len(lista_descricoes):]:
            r.click()
            sleep(1)
            ##pegar a descricao
            descricao = driver.find_element_by_class_name('description')
            ##anexar o texto a lista
            lista_descricoes.append(descricao.text)
            
        resultados = driver.find_elements_by_class_name('result-card')
        
        print(f'Numero de resultados {len(resultados)}')
        print(f'Numero de itens salvos {len(lista_descricoes)}')
        
        ##criterio de saida do loop
        if len(lista_descricoes) == len(resultados):
            break

    print(lista_descricoes)
    ##salvar doc com as informacoes coletadas
    descricao_salvar = '\n'.join(lista_descricoes)
    with open('todas_descricoes_vagas.txt', 'w') as f:
            f.write(descricao_salvar)
    
    driver.quit()
    
    