"""
This module contains the result sentences and intents for the French version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "J'ai {} applications : {}."
RESULT_ASSISTANT_ID = "Mon identifiant est le suivant : {}."
RESULT_ASSISTANT_INTENTS = "Je suis capable de comprendre {} différentes demandes."
RESULT_ASSISTANT_NAME = "Je m'appelle {}."
RESULT_ASSISTANT_PLATFORM = "Je fonctionne sur l'appareil {}."
RESULT_HOSTNAME = "Mon nom d'hôte est {}."
RESULT_IP_ADDRESS = "Mon adresse IP est {}."
RESULT_SNIPS_VERSION = "J'utilise la version {} de Snips."
RESULT_NEWER_VERSION_AVAILABLE = "Une nouvelle version de Snips est disponible."
RESULT_LATEST_SNIPS_VERSION = "La dernière version de Snips est la {}."
RESULT_OLDER = "J'utilises une ancienne version de Snips. Je pourrai être mis à jour."
RESULT_NO_RELEASE_NOTES = "Je suis désolé, je ne parviens pas à accéder aux notes de version de Snips."
RESULT_UPDATED = "J'utilises la version la plus récente de Snips, la {}."
RESULT_NOT_UPDATED = "J'utilise toujours la version {} de Snips, alors que la version {} est disponible."
RESULT_UPTIME = "J'ai commencé à fonctionner {}."
AND = ", et "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberry Pi"

def tts_ip_address(ip_address):
    """Convert an IP address to something the TTS will pronounce correctly.

    Args:
        ip_address (str): The IP address, e.g. '102.168.0.102'

    Returns:
        str: A pronounceable IP address, e.g. '192 dot 168 dot 0 dot 102'
    """
    return ip_address.replace('.', ' point ')

def tts_version(version):
    """Convert a version string to something the TTS will pronounce correctly.

    Args:
        version (str): The version string, e.g. '1.1.2'

    Returns:
        str: A pronounceable version string, e.g. '1 point 1 point 2'
    """
    return version.replace('.', ' point ')

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
