# Assistant information app for Snips

[![Build status](https://api.travis-ci.com/koenvervloesem/snips-app-assistant-information.svg?branch=master)](https://travis-ci.com/koenvervloesem/snips-app-assistant-information) [![Maintainability](https://api.codeclimate.com/v1/badges/1e58b5f63edc5d98f6d7/maintainability)](https://codeclimate.com/github/koenvervloesem/snips-app-assistant-information/maintainability) [![Code quality](https://api.codacy.com/project/badge/Grade/34eb8497da8c4f4cb8a70de5568ab837)](https://www.codacy.com/app/koenvervloesem/snips-app-assistant-information) [![Python versions](https://img.shields.io/badge/python-3.5|3.6|3.7-blue.svg)](https://www.python.org) [![GitHub license](https://img.shields.io/github/license/koenvervloesem/snips-app-assistant-information.svg)](https://github.com/koenvervloesem/snips-app-assistant-information/blob/master/LICENSE) [![Languages](https://img.shields.io/badge/i18n-en|de-brown.svg)](https://github.com/koenvervloesem/snips-app-assistant-information/tree/master/translations) [![Snips App Store](https://img.shields.io/badge/snips-app-blue.svg)](https://console.snips.ai/store/en/skill_MxzdQxPxXZW)

With this [Snips](https://snips.ai/) app, you can ask some information about your Snips assistant, like its name, ID, the platform it is running on, the Snips version, its hostname and IP address, the installed apps and the number of intents it understands.

## Installation

The easiest way to install this app is by adding the corresponding Snips app to your assistant in the [Snips Console](https://console.snips.ai):

*   English: [Assistant information](https://console.snips.ai/store/en/skill_MxzdQxPxXZW)
*   German: [Assistents Informationen](https://console.snips.ai/store/de/skill_bgg1mzp7EB2)

## Usage

This app recognizes the following intents:

*   AssistantApps - The user asks which apps the assistant has.
*   AssistantID - The user asks the assistant's ID.
*   AssistantIntents - The user asks the assistant how many intents it understands.
*   AssistantName - The user asks what the assistant's name is.
*   AssistantPlatform - The user asks what platform the assistant is running on.
*   Hostname- The user asks the assistant what hostname the Snips machine has on the local network.
*   IPAddress - The user asks the assistant what IP address the Snips machine has on the local network.
*   LatestSnipsVersion - The user asks the assistant what the latest available version of Snips is. 
*   LatestSnipsVersionRunning - The user asks the assistant whether it is running the latest version of Snips. 
*   SnipsVersion - The user asks the assistant what version of Snips it is running.
*   Uptime - The user asks the assistant how long its machine has been running. 

## Copyright

This app is provided by [Koen Vervloesem](mailto:koen@vervloesem.eu) as open source software. See LICENSE for more information.
