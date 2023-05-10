# Super_Heroes-API_REST

API REST que contiene informacion de los principales super heroes y villanos de los universo de Comics de DC y Marvel.

## Run Locally

---

#### 1. Download the project

Clone the project

```bash
  git clone https://github.com/iLuisOlivares/Super_Heroes-API_REST
```

Go to the project directory

```bash
  cd Super_Heroes-API_REST
```

#### 2. Install virtual environment

```bash
  sudo apt install python3-venv
```

Create virtual environment

```bash
  virtualenv -p python3 env
```

Activate virtual environment

```bash
  source env/bin/activate
```

#### 3. Install dependencies

```bash
  pip install -r requirements.txt
```

#### 4. Start the server

```bash
  cd super_hero_API/
```

```bash
  python manage.py runserver
```

Go to for example - http://127.0.0.1:8000/api/superheroes/

## API Reference - Superheroes

---

In localhost: http://127.0.0.1:8000/ API_REFERENCE

### Super Heroes

---

#### Get all Heroes

```http
  GET /api/superheroes
```

#### Post a Hero

```http
  POST /api/superheroes/
```

#### Get, Put and Delete a Hero by id

```http
  GET | PUT | DELETE  /api/superheroes/${id}
```

| Parameter | Type  | Description                            |
| :-------- | :---- | :------------------------------------- |
| `id`      | `int` | **Required**. Id of Superhero to fetch |

#### Get, Put and Delete a Hero by name

```http
  GET | PUT | DELETE  /api/superheroes/${name}
```

| Parameter | Type     | Description                              |
| :-------- | :------- | :--------------------------------------- |
| `name`    | `string` | **Required**. Name of Superhero to fetch |

### Super Villain

---

#### Get all Villains

```http
  GET /api/supervillain
```

#### Post a Villain

```http
  POST /api/supervillain/
```

#### Get, Put and Delete a Villain by id

```http
  GET | PUT | DELETE  /api/supervillain/${id}
```

| Parameter | Type  | Description                               |
| :-------- | :---- | :---------------------------------------- |
| `id`      | `int` | **Required**. Id of Supervillain to fetch |

#### Get, Put and Delete a Vilain by name

```http
  GET | PUT | DELETE  /api/supervillain/${name}
```

| Parameter | Type     | Description                                 |
| :-------- | :------- | :------------------------------------------ |
| `name`    | `string` | **Required**. Name of Supervillain to fetch |

### Locations

---

#### Get all Locations

```http
  GET /api/locations
```

#### Post a Location

```http
  POST /api/locations/
```

#### Get, Put and Delete a Location by id

```http
  GET | PUT | DELETE  /api/locations/${id}
```

| Parameter | Type     | Description                           |
| :-------- | :------- | :------------------------------------ |
| `id`      | `string` | **Required**. Id of Location to fetch |

#### Get, Put and Delete a Location by name

```http
  GET | PUT | DELETE  /api/locations/${name}
```

| Parameter | Type     | Description                             |
| :-------- | :------- | :-------------------------------------- |
| `name`    | `string` | **Required**. Name of Location to fetch |

---

##### Se utilizo la libreria retrying para usar el patron retry

## Authors

- [@iLuisOlivares](https://www.github.com/iluisolivares)
