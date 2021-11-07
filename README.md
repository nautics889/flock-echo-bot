# Echo bot for Flock service.
An example of Flock application represented by simple echo bot.

Built with [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/). 
At present the bot can handle only two events received from Flock: `"app.install"` and `"chat.receiveMessage"`.

After Flock user installs the bot he/she receive an initial message after small delay and this means a chat has been started:
![initial message](https://i.imgur.com/l0Ku2G8.png)
Then the bot behaves like an ordinarty echo-bot:
![demonstration of repeating](https://i.imgur.com/drANe47.png)

**Important notice**: when creating you own application, do not forget to set according flag on management dashboard (sure, in if the application supposed to be bot):
![switch this button](https://i.imgur.com/hpPtJT5.png)

Good luck with your development!
