# Import necessary libraries
import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime

st.markdown('# Analisando empresas')

st.text_input('Preencha o Ticker Code: ',key ='tickercode',value = 'GOOG')
st.markdown(f'## Ultimas noticias da {st.session_state.tickercode} :')

ticker = st.session_state.tickercode

data = yf.Ticker(ticker)

data_news=pd.DataFrame(data.news)

data_news2 = data_news[['title','publisher','link','relatedTickers']]
st.dataframe(data_news2)

end_date = datetime.now().strftime('%Y-%m-%d')
data_hist = data.history(period='max',start='2019-03-16',end =end_date,interval='5d' )
data_hist = data_hist.reset_index()

st.markdown('# Contrua seu grafico: ')
ey= st.selectbox('Eixo y:',data_hist.columns)
ex = st.selectbox('Eixo x:',data_hist.columns)

st.markdown(f'## Grafico {ey} x {ex}:')
st.line_chart(data_hist,x = ex,y=ey)

print(data_hist)