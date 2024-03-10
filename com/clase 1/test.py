import numpy as np
import pandas as pd

### LIBRERIAS PARA GRAFICAR
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C://Users//Usuario//aprendizajeautomatico//IntroduccionAprendizajeAutomatico//res.csv', parse_dates=['UTC_date', 'onset_date'])
data.head()