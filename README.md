"# UsdRub" 

git clone https://github.com/H1bro/UsdRub.git .
docker build . -t usdrub:v0.1
docker run -it -p 8080:8080 usdrub:v0.1                 

http://localhost:8080/api/v1/usd/<$USD>                 # Заменить <$USD> на необходимое количество (например 1)

