# GerenciamentoEscola

GerenciamentoEscola is a project designed for the Object-Oriented Programming course, 
taught by Professor Gabriela Nunes Lopes. The purpose is purely educational and does not 
involve any profit-making effort. Any reproduction is permitted, provided it is not for 
commercial purposes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies:

```bash
pip install python-dotenv
```

```bash
pip install pymongo
```

## Usage of dependencies

```python
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient, errors

# These lines are already in use in this project
```

## Run

You should navigate to the project folder `system` using your terminal of choice.
Then, execute the following command:

```bash
python main.py
```

### First Run
You can use the following login information on the first run:

Aluno:
`Login` joao123
`Senha` senha123

Professor:
`Login` maria123
`Senha` senha456

Diretoria:
`Login` mariana456
`Senha` senha456

Please note that the database is not populated, which means that 
some fields may not be clean or compatible with the functionalities.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Not licensed.