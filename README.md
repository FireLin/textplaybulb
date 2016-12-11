## TextPlayBulb

#This project is build on 3 modules :
* pyBulbDriver : Connect to the PlayBulb via BLE gatttool and python.
* pyBulbServer : Using the pyBulbDriver to expose the playbulb control via REST API.
* pyBulbMessenger (Bouns) : Connecting to a telegram bot to send and receive commands via telegram client installed on any smart phone, and using the REST API to issue commands to the PlayBulb.

#Resources used to create this project:
* PlayBulb Color Bluetooth Protocol : https://github.com/Phhere/Playbulb/blob/master/protocols/color.md
* Connecting Python to Playbulb via Bluetooth : https://github.com/ianrenton/playbulb-tools
* Setting up the telegram bot : http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/

API key in pyBulbMessenger needs to be replaced by token after registering your telegram bot is in third resource "Setting up the telegram bot"
