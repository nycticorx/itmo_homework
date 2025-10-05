# Ввденеие в инжиниринг данных
> Привет! Меня зовут Габдрахманова Эльвина, группа 75-63, направление "Индустриальная биотехнология"
В рамках работы я выбрала данные по психогенетике, которые содержат в себе социально-демографические и биологические данные, полученные во время анкетирования/генотипирования. Данные анонимизированы, содержат числовые и категориальные признаки.
> 
> P.S. мне нравится опечатка в названии, осознанно ее не буду исправлять 

# Структура проекта
<pre>
itmo_homework/
├── data_loader.py          # Основной скрипт для загрузки и отображения данных
├── requirements.txt        # Зависимости Python
├── pyproject.toml          # Полное описание проекта
└── README.md              # Документация проекта 
└── .gitignore              # Исключения для Git </pre>
# Поиск сырых данных
[Датасет](https://drive.google.com/drive/folders/1Nn9C2s_yZyvhX5LKMBCX4IR53z-8D4w9?usp=sharing)  — Данные взяты с моей дипломной работы
# Проект
> Этот проект загружает CSV-данные с Диска и показывает первые 10 строк.
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





### Приведение типов данных
когда будет время надеюсь доделать проект по красоте, простите+поймите ):

<img width="446" height="955" alt="image" src="https://github.com/user-attachments/assets/8e18fdaa-2891-4b02-979f-8daed0b16d0e" />
<img width="465" height="506" alt="image" src="https://github.com/user-attachments/assets/540e5835-a85c-4c46-81bd-38332cf7aa88" />






