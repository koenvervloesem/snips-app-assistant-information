"""
This module contains the result sentences and intents for the Spanish version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "Tengo {} aplicacioness : {}."
RESULT_ASSISTANT_ID = "Mi identificador es : {}."
RESULT_ASSISTANT_INTENTS = "Soy capaz de entender {} diferentes peticiones."
RESULT_ASSISTANT_NAME = "Mi nombre es {}."
RESULT_ASSISTANT_PLATFORM = "Trabajando en el dispositivo {}."
RESULT_HOSTNAME = "Mi nombre de host es {}."
RESULT_IP_ADDRESS = "Mi dirección IP es {}."
RESULT_SNIPS_VERSION = "Uso la versión {} de Snips."
RESULT_NEWER_VERSION_AVAILABLE = "Una nueva versión de Snips está disponible."
RESULT_LATEST_SNIPS_VERSION = "La última versión de Snips es la {}."
RESULT_OLDER = "Uso una versión antigua de Snips. Puedo actualizarme."
RESULT_NO_RELEASE_NOTES = "Lo siento, no puedo acceder a las notas de versiones de Snips."
RESULT_UPDATED = "Uso la versión más reciente de Snips, es la {}."
RESULT_NOT_UPDATED = "Uso de forma permanente la versión {} de Snips, aunque está disponible la versión {}."
RESULT_UPTIME = "Inicio el funcionamiento {}."
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
INTENT_ASSISTANT_APPS = 'pepebc:AssistantApps'
INTENT_ASSISTANT_ID = 'pepebc:AssistantID'
INTENT_ASSISTANT_INTENTS = 'pepebc:AssistantIntents'
INTENT_ASSISTANT_NAME = 'pepebc:AssistantName'
INTENT_ASSISTANT_PLATFORM = 'pepebc:AssistantPlatform'
INTENT_HOSTNAME = 'pepebc:Hostname'
INTENT_IP_ADDRESS = 'pepebc:IPAddress'
INTENT_LATEST_SNIPS_VERSION = 'pepebc:LatestSnipsVersion'
INTENT_LATEST_SNIPS_VERSION_RUNNING = 'pepebc:LatestSnipsVersionRunning'
INTENT_SNIPS_VERSION = 'pepebc:SnipsVersion'
INTENT_UPTIME = 'pepebc:Uptime'
