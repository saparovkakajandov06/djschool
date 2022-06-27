# Загрузить из Docker Hub образ nginx
FROM nginx

# Удаляем конфигурацию по умолчанию
RUN rm /etc/nginx/conf.d/default.conf
# Скопируйте наш nginx conf в nginx conf.d
COPY nginx.conf /etc/nginx/conf.d
