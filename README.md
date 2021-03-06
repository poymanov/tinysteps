# Tinysteps

Приложение для подбора преподавателей по английскому языку, с фильтрацией по целям изучения, записью к конкретному преподавателю и возможностью оставить заявку на подбор преподавателя.

### Установка

Для работы приложения требуется **Docker** и **Docker Compose**.

Инициализация:
```
make init
```

### Запуск

Запуск:

```
make start
```

После запуска приложение доступно по адресу - [http://localhost:5000/](http://localhost:5000/)

Остановка:
```
make stop
```
Просмотр логов приложения:
```
make logs
```

Удаление файлов приложения, которые создал Docker:
```
make flush
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе [Flask с нуля до 4 проектов в портфолио](https://academy.stepik.org/flask) в [Stepik Academy](https://academy.stepik.org/).
