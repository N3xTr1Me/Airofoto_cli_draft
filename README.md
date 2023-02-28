# Airofoto_cli_draft

## Краткое описание:

В данном репозитории представлены наработки по консольному интерфейсу для проекта "Инструмент обработки 3d-моделей аэрофотосъемки".

В директории *commands* представлены типовые команды для взаимодействия с пользователем. Впоследствии именно на их основе формировался CLI.

В директории *v1* представлен первый и самый простой прототип CLI. На данный момент он не имеет особой ценности и подобно типовым командам являлся основой для последующих изменений.

В *v2* расположен консольный интерфейс, способный работать с файлом конфига, а также первая версия структуры данного файла.

В *v3* Представлено возможное решение сериализации CLI для будущих плагинов. В идеале хотелось бы достичь архитектуры, при которой автору плагина для добавления нового функционала в программу достаточно реализовать соответствующий интерфейс. Целью сериализации CLI было избавить авторов плагинов от необходимости прописывать взаимодействие с пользователем и какую-либо логику получения/валидации аргументов для работы своего плагина.

## Шаблон конфиг файла в формате .yml:

src: [Путь до файла] - Путь до файла с исходными данными.

dest: [Путь] - Опциональный путь для сохранения результата программы

commands: [1, 2, 3 ... ] - Список операций, которые необходимо выполнить, каждая операция впоследствии описывается отдельно.

1: *Словарь аргументов* - Описание операции.

2: *Словарь аргументов*

...

## TODO

- Реализовать DTO-класс, для хранения и транспортировки данных, полученных CLI, со встроенной валидацией данных на смену обычному словарю.

- Более формально оформить логику CLI и констант, от которых она зависит.

## P.S. В данном репозитории представлены наброски и заготовки. Целью было скорее представить общие идеи, а не показать конкретную реализацию. Все представленые в репозитории решения могут и вероятно будут меняться и улучшаться в процессе дальнейшей разработки. 
