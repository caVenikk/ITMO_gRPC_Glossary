# gRPC Глоссарий

Проект представляет собой сервис для управления глоссарием терминов с использованием gRPC и SQLAlchemy.

## Технологии

- Python 3.11+
- gRPC
- Protocol Buffers
- SQLAlchemy 2.0
- aiosqlite
- Alembic

## Установка

1. Клонируйте репозиторий и перейдите в директорию проекта:

   ```bash
   git clone https://github.com/caVenikk/ITMO_gRPC_Glossary.git
   cd ITMO_gRPC_Glossary
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate # для Linux/macOS
   venv\Scripts\activate # для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install grpcio grpcio-tools protobuf sqlalchemy[asyncio] aiosqlite python-dotenv alembic
   ```

4. Создайте файл .env в корневой директории:

   ```env
   DATABASE_URL=sqlite+aiosqlite:///src/app.db
   DEBUG=True
   ```

   **`Note:`** можно сделать `cp .env.example .env` и заполнить переменные.

## Настройка базы данных

1. Сгенерируйте файлы Protocol Buffers:

   ```bash
   python src/generate_proto.py
   ```

2. Примените миграции базы данных:

   ```bash
   alembic upgrade head
   ```

## Запуск

1. Запустите сервер:

   ```bash
   python src/server.py
   ```

2. В другом терминале запустите тестовые примеры клиента:

   ```bash
   python src/client_examples.py
   ```

## Функциональность

Сервис предоставляет следующие операции:

- Получение всех терминов
- Получение термина по ID
- Поиск терминов по тексту (в названии и определении)
- Создание нового термина
- Обновление существующего термина
- Удаление термина

## Структура проекта

```text
src/
├── proto/
│ ├── **init**.py
│ ├── glossary.proto # Определение Protocol Buffers
│ ├── glossary_pb2.py # Сгенерированный код
│ └── glossary_pb2_grpc.py # Сгенерированный код
├── services/
│ └── glossary_service.py # Реализация сервиса
├── database/
│ ├── models/ # Модели SQLAlchemy
│ ├── alembic/ # Миграции
│ └── session.py # Настройка сессии БД
├── server.py # Запуск сервера
├── client.py # Базовый клиент
└── client_examples.py # Примеры использования
```

## API

### GetAllTerms

Получение всех терминов из глоссария.

### GetTermById

Получение термина по его идентификатору.

### SearchTerms

Поиск терминов по подстроке в названии или определении.

### CreateTerm

Создание нового термина.

### UpdateTerm

Обновление существующего термина.

### DeleteTerm

Удаление термина по идентификатору.

## Разработка

При изменении .proto файла необходимо перегенерировать код:

```bash
python src/generate_proto.py
```

При изменении моделей данных необходимо создать и применить миграции:

```bash
alembic revision --autogenerate -m "Описание изменений"
alembic upgrade head
```
