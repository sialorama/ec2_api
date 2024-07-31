

## Exécuter et tester l'application FastAPI dans un conteneur Docker:

### Construire l'image Docker :  

```sh
Copier le code
docker build -t my-fastapi-app .
```
  
### Exécutez le conteneur Docker :  
  
```sh
Copier le code
docker run -p 5000:5000 my-fastapi-app
```
  
### Accédez à votre API :  

Ouvrir lenavigateur web et accédez à http://localhost:5000/docs pour voir la documentation interactive générée par FastAPI.
