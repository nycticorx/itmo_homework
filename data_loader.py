>>> import pandas as pd
>>> FILE_ID = "1hdmmcMi5-30MwvlKdwXb7XeeGYmyJMoK"
>>> file_url = f"https://docs.google.com/spreadsheets/d/{FILE_ID}"
>>> import pandas as pd
>>> FILE_ID = "1JoUNSGst7mIbon9LpFjIeIdpjuVVPpcg"
>>> file_url = f"https://drive.google.com/uc?id={FILE_ID}"
>>> raw_data = pd.read_csv(file_url)
>>> print(raw_data.head(10))
     id      SDI1_1  Dem_St_Age  Dem_St_Sex Dem_St_SityStatus  ...  SDI4_6_Other  SDI4_8 SDI4_9  GWAS Genotek
0  2001         NaN         NaN         2.0               NaN  ...           NaN     NaN    NaN   NaN     NaN
1  2002         NaN         NaN         2.0               NaN  ...           NaN     NaN    NaN   NaN     NaN
2  2003   6/30/1999        21.0         2.0                 2  ...           NaN     NaN    NaN   1.0  XV9529
3  2004   11/7/1999        21.0         2.0                 3  ...           NaN     NaN    NaN   1.0  DZ0262
4  2005   9/23/1999        21.0         2.0                 1  ...           NaN     NaN    NaN   1.0  FQ4293
5  2006         NaN         NaN         2.0               NaN  ...           NaN     NaN    NaN   NaN     NaN
6  2007   6/10/1999        21.0         2.0                 1  ...           NaN   [1,6]    NaN   1.0  HF8896
7  2008   12/9/1999        21.0         2.0                 3  ...           NaN     NaN    NaN   1.0  GT8455
8  2009    6/3/1998        22.0         2.0                 1  ...           NaN     [7]    NaN   1.0  CX0654
9  2010  12/23/1998        22.0         2.0                 1  ...           NaN     NaN    NaN   1.0  ZU0003

[10 rows x 42 columns]
