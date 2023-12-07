# Clip Fetcher Bot

A Telegram bot for downloading videos from popular websites like YouTube, Instagram, Reddit, Facebook etc. This bot uses the popular `yt-dlp` program
in the back end.

## Access
You can access the bot [here](https://t.me/clip_fetcher_bot).

## Features

- Download videos directly within Telegram chat windows from almost all popular websites. A complete list of all supported sites can be found [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

- Get the link to download the video in case you do not want to download now
for whatever reason. **Do note that YouTube video download links expire after
some time**.


## Usage

You can interact with the bot either personally (i.e. in a seperate chat with the bot) or in a group. If you're using the bot in a group and you've got **multiple bots** in the group, you need to suffix every command with `@clip_fetcher_bot`—the username of the bot; you don't need to do this if the last bot that the group members have interacted with is this bot itself.

For futher help, including the various commands the bot supports, type `/help` or `/help@clip_fetcher_bot` (depending on where you're chatting with the bot).

## Host it yourself
If you'd like to have your own bot and use this bot's code, you'd need to have the following:

- Python >=3.8
- [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot/)
- An API key from [BotFather](https://t.me/BotFather). Type `/help` in its chat to learn how to do that.
- A minimal server that will run the Python program.
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

NOTE: Copy the API key and save it to a text file named `api_key.txt`. 

You're good to go 👍

## Contribution
If you'd like to contribute to the development of the bot, thank you! The following guidelines have to be kept in mind:

- **Stay on topic**: Contribute something to the code which is related to the bot's function.

- **Fork and Clone**: Start by forking the project, and then clone it to your local machine for development.

- **Create a Branch**: Always create a new branch for your changes. This keeps the project history cleaner and makes it easier to manage different features or fixes.

- **Follow Style Guidelines**: Ensure your code follows any existing style guidelines or conventions. This might include things like code formatting, variable naming, etc.

- **Write Descriptive Commit Messages**: Commit messages should be clear and descriptive, explaining what changes were made and why.

- **Test Your Changes**: Before submitting your changes, make sure all existing tests pass and add new tests if necessary.

- **Document Your Changes**: Update the README or other documentation to reflect any changes you've made, if applicable.

- **Create a Pull Request**: Once your changes are ready and committed, push your branch to your fork and submit a pull request. In the pull request description, explain your changes and any issues they fix.

- **Respond to Feedback**: Be prepared to accept constructive criticism and respond to feedback on your pull request. Changes may not be accepted as is, and may require further work or adjustment.

Thanks for the help! 😄

## License
This project is licensed under the terms of the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, under the condition that you include the original copyright notice and disclaimers in any copies of the software or substantial portions of it.