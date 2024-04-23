import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Dashboards', layout='wide')
df = pd.read_csv("data/processed/df_pronto.csv")

print(df)