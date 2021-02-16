# anime-bot-discord

:octocat:	**Explications en Français**

**you will find the explanations in English below**

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
     
- Lancer le script avec python, il vous donne une url, vous devez la copier coller dans votre navigateur, ensuite vous cliquez sur "Allow" et vous serez redirigé sur l'url que vous avez entré dans les paramètres de votre client API. Dans l'url de cette page vous verrez une variable en GET ?code='...'. Copier ce code et coller le dans l'input dans votre terminal. Une fois ceci fait, dans votre terminal vous devriez voir votre accès_token, le refresh_token et quand l'accès token expire. L'accès token et le refresh_token sont sauvegardés dans leur fichier respectif : mal_token.txt et refresh_token.txt. Ne les toucher pas


Partie 2 : 
**Si vous avez déjà récupérer votre accès_token et refresh_token, le fichier mal_auth.py ne vous sera pas utile :**

- Installer les modules nécessaires : 

      pip install discord

      pip install aiohttp

- Mettez votre access_token dans mal_token.txt et votre refresh_token dans refresh_token.txt (on parle bien du token de l'api et non celui de votre bot discord). Si vous avez suivi la partie 1 vous n'avez pas besoin de faire cette étape car les fichiers contiennent déjà votre mal_token et votre refresh_token
- Remplacer 'YOUR_TOKEN' par le token de votre **bot discord** dans le code (ligne 8)
- Lancer le bot avec python 

Sur Windows : 

    python bot.py 

Sur Linux :  

    python3 bot.py

**Remarque : vous devez changer vous même l'accès token lorsque celui sera expiré, un système qui le change automatiquement lorsque celui-ci sera expiré sera probablement fait dans le futur. Pour changer votre token lorsqu'il est expiré c'est la : [MAL-Token](https://myanimelist.net/apiconfig/references/authorization#refreshing-an-access-token)**

:octocat: **Explanations in English**

This bot will allow you to have information on an anime with the command !anime> and later on manga. Information about anime are retrieved with queries on the api of myanimelist 

![Image of command !anime](https://i.ibb.co/ZcdK9M3/bot.png)

**Installation :** 

Prerequisites :
             
             -to have a discord bot and its token
            
            - have created a client to access the myanimelist api and retrieve the client_id and secret_client
            
Part 1 :
**If you haven't got your access_token and refresh_token from the api you have to follow this part, if you have already done so you can skip this step and go to part 2:**

- Insert your client_id and secret_client in the code of the script mal_auth.py (line 5 and 6)
- Install the requests module: 

       pip install requests
     
- Launch the script with python, it gives you a url, you have to copy and paste it in your browser, then you click on "Allow" and you will be redirected to the url you entered in your API client settings. In the url of this page you will see a GET variable ?code='...'. Copy this code and paste it into the input in your terminal. Once this is done, in your terminal you should see your access_token, the refresh_token and when the token access expires. The token access and the refresh_token are saved in their respective files: mal_token.txt and refresh_token.txt. Do not touch them


Part 2 : 
**If you have already recovered your access_token and refresh_token, the file mal_auth.py won't be useful :**

- Install the necessary modules : 

      pip install discord

      pip install aiohttp

- Put your access_token in mal_token.txt and your refresh_token in refresh_token.txt (we are talking about the api token and not your discord bot token). If you followed part 1 you don't need to do this step because the files already contain your mal_token and your refresh_token
- Replace 'YOUR_TOKEN' by the token of your **discordant boot** in the code (line 8)
- Launch the bot with python 

On Windows : 

    python bot.py 

On Linux :  

    python3 bot.py

**Note: you have to change the token access yourself when it expires, a system that changes it automatically when it expires will probably be done in the future. To change your token when it's expired it's the : [MAL-Token](https://myanimelist.net/apiconfig/references/authorization#refreshing-an-access-token)**

Translated with www.DeepL.com/Translator (free version)
                      
