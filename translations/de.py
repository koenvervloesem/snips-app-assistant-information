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
RESULT_NEWER_VERSION_AVAILABLE = "Eine neue Version ist verfügbar."
RESULT_LATEST_SNIPS_VERSION = "Die neuste Version von Snips ist {}."
RESULT_OLDER = "Ich laufe noch auf einer alten Version."
RESULT_NO_RELEASE_NOTES = "Entschuldige, ich kann die aktuellste Version nicht ermitteln."
RESULT_UPDATED = "Ich laufe auf der neusten Version von Snips, Version {}."
RESULT_NOT_UPDATED = "Ich laufe noch auf Snips version {}, während Version {} bereits verfügbar ist."
RESULT_UPTIME = "Ich bin wach seit {}."
AND = ", und "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberrie Pei"

def tts_ip_address(ip_address):
    """Convert an IP address to something the TTS will pronounce correctly.
    Args:
        ip_address (str): The IP address, e.g. '102.168.0.102'
    Returns:
        str: A pronounceable IP address, e.g. '192 dot 168 dot 0 dot 102'
    """
    return ip_address.replace('.', ' Punkt ')

def tts_version(version):
    """Convert a version string to something the TTS will pronounce correctly.
    Args:
        version (str): The version string, e.g. '1.1.2'
    Returns:
        str: A pronounceable version string, e.g. '1 point 1 point 2'
    """
    return version.replace('.', ' Punkt ')

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
