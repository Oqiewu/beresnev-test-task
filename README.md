# Тестовое CRUD приложение

## Описание

Это веб-приложение для управления пользователями с возможностью добавления, редактирования и удаления записей. Приложение состоит из двух частей: фронтенда на базе Vue.js/Nuxt.js и бэкенда на FastAPI с использованием базы данных PostgreSQL. Обе части упакованы и разворачиваются через Docker Compose.

### Основные компоненты:

- **Frontend**: Vue.js/Nuxt.js с использованием Composition API и TypeScript
  - Интерфейс для управления пользователями.
  - Компоненты:
    - `UserForm.vue` — форма для добавления/редактирования пользователя.
    - `Modal.vue` — модальное окно для отображения формы или подтверждения удаления.
    - `UserList.vue` — таблица со списком пользователей.
  
- **Backend**: FastAPI, PostgreSQL, SQLAlchemy
  - CRUD API для работы с пользователями (создание, чтение, обновление, удаление).
  - Асинхронные запросы к базе данных для повышения производительности.

## Стек технологий

- **Frontend**:
  - Vue.js (Nuxt.js)
  - Composition API
  - TypeScript
  - HTML/CSS (TailwindCSS для стилизации)
  
- **Backend**:
  - Python (FastAPI)
  - PostgreSQL
  - SQLAlchemy
  - Asyncio

- **Docker**:
  - Docker Compose для контейнеризации сервисов.

## Как запустить проект

### Предварительные требования:

- Установленный Docker и Docker Compose.

### Запуск:

1. Склонируйте проект с GitHub:
 
  ```bash
  git clone 'https://github.com/Oqiewu/beresnev-test-task.git'
  ```

2. Перейдите в корневую директорию проекта:

  ```bash
  cd beresnev-test-task
  ```

3. Запустите проект с помощью Docker Compose из корневой директории проекта:

   ```bash
   docker-compose up --build
   ```

4. Приложение будет доступно по следующим адресам:

    Frontend: http://localhost:3000
    Backend API: http://localhost:8000


## Скриншоты

![Главная страница](/screenshots/Screenshot_1.png)

![Добавление пользователя](/screenshots/Screenshot_2.png)

## API

- **GET** `/api/users` — получить список пользователей.

- **POST** `/api/users` — создать нового пользователя.

- **PUT** `/api/users/{id}` — обновить информацию о пользователе.

- **DELETE** `/api/users/{id}` — удалить пользователя.
