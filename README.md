# Пробный проект автотестов JBJ
Проект автотестов. На данный момент запускает простые тап тесты в приложении пазлов.

## Требования 
|        | v     |
|--------|-------|
| Python | 3.x   |
|JBJ app | 1.0.129+ Debug|

Для автоматического прохождения тутора необходима дебаг версия. Шаги построенны на
ожидании решеного пазла + тап кнопки "win"


## Запуск
-- При первом скачивании проекта необходимо установить зависимости 
при активированном ВО

```sh
pip install requirements.txt
```

!!! Тесты написаны для Pixel 4a - стабильно работают на нем. Адаптивносность в процессе реализации.
При смене на конекретное устройство заменить ID в global_auto_arg.py - сейчас подтянут автоопределение 
устройство средствами встроенного в airtest adb

-- приложение закрыто, девайс разблокирован 

-- Запустить main\main.py
```sh
py main.py
```

## Отчеты
 
--Тестовые функции запускаются через простой логгер. 
Список упавших и прошедших тестов(функций) формируется в txt файлах в корне проекта
по окончанию

-- По каждому feature пакету выводиться html отчет с визуализаций 
мест тапов и ассертов тестов с описанием в папку html_report в корень проекта -
названия отчетов соответствуют названиям фича-директорий

## Структура и доп инфа

-- Тесты последовательны и созависимы в каждой фиче. 
Отдельные итерации запуска\закрытия приложения реализованы
только на уровне запуска фичи для экономии времени прохождения, 
но эта экономия влечет выскоий уровень атомарности пакетов фичей. 
На данном этапе падения теста в середине фичи с 90% вероятностью 
повлечет падение следующих за ним тестов фича пакета. 

-- Директории фичей собраны по локальному либо функциональному соответстию: 
разделам приложения и смежным с ними фунционалу


## Приоритет работ по проекту автоматики JBJ

1. Написание стартовой фичи для сброса app_data и прохождения туториала (done)
2. Доработка для запуска на разных локальных устройствах из одного проекта
3. Автоматизация подтягивания подключённых устройств (Android - done)
4. Доработки для локального запуска через Appium Server
5. Написание инфраструктуры для установочного тестирования Android на BitBar текущим пулом тестов средствами Appium
6. Реализация возможности подключения iOS (для локального запуска)
7. Реализация возможности подключения iOS (в инфре BitBar)
8. Рефактор структуры фичей под стандарт UnitTest
9. Расширение сьюта тестов 

