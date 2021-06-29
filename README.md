# discord-slash-requests
A small python program to help with discord slash commands

# Setup
Copy the `config.json` and `slashrequest.py` files into your project and fill in the required flags for the config.

# Usage
Run a `python3` terminal and import the `sc` class (`from slashrequest import sc`) for guild-specific usage. For global usage, import the `gl` class (`from slashrequest import gl`).

\* **Note:** Both GL and SC classes have the same function names and parameters

## Getting all commands
To get all commands, use `[class].get()`, which will return a tuple of dicts which contain their respective name and ID. To get one specific command, pass in the command name like so: `[class].get('command_name')`. This returns all parameters of a command with options and version IDs. To get all parameters for all commands, use `[class].get(all=True)` which will return a list of all commands.

## Creating a command
Use the [web tool](https://windowsvistaiscool.github.io/discord-slash-generator) (coming soon) to generate your command. Take the JSON output and put it into the `[class].post()` method. (ex. `gl.post({"name":"example","description":"Example description"})`)

### Modifying a command
You can use the tool again to modify an existing command with this same method.

## Removing a command
To remove a command, use the `[class].rem()` method and pass in the command name like this: `[class].rem("command_name")`

## Setting permissions for a command
\* **Note:** The GL class does not have this method and should only be used by the SC class
To set permissions, use the `sc.perm()` method. The first parameter will always be the **command ID**. [more coming soon]

## Changing the guild ID
\* **Note:** This method will change the guild ID set in the config
To change the guild ID for the SC class, use `sc.setGID()` method and passing a **string** containing the guild ID

# Responses
### 200-204
The method was successful
### 401 or 403
Unauthorized
### 404 
Resource not found
