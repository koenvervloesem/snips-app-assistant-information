"""
This module contains the result sentences and intents for the Italian version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "Io ho {} applicazioni : {}."
RESULT_ASSISTANT_ID = "Il mio numero identificativo è: {}."
RESULT_ASSISTANT_INTENTS = "Conosco {} differenti comandi."
RESULT_ASSISTANT_NAME = "Mi chiamo {}."
RESULT_ASSISTANT_PLATFORM = "Sto funzionando sul dispositivo {}."
RESULT_HOSTNAME = "Il nome dell'host è {}."
RESULT_IP_ADDRESS = "Il mio indirizzo ip è {}."
RESULT_SNIPS_VERSION = "Utilizzo la versione {} di Snips."
RESULT_NEWER_VERSION_AVAILABLE = "E' disponibile una nuova versione."
RESULT_LATEST_SNIPS_VERSION = "L'ultima versione di Snips è la {}."
RESULT_OLDER = "Sto usando una versione non aggiornata."
RESULT_NO_RELEASE_NOTES = "Mi dispiace, non riesco ad accedere alle note di rilascio di Snips."
RESULT_UPDATED = "Sto utilizzano la versione più recente di Snips, {}."
RESULT_NOT_UPDATED = "Sto utilizzando la versione {} di Snips, mentre la versione {} è già disponibile."
RESULT_UPTIME = "Mi sono svegliato {}."
AND = ", e "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberry Pi"

def tts_ip_address(ip_address):
    """Convert an IP address to something the TTS will pronounce correctly.

    Args:
        ip_address (str): The IP address, e.g. '102.168.0.102'

    Returns:
        str: A pronounceable IP address, e.g. '192 dot 168 dot 0 dot 102'
    """
    return ip_address.replace('.', ' punto ')

def tts_version(version):
    """Convert a version string to something the TTS will pronounce correctly.

    Args:
        version (str): The version string, e.g. '1.1.2'

    Returns:
        str: A pronounceable version string, e.g. '1 point 1 point 2'
    """
    return version.replace('.', ' punto ')

# Intents
INTENT_ASSISTANT_APPS = 'SparkMonkey:AssistantApps'
INTENT_ASSISTANT_ID = 'SparkMonkey:AssistantID'
INTENT_ASSISTANT_INTENTS = 'SparkMonkey:AssistantIntents'
INTENT_ASSISTANT_NAME = 'SparkMonkey:AssistantName'
INTENT_ASSISTANT_PLATFORM = 'SparkMonkey:AssistantPlatform'
INTENT_HOSTNAME = 'SparkMonkey:Hostname'
INTENT_IP_ADDRESS = 'SparkMonkey:IPAddress'
INTENT_LATEST_SNIPS_VERSION = 'SparkMonkey:LatestSnipsVersion'
INTENT_LATEST_SNIPS_VERSION_RUNNING = 'SparkMonkey:LatestSnipsVersionRunning'
INTENT_SNIPS_VERSION = 'SparkMonkey:SnipsVersion'
INTENT_UPTIME = 'SparkMonkey:Uptime'
