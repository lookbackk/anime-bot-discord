# anime-bot-discord

:octocat:	**Explications en Français**

Ce bot vous permettra d'avoir des informations sur un anime avec la commande !anime <anime> et plus tard sur des mangas. Les informations sur les animés sont récupérées avec des requêtes sur l'api de myanimelist 

![Image of command !anime](https://i.ibb.co/ZcdK9M3/bot.png)

**Installation :** 

Pré-requis :
             
             -avoir un bot discord et son token
            
            - avoir créer un client pour accèder à l'api de myanimelist et avoir récupérer le client_id et client_secret
            
Partie 1 :
**Si vous n'avez pas récupérer votre accès_token et refresh_token de l'api vous devez suivre cette partie, si cela est déjà fait vous pouvez passer cette étape et vous rendre à la partie 2:**

- Insérer votre client_id et client_secret dans le code du script mal_auth.py (ligne 5 et 6)
- Installer le module requests : 

       pip install requests
     
- Lancer le script avec python, il vous donne une url, vous devez la copier coller dans votre navigateur, ensuite vous cliquez sur "Allow" et vous serez redirigé sur l'url que vous avez entré dans les paramètres de votre client API. Dans l'url de cette page vous verrez une variable en GET ?code='...'. Copier ce code et coller le dans l'input dans votre terminal. Une fois ceci fait, dans votre terminal vous devriez voir votre accès_token, le refresh_token et quand l'accès token expire. L'accès token et le refresh_token sont sauvegardés dans leur fichier respectif : token.txt et refresh_token.txt. Ne les toucher pas


Partie 2 : 
**Si vous avez déjà récupérer votre accès_token et refresh_token, le fichier mal_auth.py ne vous sera pas utile :**

- Installer les modules nécessaires : 

      pip install discord

      pip install aiohttp

- Mettez votre access_token dans token.txt et votre refresh_token dans refresh_token.txt (on parle bien du token de l'api et non celui de votre bot discord
- Remplacer 'YOUR_TOKEN' par le token de votre **bot discord** dans le code (ligne 8)
- Lancer le bot avec python 

Sur Windows : python bot.py 

Sur Linux : python3 bot.py

**Remarque : vous devez changer vous même le token lorsque celui sera expiré, un système qui le change automatiquement lorsque celui-ci sera expiré sera probablement fait dans le futur. Pour changer votre token lorsqu'il est expiré c'est la : [MAL-Token](https://myanimelist.net/apiconfig/references/authorization#refreshing-an-access-token)**

Les explications en anglais arriveront plus tard. 

                      
