# -*- coding: utf-8 -*-
"""webscraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1okNY0Ly_C4MrTC6DO_z6NYeCwkdfshCf
"""

## traeremos data de una pagina WEB.
## metodo para traer informacion de una web para automatizar procesos. COmo GPT,
## hay diferentes formas, optaremos por una simple.
import pandas as pd
##https://www.football-data.co.uk/mmz4281/2425/E0.csv

datos_futbol=pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

datos_futbol

datos_futbol.rename(columns={'fecha':'Fecha','HomeTeam':'Local','AwayTeam':'Visitante','FTHG':'Goles Locales','FTAG':'Visitantes'})

## vamos a cambiar un digito con el siclo FOR:
## estos son los lick a scrapiar:
#https://www.football-data.co.uk/mmz4281/2425/E0.csv
#https://www.football-data.co.uk/mmz4281/2425/E1.csv
#https://www.football-data.co.uk/mmz4281/2425/E2.csv
#https://www.football-data.co.uk/mmz4281/2425/E3.csv
#https://www.football-data.co.uk/mmz4281/2425/EC.csv

# la estructura puede ser: https://www.football-data.co.uk/mmz4281
# la segunda: /2425
# la tercer parte + E0 + .csv
#https://www.football-data.co.uk/mmz4281/2425/E0.csv
'https://www.football-data.co.uk/mmz4281/'+'2425'+'/'+'E0'+'.csv'

# guardamos ya que es igual esta parte.
ruta='https://www.football-data.co.uk/mmz4281/'

##crear una lista con los campeones.
campeones=['E0','E1','E2','E3','EC','EL']
enlaces=[]
for campeon in campeones:
  df_links=pd.read_csv(ruta +'2425' + '/' + campeon +'.csv')
  enlaces.append(df_links)

len(enlaces)

enlaces[-1]