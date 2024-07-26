#HI Guys, today I Will show you how to read CSV with pandas

import pandas as pd
import streamlit as st

# Create a DataFrame from a CSV file

# Print the first 5 rows of the DataFrame

def ler_csv(nome):
    nome += '.csv'
    df = pd.read_csv(nome)
    #print(df)
    return df

students = ler_csv('libraries/students_complete')
schools = ler_csv('libraries/schools_complete')

# Identify students quantities
# df.shape = retorna uma tupla com o numero de linhas e o numero de colunas.

#total de estudantes no DataFrame
total_students = students.shape[0]
print(f'O total de estudante e: {total_students}\n')

#Imprimir o orcamento total
orcamento_total = schools['budget'].sum()
print(f'O orcamento total e: {orcamento_total}\n')

# Media em matematica das notas por escola
media_math = students['math_score'].mean()
print(f'A media de matematica e: {media_math:.2f}\n')

# quantidade de medias por reading score
medias_por_reading = students['reading_score'].mean()
print(f'A media de leitura e: {medias_por_reading:.2f}\n')


# Quantidade de estudantes com matematica acima de 70%
porcentagem_math = students.loc[students['math_score']>70].count()['student_name']
porcentagem_math = porcentagem_math / total_students
porcentagem_math *= 100 
print(f'{porcentagem_math:.2f}% foram aprovados aprovados em matematica:')


# Quantidade de estudantes com reading acima de 70%
porcentagem_reading = students.loc[students['reading_score']>70].count()['student_name']
porcentagem_reading = porcentagem_reading / total_students
porcentagem_reading *= 100
print(f'{porcentagem_reading:.2f}% foram aprovados aprovados em leitura:')

# Unir os dois Dataframes

schools_data_complete = pd.merge(students,schools, how='inner', on=['school_name'],sort=True)


# Verificar a quantidade de estudantes por escola

passing_math_reading_count = schools_data_complete[
    (schools_data_complete['math_score']>= 70) & (schools_data_complete['reading_score'] >= 70)
].count()['student_name']

print(f'Quantidade de aprovados nas duas materias: {passing_math_reading_count}')



# Calcular o numero de estudantes por escola

students_per_school = schools_data_complete['student_name'].count()
#print(f'Quandidade de estudantes: {students_per_school}')

number_of_schools = schools_data_complete['school_name'].nunique()
#print(f'Quantidade de escolas: {number_of_schools}')


# Orcamento medio

schools_data_budget_avg = schools_data_complete['budget'].mean()
print(f'O orcamento medio: {schools_data_budget_avg:.2f}')


# Diferenca entre orcamento e media de matematica

budget_math_diff = schools_data_complete['budget'] - schools_data_complete['math_score']
budget_math_diff_avg = budget_math_diff.mean()
print(f'A diferenca entre orcamento e media de matematica: {budget_math_diff_avg:.2f}')

#Criando resumo de medias

summary_stats = pd.DataFrame({
    'total_estudantes':total_students,
    'orcamento_total':orcamento_total,
    'media_matematica':media_math,
    'media_reading':medias_por_reading,
    'porcentagem_math':porcentagem_math,
    'porcentagem_reading':porcentagem_reading,
    'aprovados_math_reading':passing_math_reading_count,
    'student_per_school':students_per_school
}, index=[0])


print(summary_stats)





# Iniciando com Streamlit

st.title('Análise de dados de estudantes')

st.markdown('# Análise de dados das escolas')

st.markdown('## Reading Score per School')

st.dataframe(schools_data_complete)

st.line_chart(schools_data_complete,x='reading_score',y='budget')


chart = alt.Chart(schools_data_complete).mark_circle().encode(
    x = 'math_score',
    y = 'budget',
    size = 'budget',
    color ='school_name'
)

st.altair_chart(chart, use_container_width=True)