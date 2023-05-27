# sngy_test_task
Описание проекта
----------
Тестовое задание

----------
# Установка

Установка проекта из репозитория
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone 'git@github.com:valeriy-kirichenko/sngy_test_task.git'
cd sngy_test_task/
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/Scripts/activate
```
3. Установить зависимости:
```bash
cd backend/
python3 -m pip install --upgrade pip
pip install -r requirements.txt
cd ../frontend/
npm install

```
4. Выполнить миграции:
```bash
cd ../backend/
python3 manage.py migrate
```
5. Загрузить тестовые данные:
```bash
python3 manage.py loaddata data.json
```
6. Запустить проект:
```bash
python3 manage.py runserver

# Из другого терминала запустить фронт
cd ../frontend
npm run dev
```
----------
Автор:
----------
* **Кириченко Валерий Михайлович**
GitHub - [valeriy-kirichenko](https://github.com/valeriy-kirichenko)