# Загрузить из Docker Hub образ python
FROM python:3

# Создаем рабочую директорию
WORKDIR /usr/src/app

# Скопировать файл 'requirements.txt' в рабочую директорию
COPY requirements.txt .
# Скопировать файл 'enrtypoint.sh' в рабочую директорию
COPY entrypoint.sh .
# Установить требования
RUN pip install -r requirements.txt
# делаем файл entrypoint.sh исполняемым
RUN chmod +x entrypoint.sh
# Скопировать все что есть в нашу рабочую директорию
COPY . .
# Показываем путь к файлу 'entrypoint.sh'
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]