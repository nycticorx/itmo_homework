# transform.py
import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Приведение типов, кодирование SNP, переименование колонок
    и базовая очистка данных.
    """

    # Обработка пропусков
    na_vals = ["", "NaN", "nan", "нет данных", "-"]

    # Преобразуем типы
    df = df.replace(na_vals, pd.NA)

    # ЧИСЛА
    int_cols = [
        "id", "Dem_St_Age", "Dem_St_Sex", "Dem_St_SityStatus",
        "Family_amount", "Dem_St_EducationProfile", "Dem_St_EducationDirect",
        "SDI1_11", "SDI2_8", "Fin_level", "SDI2_9",
        "SDI3_4", "SDI4_2", "SDI4_3 сколько раз", "SAS-SV"
    ]
    for col in int_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int32")

    # БУЛЛЫ
    bool_cols = ["SDI1_10", "SDI2_11", "SDI3_6", "SDI3_7", "GWAS"]
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map({"1": True, "0": False}).astype("boolean")

    # ТЕКСТ
    text_cols = [
        "SDI1_7", "SDI2_10", "SDI3_1", "SDI3_2", "SDI3_3", "SDI3_5", "SDI3_9",
        "SDI4_5", "SDI4_5_Other", "SDI4_6", "SDI4_8", "SDI4_9", "Genotek", "V2",
        "174868700", "78171124", "78172260", "18047255", "18047816", "113346955",
        "113803028", "72331923", "72372862", "47409034", "28551665", "19951271",
        "27677041\xa0", "27679916\xa0", "63261329\xa0", "47471478\xa0"
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str)

    # SNP
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
        if col in df.columns:
            df[col] = df[col].map(geno_mapping[col]).astype("Int32")

    # ПЕРЕИМЕНОВАНИЕ КОЛОНОК 
    rename_map = {
        "174868700": "SNP1_174868700",
        "78171124": "SNP2_78171124",
        "78172260": "SNP3_78172260",
        "18047255": "SNP4_18047255",
        "18047816": "SNP5_18047816",
        "113346955": "SNP6_113346955",
        "113803028": "SNP7_113803028",
        "72331923": "SNP8_72331923",
        "72372862": "SNP9_72372862",
        "47409034": "SNP10_47409034",
        "28551665": "SNP11_28551665",
        "19951271": "SNP12_19951271",
        "27677041\xa0": "SNP13_27677041",
        "27679916\xa0": "SNP14_27679916",
        "63261329\xa0": "SNP15_63261329",
        "47471478\xa0": "SNP16_47471478",
        "SDI1_1": "birthday",
        "SDI1_7": "nationality",
        "SDI1_10": "bilingualism",
        "SDI1_11": "bilingualism_level",
        "SDI2_8": "income_level",
        "SDI2_9": "a_full_fledged_family",
        "SDI2_10": "breastfeeding",
        "SDI2_11": "childhood_abuse",
        "SDI3_1": "chronic_disease",
        "SDI3_2": "smoking",
        "SDI3_3": "smoking_level",
        "SDI3_4": "sports_frequency",
        "SDI3_5": "sports_name",
        "SDI3_6": "antibiotic",
        "SDI3_7": "hormonal_therapy",
        "SDI3_9": "family_psychiatric_disease",
        "SDI4_2": "covid19",
        "SDI4_3 сколько раз": "covid19_how_many_times",
        "SDI4_4": "date_of_covid19",
        "SDI4_5": "covid19_symptoms",
        "SDI4_5_Other": "covid19_symptoms_other",
        "SDI4_6": "covid19_degree",
        "SDI4_8": "changes_in_precognitive_disorders",
        "SDI4_9": "covid19_other_problems_other",
    }

    df = df.rename(columns=rename_map)

    print("Трансформация данных завершена.")
    return df
