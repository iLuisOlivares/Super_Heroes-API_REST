# Super_Heroes-API_REST

API REST que contiene informacion de los principales super heroes y villanos de los universo de Comics de DC y Marvel.

## Run Locally

<hr>
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

In localhost: http://127.0.0.1:8000/ API_REFERENCE

#### Get all Heroes

```http
  GET /api/superheroes
```

#### Post a Hero

```http
  POST /api/superheroes/
```

#### Get, Put and Delete a Hero

```http
  GET | PUT | DELETE  /api/superheroes/${id}
```

| Parameter | Type     | Description                            |
| :-------- | :------- | :------------------------------------- |
| `id`      | `string` | **Required**. Id of superHero to fetch |

## Authors

- [@iLuisOlivares](https://www.github.com/iluisolivares)
