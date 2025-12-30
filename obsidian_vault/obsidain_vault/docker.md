

---

## type: tool  
language: python  
tags: docker, containers, devops, virtualization, backend

## 🧠 Model mentalny (Second Brain)

**Docker = uruchamialne środowisko**, nie maszyna wirtualna.  
Nie "instalujesz aplikacji" → **tworzysz obraz**, z którego uruchamiasz **kontenery**.

> Kontener = proces + izolacja + filesystem

---

## Dlaczego Docker istnieje

Problem:

- „U mnie działa”
    
- Różne wersje Pythona / bibliotek / systemu
    

Rozwiązanie:

- To samo środowisko **lokalnie, na CI i na serwerze**
    
- Deterministyczne buildy
    

---

## Kluczowe pojęcia (nie mylić)

### Obraz (Image)

- **Niemutowalny szablon** (snapshot)
    
- Zbudowany z Dockerfile
    
- Warstwowy (layers)
    

```text
python:3.13-slim
 ├── system
 ├── python
 └── dependencies
```

### Kontener (Container)

- **Uruchomiony obraz**
    
- To realny proces w systemie
    
- Może być startowany / zatrzymywany
    

> Image : Container :: class : instance

---

### Dockerfile

Instrukcja **jak zbudować obraz**.

Minimalny przykład (senior‑level):

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen

COPY . .

CMD ["python", "main.py"]
```

**Co tu się dzieje dokładnie:**

- `FROM` → wybór bazowego filesystemu
    
- `WORKDIR` → ustawia cwd dla kolejnych warstw
    
- `COPY` → kopiuje pliki **do obrazu**, nie do hosta
    
- `RUN` → wykonuje komendę **w czasie budowania** (tworzy warstwę)
    
- `CMD` → domyślna komenda **w czasie uruchomienia kontenera**
    

---

## Docker vs VM (ważne)

|Cecha|Docker|VM|
|---|---|---|
|Kernel|współdzielony|osobny|
|Start|ms–sekundy|minuty|
|Waga|MB|GB|
|Izolacja|procesowa|sprzętowa|

Docker ≠ wirtualna maszyna.

---

## docker compose

**Orkiestracja lokalna** wielu kontenerów.

Przykład (Django + Postgres):

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
```

**Zasada:**

- 1 kontener = 1 odpowiedzialność
    

---

## Sieci i wolumeny (minimum)

### Network

- Każdy `docker compose` tworzy **własną sieć**
    
- Usługi widzą się po nazwach (`db`, `web`)
    

### Volume

- Trwałość danych (np. baza)
    

```yaml
volumes:
  postgres_data:
```

---

## Najczęstsze błędy

- Instalowanie zależności przy każdym starcie kontenera
    
- COPY całego projektu przed install deps (psuje cache)
    
- Mylenie `RUN` z `CMD`
    
- Traktowanie kontenera jak serwera SSH
    

---

## Techniki zapamiętywania

- **Analogia:** Image = blueprint, Container = dom
    
- **Wzorzec:** class / instance
    
- **Mnemonika:**
    
    - BUILD → image
        
    - RUN → container
        

---

## Dokumentacja

- Docker docs: [https://docs.docker.com/](https://docs.docker.com/)
    
- Dockerfile best practices: [https://docs.docker.com/develop/develop-images/dockerfile_best-practices/](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
    
- Compose spec: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
    

---

## Do dalszego rozbicia (kolejne notatki)

- Docker build cache (warstwy)
    
- ENTRYPOINT vs CMD
    
- Multi-stage build
    
- Docker + pytest
    
- Docker w CI (GitHub Actions)

#docker #containers
