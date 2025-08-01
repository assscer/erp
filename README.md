# ERP System — микросервисный каркас на Django + Vue + Docker

## Описание

ERP-система на микросервисной архитектуре, где каждый сервис реализует свою модель данных и наполняет универсальный табличный компонент.  
Сделано с использованием:

- Django + Django REST Framework
- PostgreSQL
- Vue 3 + Vite
- Docker / Docker Compose

---

## Быстрый запуск

### Требования:

- Docker + Docker Compose

### Команды:

1. **Склонируйте репозиторий:**

```bash
git clone https://github.com/assscer/erp.git
cd erp
docker compose up --build


Frontend UI: http://localhost:5173

Backend API: http://localhost:8000/api/

Products API: http://localhost:8000/api/products/

Orders API: http://localhost:8000/api/orders/


Перейдите на http://localhost:5173

Вкладка Products — таблица с продуктами

Вкладка Orders — таблица с заказами

Таблица автоматически формируется из данных API