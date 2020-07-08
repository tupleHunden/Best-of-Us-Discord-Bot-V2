
# Best of Us Discord Bot V2

This is a simple moderation and command feature bot Discord server "Best of Us".

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing
Ensure you have Python 3.6+ Installed
```
python3 --version
```

Clone the repo to your local machine
```
git clone git@github.com:tupleHunden/Best-of-Us-Discord-Bot-V2.git
```
Go into the new directory
```
cd Best-of-Us-Discord-Bot-V2
```

Install the Discord Python Library
```
pip3 install discord.py
```

Install the Dotenv Library 
```
pip install -U python-dotenv
```
Install the Requests Library
```
pip3 install requests
```
Create a .env file to store your token(s)
```
cd src
touch .env
```
Add your Discord Bot's secret token into the .env
```
DISCORD_BOT_TOKEN="your-token-here"
```

You can now run the Bot
```
python3 main.py
```

For more information on how create the Discord bot accounts and add them to your server, check out the Discord Developer Documentation.

[https://discord.com/developers/docs/intro](https://discord.com/developers/docs/intro)

## Built With

* [Python 3.6+](https://www.python.org/) 
* [Discord.py](https://discordpy.readthedocs.io/en/latest/) - Python Library

## Contributing

Feel free to create a pull request with any additions you want to add and I'll review as they come in.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
