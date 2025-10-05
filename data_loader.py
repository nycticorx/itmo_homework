import pandas as pd

FILE_ID = "1LtthrtKpMg1cPQEDkKJjglbqGIUDFjYr"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)

print(raw_data.head(10))    # Вывод первых 10 строк;

na_vals = ["", "NaN", "nan", "нет данных", "-"]
df = pd.read_csv(
    file_url,
    dtype=str,
    parse_dates=["SDI1_1"],
    dayfirst=True,
    na_values=na_vals
)

int_cols = [
    "id", "Dem_St_Age", "Dem_St_Sex", "Dem_St_SityStatus",
    "Family_amount", "Dem_St_EducationProfile", "Dem_St_EducationDirect",
    "SDI1_11", "SDI2_8", "Fin_level", "SDI2_9",
    "SDI3_4", "SDI4_2", "SDI4_3 сколько раз", "SAS-SV"
]

for col in int_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int32")

bool_cols = ["SDI1_10", "SDI2_11", "SDI3_6", "SDI3_7", "GWAS"]
for col in bool_cols:
    df[col] = df[col].map({"1": True, "0": False}).astype("boolean")  # Преобразуем строки "1"/"0" в bool, остальные в NaN


text_cols = [
    "SDI1_7", "SDI2_10", "SDI3_1", "SDI3_2", "SDI3_3", "SDI3_5", "SDI3_9",
    "SDI4_5", "SDI4_5_Other", "SDI4_6", "SDI4_8", "SDI4_9", "Genotek", "V2",
    "174868700", "78171124", "78172260", "18047255", "18047816", "113346955",
    "113803028", "72331923", "72372862", "47409034", "28551665", "19951271",
    "27677041\xa0", "27679916\xa0", "63261329\xa0", "47471478\xa0"
]

for col in text_cols:
    df[col] = df[col].astype(str)

geno_cols = [
    "174868700", "78171124", "78172260", "18047255", "18047816", "113346955",
    "113803028", "72331923", "72372862", "47409034", "28551665", "19951271",
    "27677041\xa0", "27679916\xa0", "63261329\xa0", "47471478\xa0"
]
geno_mapping = {
    "174868700": {"AA": 0, "AG": 1, "GG": 2},
    "78171124": {"TT": 0, "CT": 1, "CC": 2},
    "78172260": {"CC": 0, "GC": 1, "GG": 2},
    "18047255": {"GG": 0, "GT": 1, "TT": 2},
    "18047816": {"GG": 0, "GT": 1, "TT": 2},
    "113346955": {"AA": 0, "AG": 1, "GG": 2},
    "113803028": {"AA": 0, "AC": 1, "CC": 2},
    "72331923": {"AA": 0, "AG": 1, "GG": 2},
    "72372862": {"TT": 0, "AG": 1, "GG": 2},
    "47409034": {"AA": 0, "AG": 1, "GG": 2},
    "28551665": {"AA": 0, "AG": 1, "GG": 2},
    "19951271": {"AA": 0, "AG": 1, "GG": 2},
    "27677041\xa0": {"CC": 0, "CT": 1, "TT": 2},
    "27679916\xa0": {"AA": 0, "AG": 1, "GG": 2},
    "63261329\xa0": {"CC": 0, "CT": 1, "TT": 2},
    "47471478\xa0": {"CC": 0, "CT": 1, "TT": 2}
}

for col in geno_cols:
    df[col] = df[col].map(geno_mapping[col]).astype("Int32")
print(df.dtypes)

df.to_parquet("my_project.parquet")
