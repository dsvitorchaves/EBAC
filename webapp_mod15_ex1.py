import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configurando largura máxima para exibição das colunas no DataFrame
st.set_option('deprecation.showPyplotGlobalUse', False)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)  # Arredondando para 2 casas decimais

# Função para atribuir o nível à pontuação
def get_nivel_pontuacao(pontuacao):
    if pontuacao <= 30:
        return 'Leve'
    elif pontuacao <= 70:
        return 'Moderado'
    else:
        return 'Grave'

# Gerando um conjunto de dados fictício
np.random.seed(42)
data = {
    'Idade': np.random.randint(18, 70, 300),
    'Gênero': np.random.choice(['Masculino', 'Feminino'], 300),
    'Problema Mental': np.random.choice(['Depressão', 'Ansiedade', 'Esquizofrenia', 'Bipolaridade'], 300),
    'Pontuação Escala': np.random.randint(0, 100, 300)
}
df = pd.DataFrame(data)

# Adicionando a coluna "Nível" ao DataFrame
df['Nível'] = df['Pontuação Escala'].apply(get_nivel_pontuacao)

# Configurando título e subtítulo do aplicativo
st.title('Análise de Dados - Clínica Psiquiátrica')
st.subheader('Informações sobre problemas mentais e pacientes')

# Exibindo os dados no Streamlit
st.write('## Dados dos Pacientes')
st.dataframe(df)

# Gerando gráficos
st.write('## Gráficos')
st.write('### Distribuição de Idade')
plt.figure(figsize=(8, 6))
sns.histplot(df['Idade'], bins=20, kde=True)
st.pyplot(plt)

st.write('### Distribuição de Pontuação na Escala')
plt.figure(figsize=(8, 6))
sns.histplot(df['Pontuação Escala'], bins=20, kde=True)
st.pyplot(plt)

st.write('### Contagem de Problemas Mentais')
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Problema Mental')
st.pyplot(plt)

# Gráfico de Barras: Predominância de Gênero por Problema Mental
st.write('### Predominância de Gênero por Problema Mental')
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Problema Mental', hue='Gênero')
plt.legend(title='Gênero')
st.pyplot(plt)

# Análise estatística
st.write('## Análise Estatística')
st.write('### Resumo Estatístico dos Dados')
st.write(df.describe().rename(index={'count': 'Contagem', 'mean': 'Média', 'std': 'Desvio Padrão'}).round(2))

# Insights sobre o Resumo Estatístico
st.write('### Insights sobre o Resumo Estatístico')
st.write('- **Contagem (Contagem):** Quantidade total de pacientes em cada coluna.')
st.write('- **Média (Média):** Valor médio dos dados para cada coluna. Representa o centro dos dados.')
st.write('- **Desvio Padrão (Desvio Padrão):** Medida de dispersão que indica o quanto os dados se afastam da média. Quanto maior o valor, maior a dispersão dos dados.')

st.write('### Média de Pontuação por Problema Mental')
mean_scores = df.groupby('Problema Mental')['Pontuação Escala'].mean().round(2)
st.write(mean_scores)

# Filtro por gênero
st.write('## Filtro por Gênero')
selected_gender = st.selectbox('Selecione o gênero:', df['Gênero'].unique())
filtered_data_gender = df[df['Gênero'] == selected_gender]
st.write(filtered_data_gender)

# Filtro por problema mental
st.write('## Filtro por Problema Mental')
selected_problem = st.selectbox('Selecione o problema mental:', df['Problema Mental'].unique())
filtered_data_problem = df[df['Problema Mental'] == selected_problem]
st.write(filtered_data_problem)
