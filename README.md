"# UsdRub" 

git clone https://github.com/H1bro/UsdRub.git .   # Клонирование репозитория

docker build . -t usdrub:v0.1                     # Создание docker image

docker run -it -p 8080:8080 usdrub:v0.1           # Запуск docker контейнера                 

http://localhost:8080/api/v1/usd/<$USD>                 # Заменить <$USD> на необходимое количество (например 1)

