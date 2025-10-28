# Smartphone Addiction & Genetics — Data Analysis Project”

Проект посвящён исследованию взаимосвязи уровня зависимости от смартфона (SAS-SV) с генетическими и демографическими факторами.

<div align="center">

  <img width="1424" height="745" alt="image" src="https://github.com/user-attachments/assets/b0f0c77f-a5bb-45e4-a2f2-9104f113789a" />

</div> 
Используется уникальный датасет, содержащий:

1. анкетные данные респондентов,
2. результаты тестирования по шкале SAS-SV,
3. результаты генотипирования по ряду SNP-маркеров,
4. демографические и поведенческие характеристики (курение, пол и др.).

Проект выполнен в рамках учебного курса по инженерии данных, с целью обучиться и продемонстрировать навыкам:
- предобработки данных,
- проведения EDA (Exploratory Data Analysis),
- визуализации взаимосвязей,
- формирования выводов и гипотез для дальнейшего анализа.

# Структура проекта

<pre>
itmo_homework/
├── README.md               # Основная документация проекта
├── .gitignore              # Исключения для Git
├── pyproject.toml          # Конфигурация проекта и зависимости
├── requirements.txt        # Зависимости Python
├── api_reader.py           # Основной скрипт для работы с API
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Функции для загрузки данных
│   └── write_to_db.py      # Функции для записи в БД
├── notebooks/
    └── eda.ipynb           # Ноутбук для анализа данных </pre>


# Описание датасета
[Датасет](https://drive.google.com/drive/folders/1Nn9C2s_yZyvhX5LKMBCX4IR53z-8D4w9?usp=sharing) 

<p align="center">
  <table align="center">
    <tr>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/62248523-f9b8-41db-bb6c-701dadee4594" width="400"/>
      </td>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/73c9354c-1a8b-4328-aade-fd0a90430615" width="400"/>
      </td>
    </tr>
  </table>
</p>


# Функциональность
1. Загрузка и очистка данных
2. Анализ распределений признаков
3. Визуализация различий по полу, курению и другим факторам
4. Корреляционный анализ признаков
5. Первичные выводы о связи генотипов и уровня зависимости
6. Дополнительно проведена обработка API

# Используемые технологии
| Категория     | Инструменты                         |
| ------------- | ----------------------------------- |
| Язык          | Python 3.10+                        |
| Анализ данных | pandas, numpy                       |
| Визуализация  | matplotlib, seaborn, plotly.express |
| Репозиторий   | GitHub                              |
| Среда         | Jupyter Notebook / VS Code          |


<details> <summary>  <b> Первичные шаги по работе с датасетом</b> </summary>
  
## Создание виртуального окружения
<pre>conda create -n my_env python=3.13 pip
conda activate my_env </pre>
  <details>
  <summary>Пояснения:</summary>
    
> -n — «создай окружение с именем…»
> 
> pip — пакетный менеджер для установки библиотек
  </details> 

      
## Установка библиотек
<pre>pip install poetry
poetry new my_project </pre>
<details>
  <summary>Пояснения:</summary>
    
  > poetry — инструмент для управления проектами и зависимостями, с его помощью можно создавать проект и фиксировать библиотеки.
    
  > Фиксировать библиотеки — это значит запомнить точные версии всех библиотек, которые использует проект, чтобы потом его можно было воспроизвести на другом компьютере или через несколько месяцев.
>>
   </details> 
   
> Переходим в папку с окружением:
<pre>cd my_project </pre> 
> Добавялем библиотеки в проект 
<pre>poetry add jupyterlab pandas matplotlib wget
poetry install --no-root</pre> 
<details>
  <summary>Пояснения:</summary>
  
  > jupyterlab — для запуска Jupyter-ноутбуков
  >   
  > pandas — работа с таблицами CSV/Excel
  > 
  > matplotlib — визуализация данных (графики)
  >
  > wget — скачивание файлов через Python

</details> 

## Скрипт выгрузки данных с Диска
<pre>python data_loader.py</pre> 
<details>
  <summary>Скрипт делает 3 вещи:</summary>

  
  > Формирует ссылку на файл в Google Drive.
  
  > Скачивает файл и превращает его в таблицу Python (DataFrame).

  > Показывает первые строки для проверки.
</details> 

## Результат выгрузки данных:

<img width="1387" height="392" alt="image" src="https://github.com/user-attachments/assets/e4651ed6-6699-4de5-87fb-ebb68a3b53d5" />
 </details>




## Описание переменных датасета

<div align="center">
  
| **Название признака** | **Тип данных** | **Описание** |
|:----------------------:|:--------------:|:-------------:|
| `id` | Int32 | Уникальный идентификатор респондента |
| `birthday` | object | Дата рождения |
| `Dem_St_Age` | Int32 | Возраст |
| `Dem_St_Sex` | Int32 | Пол (1 — муж., 2 — жен.) |
| `Dem_St_SityStatus` | Int32 | Тип населённого пункта (город / посёлок / село) |
| `Family_amount` | Int32 | Количество членов семьи |
| `Dem_St_EducationProfile` | Int32 | Профиль образования |
| `Dem_St_EducationDirect` | Int32 | Направление образования |
| `nationality` | object | Национальность |
| `bilingualism` | boolean | Наличие двуязычия |
| `bilingualism_level` | Int32 | Уровень владения вторым языком |
| `income_level` | Int32 | Уровень дохода |
| `Fin_level` | Int32 | Финансовое благополучие семьи |
| `a_full_fledged_family` | Int32 | Полная семья (1 — да, 0 — нет) |
| `breastfeeding` | object | Грудное вскармливание |
| `childhood_abuse` | boolean | Наличие насилия в детстве |
| `chronic_disease` | object | Хронические заболевания |
| `smoking` | object | Статус курения |
| `smoking_level` | object | Интенсивность курения |
| `sports_frequency` | Int32 | Частота занятий спортом |
| `sports_name` | object | Вид спорта |
| `antibiotic` | boolean | Приём антибиотиков |
| `hormonal_therapy` | boolean | Приём гормональных препаратов |
| `family_psychiatric_disease` | object | Наличие психических заболеваний в семье |
| `covid19` | Int32 | Переносил ли COVID-19 |
| `covid19_how_many_times` | Int32 | Количество случаев COVID-19 |
| `covid19_symptoms` | object | Симптомы при COVID-19 |
| `covid19_symptoms_other` | object | Другие симптомы COVID-19 |
| `covid19_degree` | object | Тяжесть протекания |
| `changes_in_precognitive_disorders` | object | Изменения когнитивных функций после COVID |
| `covid19_other_problems_other` | object | Прочие последствия COVID-19 |
| `GWAS` | boolean | Участие в исследовании GWAS |
| `Genotek` | object | Участие в проекте Genotek |
| `SAS-SV` | Int32 | Баллы по шкале зависимости от смартфона |
| `V2` | object | id генотипирования |
| `SNP1_174868700` – `SNP16_47471478` | Int32 | Генотипы по SNP-маркерам (0, 1, 2) |

</div>

<details> <summary>screenshots: </summary> 
  
<img width="508" height="935" alt="image" src="https://github.com/user-attachments/assets/f4464343-cc70-4281-98ba-3df175604209"> <img width="505" height="955" alt="image" src="https://github.com/user-attachments/assets/375068ec-10ea-4a0d-8ca1-426cb07a6c1a"> <img width="499" height="244" alt="image" src="https://github.com/user-attachments/assets/688a0b0a-557e-4495-ace9-71c179c853cd" />
</details> 

## Выводы по EDA
https://nbviewer.org/github/nycticorx/itmo_homework/blob/main/notebooks/eda.ipynb

1) Нет связи между большинством анализируемых социо-демографических факторов и зависимостью от смартфона 
2) Обнаружены значимые различия в зависимости от смартфона по гендерному признаку
3) Выявлена этнически-специфичная ассоциация полиморфизма rs4680 гена COMT с зависимостью от смартфона: носители генотипа AA среди башкир демонстрируют большую зависимость, при отсутствии подобной связи у русских и татар.






