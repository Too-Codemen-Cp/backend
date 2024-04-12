# Серверная часть сервиса по поиску музейных предметов по картинке

## API документация
[Ссылка]()

## Установка и запуск

1. Убедитесь, что у вас установлен [Docker](https://www.docker.com)
2. Склонируйте репозиторий
    ```shell
   git clone https://github.com/Too-Codemen-Cp/backend
   ```
3. Перейдите в склонированную папку
4. Введите команды
   ```shell
   docker build -t image
   docker run -p 8000:8000 image
    ```
5. Backend запущен на 8000 порту.