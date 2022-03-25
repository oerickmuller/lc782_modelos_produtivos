## Criando e ativando o virtualenv

### Windows/Powershell

**Criando**
```powershell
> py -m venv .venv
```

**Ativando**
```powershell
> .\Scripts\bin\Activate.ps1
```

### Linux/macOS

**Criando**
```bash
> python -m venv .venv
```

**Ativando**
```bash
> source .venv/bin/activate
```

## Rodando a aplicação

### Windows/Powershell

```powershell
> $env:FLASK_APP = "my_api"
> $env:FLASK_ENV = "development"
> flask run
```

### Linux / macOS

```bash
> FLASK_APP="my_api" FLASK_ENV="development" flask run
```
