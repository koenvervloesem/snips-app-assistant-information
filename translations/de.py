"""
This module contains the result sentences and intents for the German version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "Ich habe {} apps: {}."
RESULT_ASSISTANT_ID = "Meine ID ist {}."
RESULT_ASSISTANT_INTENTS = "Ich kenne {} Befehle."
RESULT_ASSISTANT_NAME = "Mein Name ist {}."
RESULT_ASSISTANT_PLATFORM = "Ich laufe auf der {} platform."
RESULT_HOSTNAME = "Mein Host-Name ist {}."
RESULT_IP_ADDRESS = "Meine IP Adresse ist {}."
RESULT_SNIPS_VERSION = "Ich laufe mit Snips version {}."
# RESULT_NEWER_VERSION_AVAILABLE = "There's a newer version available."
# RESULT_LATEST_SNIPS_VERSION = "The latest Snips version is {}."
# RESULT_OLDER = "I'm still running an older version."
# RESULT_NO_RELEASE_NOTES = "I'm sorry, I can't access the release notes of Snips."
# RESULT_UPDATED = "I'm running the latest Snips version, {}."
# RESULT_NOT_UPDATED = "I'm still running Snips version {}, while version {} is already available."
# RESULT_UPTIME = "I woke up {}."
AND = ", und "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberrie Pei"

# TODO: Look at en.py for some new tts workaround functions

# Intents
INTENT_ASSISTANT_APPS = 'Philipp:AssistantApps'
INTENT_ASSISTANT_ID = 'Philipp:AssistantID'
INTENT_ASSISTANT_INTENTS = 'Philipp:AssistantIntents'
INTENT_ASSISTANT_NAME = 'Philipp:AssistantName'
INTENT_ASSISTANT_PLATFORM = 'Philipp:AssistantPlatform'
INTENT_HOSTNAME = 'Philipp:Hostname'
INTENT_IP_ADDRESS = 'Philipp:IPAddress'
INTENT_LATEST_SNIPS_VERSION = 'Philipp:LatestSnipsVersion'
INTENT_LATEST_SNIPS_VERSION_RUNNING = 'Philipp:LatestSnipsVersionRunning'
INTENT_SNIPS_VERSION = 'Philipp:SnipsVersion'
INTENT_UPTIME = 'Philipp:Uptime'
