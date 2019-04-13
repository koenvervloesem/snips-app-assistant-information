"""
This module contains the result sentences and intents for the English version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "I have {} apps: {}."
RESULT_ASSISTANT_ID = "My ID is {}."
RESULT_ASSISTANT_INTENTS = "I know {} intents."
RESULT_ASSISTANT_NAME = "My name is {}."
RESULT_ASSISTANT_PLATFORM = "I'm running on the {} platform."
RESULT_HOSTNAME = "My host name is {}."
RESULT_IP_ADDRESS = "My IP address is {}."
RESULT_SNIPS_VERSION = "I'm running Snips version {}."
RESULT_NEWER_VERSION_AVAILABLE = "There's a newer version available."
RESULT_LATEST_SNIPS_VERSION = "The latest Snips version is {}."
RESULT_OLDER = "I'm still running an older version."
RESULT_NO_RELEASE_NOTES = "I'm sorry, I can't access the release notes of Snips."
RESULT_UPDATED = "I'm running the latest Snips version, {}."
RESULT_NOT_UPDATED = "I'm still running Snips version {}, while version {} is already available."
RESULT_UPTIME = "I awoke {}."
AND = ", and "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberry Pi"

def tts_ip_address(ip_address):
    """Convert an IP address to something the TTS will pronounce correctly.

    Args:
        ip_address (str): The IP address, e.g. '102.168.0.102'

    Returns:
        str: A pronounceable IP address, e.g. '192 dot 168 dot 0 dot 102'
    """
    return ip_address.replace('.', ' dot ')

def tts_version(version):
    """Convert a version string to something the TTS will pronounce correctly.

    Args:
        version (str): The version string, e.g. '1.1.2'

    Returns:
        str: A pronounceable version string, e.g. '1 point 1 point 2'
    """
    return version.replace('.', ' point ')

# Intents
INTENT_ASSISTANT_APPS = 'koan:AssistantApps'
INTENT_ASSISTANT_ID = 'koan:AssistantID'
INTENT_ASSISTANT_INTENTS = 'koan:AssistantIntents'
INTENT_ASSISTANT_NAME = 'koan:AssistantName'
INTENT_ASSISTANT_PLATFORM = 'koan:AssistantPlatform'
INTENT_HOSTNAME = 'koan:Hostname'
INTENT_IP_ADDRESS = 'koan:IPAddress'
INTENT_LATEST_SNIPS_VERSION = 'koan:LatestSnipsVersion'
INTENT_LATEST_SNIPS_VERSION_RUNNING = 'koan:LatestSnipsVersionRunning'
INTENT_SNIPS_VERSION = 'koan:SnipsVersion'
INTENT_UPTIME = 'koan:Uptime'
