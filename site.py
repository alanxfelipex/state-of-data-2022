import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

modelo = joblib.load('classificar_satisfacao.pkl')

def definir_funcionario(dicionario, valor, lista):
    chaves = list(dicionario.keys())
    for chave in chaves:
        if dicionario[chave] == valor:
            lista.append(1)
        else:
            lista.append(0)
    return lista
st.set_page_config(page_title='Calculadora de Satisfação')

with st.container():
    st.subheader('Calculadora de Satisfação')
    #st.title("Titulo")
    st.write("Esta é uma ferramenta criada usando os dados do State of Data de 2022 que serve para verificar a satisfação dos colaboradores na Área de Dados")
    st.write("Criado por [Alan Felipe](https://www.linkedin.com/in/alanxfelipe/)")

with st.container():
    st.write('---')

with st.container():

    # Idade
    dicionario_idade = {'Entre 17 e 21': 'idade_17-21',
                        'Entre 22 e 24': 'idade_22-24',
                        'Entre 25 e 29': 'idade_25-29',
                        'Entre 30 e 34': 'idade_30-34',
                        'Entre 35 e 39': 'idade_35-39',
                        'Entre 40 e 44': 'idade_40-44',
                        'Entre 45 e 49': 'idade_45-49',
                        'Entre 50 e 54': 'idade_50-54',
                        'Mais de 55': 'idade_55+'}

    faixa_idade = st.selectbox('Faixa de idade', list(dicionario_idade.keys()))
    valor_idade = dicionario_idade[faixa_idade]

    # Sexo
    dicionario_sexo = {'Feminino': 'genero_Feminino',
                       'Masculino': 'genero_Masculino'}
    faixa_sexo = st.selectbox('Sexo', list(dicionario_sexo.keys()))
    valor_sexo = dicionario_sexo[faixa_sexo]

    # Cor
    dicionario_cor = {'Amarela': 'cor_Amarela',
                      'Branca': 'cor_Branca',
                      'Indigena': 'cor_Indígena',
                      'Parda': 'cor_Parda',
                      'Preta': 'cor_Preta',
                      'Outra': 'cor_Outra'}
    faixa_cor = st.selectbox('Cor/Raça/Etnia', list(dicionario_cor.keys()))
    valor_cor = dicionario_cor[faixa_cor]

    # Modelo de Trabalho
    dicionario_modelo = {'Modelo 100% Presencial': 'modelo_de_trabalho_Modelo 100% presencial',
                         'Modelo 100% Remoto': 'modelo_de_trabalho_Modelo 100% remoto',
                         'Hibrido com dias Fixos': 'modelo_de_trabalho_Modelo híbrido com dias fixos de trabalho presencial',
                         'Hibrido Flexível': 'modelo_de_trabalho_Modelo híbrido flexível (o funcionário tem liberdade para escolher quando estar no escritório presencialmente)',
                         }
    faixa_modelo = st.selectbox('Modelo de Trabalho', list(dicionario_modelo.keys()))
    valor_modelo = dicionario_modelo[faixa_modelo]

    # Ensino
    dicionario_ensino = {'Não Tenho Graduação Formal': 'ensino_Não tenho graduação formal',
                         'Estudante de Graduação': 'ensino_Estudante de Graduação',
                         'Graduação/Bacharelado': 'ensino_Graduação/Bacharelado',
                         'Pós-Graduação': 'ensino_Pós-graduação',
                         'Mestrado': 'ensino_Mestrado',
                         'Doutorado/Phd': 'ensino_Doutorado ou Phd'
                         }

    faixa_ensino = st.selectbox('Nivel de Ensino', list(dicionario_ensino.keys()))
    valor_ensino = dicionario_ensino[faixa_ensino]

    # Número de Funcionários

    dicionario_funcionarios = {'Entre 1 a 5': 'numero_de_funcionarios_de 1 a 5',
                               'Entre 6 e 10': 'numero_de_funcionarios_de 6 a 10',
                               'Entre 11 e 50': 'numero_de_funcionarios_de 11 a 50',
                               'Entre 51 e 100': 'numero_de_funcionarios_de 51 a 100',
                               'Entre 101 a 500': 'numero_de_funcionarios_de 101 a 500',
                               'Entre 501 a 1000': 'numero_de_funcionarios_de 501 a 1.000',
                               'Entre 1001 a 3000': 'numero_de_funcionarios_de 1.001 a 3.000',
                               'Acima de 3000': 'numero_de_funcionarios_Acima de 3.000'}

    faixa_funcionario = st.selectbox('Total de Funcionários', list(dicionario_funcionarios.keys()))
    valor_funcionario = dicionario_funcionarios[faixa_funcionario]

    # Equipe de Dados

    dicionario_equipe = {
        "Não temos equipe": 'tamanho_equipe_Ainda não temos pessoas atuando com dados na empresa',
        'Entre 1 e 3 pessoas': 'tamanho_equipe_1 - 3',
        'Entre 4 e 10 pessoas': 'tamanho_equipe_4 - 10',
        'Entre 11 e 30 pessoas': 'tamanho_equipe_11 - 20',
        'Entre 21 e 50 pessoas': 'tamanho_equipe_21 - 50',
        'Entre 51 e 100 pessoas': 'tamanho_equipe_51 - 100',
        'Entre 101 e 300 pessoas': 'tamanho_equipe_101 - 300',
        'Acima de 300 pessoas': 'tamanho_equipe_Acima de 300 pessoas'
    }

    faixa_equipe = st.selectbox('Tamanho da equipe de dados', list(dicionario_equipe.keys()))
    valor_equipe = dicionario_equipe[faixa_equipe]

    # Salário

    dicionario_salario = {'Menos de R$ 1000/mês': 'faixa_salario_Menos de R$ 1.000/mês',
                          'Entre R$ 1001/mês a R$ 2000/mês': 'faixa_salario_de R$ 1.001/mês a R$ 2.000/mês',
                          'Entre R$ 2001/mês a R$ 3000/mês': 'faixa_salario_de R$ 2.001/mês a R$ 3.000/mês',
                          'Entre R$ 3001/mês a R$ 4000/mês': 'faixa_salario_de R$ 3.001/mês a R$ 4.000/mês',
                          'Entre R$ 4001/mês a R$ 6000/mês': 'faixa_salario_de R$ 4.001/mês a R$ 6.000/mês',
                          'Entre R$ 6001/mês a R$ 8000/mês': 'faixa_salario_de R$ 6.001/mês a R$ 8.000/mês',
                          'Entre R$ 8001/mês a R$ 12000/mês': 'faixa_salario_de R$ 8.001/mês a R$ 12.000/mês',
                          'Entre R$ 12001/mês a R$ 16000/mês': 'faixa_salario_de R$ 12.001/mês a R$ 16.000/mês',
                          'Entre R$ 16001/mês a R$ 20000/mês': 'faixa_salario_de R$ 16.001/mês a R$ 20.000/mês',
                          'Entre R$ 20001/mês a R$ 25000/mês': 'faixa_salario_de R$ 20.001/mês a R$ 25.000/mês',
                          'Entre R$ 25001/mês a R$ 30000/mês': 'faixa_salario_de R$ 25.001/mês a R$ 30.000/mês',
                          'Entre R$ 30001/mês a R$ 40000/mês': 'faixa_salario_de R$ 30.001/mês a R$ 40.000/mês',
                          'Acima de R$40001/mês': 'faixa_salario_Acima de R$ 40.001/mês'}

    faixa_salario = st.selectbox("Faixa salarial", list(dicionario_salario.keys()))
    valor_salario = dicionario_salario[faixa_salario]

    # Experiencia

    dicionario_experiencia = {
        "Não tenho experiência": 'experiencia_com_dados_Não tenho experiência na área de dados',
        "Menos de 1 ano": 'experiencia_com_dados_Menos de 1 ano',
        "De 1 a 2 anos": 'experiencia_com_dados_de 1 a 2 anos',
        "De 3 a 4 anos": 'experiencia_com_dados_de 3 a 4 anos',
        'De 4 a 6 anos': 'experiencia_com_dados_de 4 a 6 anos',
        'De 7 a 10 Anos': 'experiencia_com_dados_de 7 a 10 anos',
        'Mais de 10 Anos': 'experiencia_com_dados_Mais de 10 anos'
    }

    faixa_experiencia = st.selectbox('Tempo de Experiência', list(dicionario_experiencia.keys()))
    valor_experiencia = dicionario_experiencia[faixa_experiencia]


with st.container():
    calcular = st.button('Verificar Satisfação')
    if calcular:
        funcionario = []
        funcionario = definir_funcionario(dicionario_idade, valor_idade, funcionario)
        funcionario = definir_funcionario(dicionario_sexo, valor_sexo, funcionario)
        funcionario = definir_funcionario(dicionario_cor, valor_cor, funcionario)
        funcionario = definir_funcionario(dicionario_modelo, valor_modelo, funcionario)
        funcionario = definir_funcionario(dicionario_ensino, valor_ensino, funcionario)
        funcionario = definir_funcionario(dicionario_funcionarios, valor_funcionario, funcionario)
        funcionario = definir_funcionario(dicionario_equipe, valor_equipe, funcionario)
        funcionario = definir_funcionario(dicionario_salario, valor_salario, funcionario)
        funcionario = definir_funcionario(dicionario_experiencia, valor_experiencia, funcionario)

        funcionario = np.asarray(funcionario).reshape(1, -1)
        classificacao = modelo.predict(funcionario)
        if classificacao == 1:
            satisfacao = 'A probabilidade é que este colaborador esteja Satisfeito'

        else:
            satisfacao = 'A probabilidade é que este colabrador esteja Insatisfeito'

        st.write(satisfacao)