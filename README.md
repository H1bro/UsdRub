"# UsdRub" 

# Клонирование репозитория
git clone https://github.com/H1bro/UsdRub.git .   

# Сборка образа
docker build . -t usdrub:v0.1                     

# Запуск контейнера
docker run -it -p 8080:8080 usdrub:v0.1           # Запуск docker контейнера                 

# Заменить <$USD> на необходимое количество (например 1)
# При переходе по ссылке получаем в ответ json 
http://localhost:8080/api/v1/usd/<$USD>                 

