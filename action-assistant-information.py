#!/usr/bin/env python3
"""
This module contains a Snips app that answers questions about your Snips
assistant.
"""

import importlib
from pathlib import Path
import socket
from urllib.error import URLError

from snipskit.apps import SnipsAppMixin
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent
from snipskit.services import version
from snipskit.tools import latest_snips_version

# Use the assistant's language.
i18n = importlib.import_module('translations.' + SnipsAppMixin().assistant['language'])


class AssistantInformation(HermesSnipsApp):
    """
    This app answers questions about your Snips assistant.
    """

    @intent(i18n.INTENT_ASSISTANT_APPS)
    def handle_assistant_apps(self, hermes, intent_message):
        """Handle the intent AssistantApps."""

        # Look at the snippets directory and not in Snipsfile.yaml.
        # The former also contains apps with inline snippets,
        # the latter doesn't.
        apps = [str(app) for app in (Path(self.assistant.filename).parent / 'snippets').iterdir()]

        # Make the names more pronounceable.
        # For instance: from 'koan.What_is_happening_on_this_day' to
        # 'What is happening on this day'
        apps = [app[app.find('.')+1:].replace('_', ' ') for app in apps]

        # Tell "X, Y, and Z" instead of "X, Y, Z"
        # We always have at least one app, otherwise this app wouldn't run...
        # So we don't need to check for num_apps == 0.
        num_apps = len(apps)
        if num_apps == 1:
            names_apps = apps[0]
        else:
            last_app = apps.pop()
            names_apps = ', '.join(apps) + i18n.AND + last_app

        result_sentence = i18n.RESULT_ASSISTANT_APPS.format(num_apps,
                                                            names_apps)
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_ASSISTANT_ID)
    def handle_assistant_id(self, hermes, intent_message):
        """Handle the intent AssistantID."""

        # Spell out the individual letters of the ID
        prefix, suffix = self.assistant['id'].split('_')
        suffix = ' '.join(list(suffix))
        project_id = prefix + '_' + suffix

        result_sentence = i18n.RESULT_ASSISTANT_ID.format(project_id)
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_ASSISTANT_INTENTS)
    def handle_assistant_intents(self, hermes, intent_message):
        """Handle the intent AssistantIntents."""
        number_of_intents = len(self.assistant['intents'])

        result_sentence = i18n.RESULT_ASSISTANT_INTENTS.format(number_of_intents)
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_ASSISTANT_NAME)
    def handle_assistant_name(self, hermes, intent_message):
        """Handle the intent AssistantName."""
        name = self.assistant['name']

        result_sentence = i18n.RESULT_ASSISTANT_NAME.format(name)
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_ASSISTANT_PLATFORM)
    def handle_assistant_platform(self, hermes, intent_message):
        """Handle the intent AssistantPlatform."""
        platform = self.assistant['platform']['type'].replace('raspberrypi',
                                                              i18n.REPLACE_TTS_RASPI)

        result_sentence = i18n.RESULT_ASSISTANT_PLATFORM.format(platform)
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_HOSTNAME)
    def handle_hostname(self, hermes, intent_message):
        """Handle the intent Hostname."""

        result_sentence = i18n.RESULT_HOSTNAME.format(socket.gethostname())
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_IP_ADDRESS)
    def handle_ip_address(self, hermes, intent_message):
        """Handle the intent IPAddress."""

        # Based on https://stackoverflow.com/a/28950776/10368577
        # This *should* work on Linux, macOS and Windows.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # This doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            ip_address = s.getsockname()[0]
        except OSError:
            ip_address = '127.0.0.1'
        finally:
            s.close()

        result_sentence = i18n.RESULT_IP_ADDRESS.format(i18n.tts_ip_address(ip_address))
        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_SNIPS_VERSION)
    def handle_snips_version(self, hermes, intent_message):
        """Handle the intent SnipsVersion."""
        installed = version()
        result_sentence = i18n.RESULT_SNIPS_VERSION.format(i18n.tts_version(installed))

        try:
            latest = latest_snips_version()
            if installed < latest:
                result_sentence += i18n.RESULT_NEWER_VERSION_AVAILABLE
        except URLError:
            pass  # The user didn't ask for the latest version, so ignore it.

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_LATEST_SNIPS_VERSION)
    def handle_latest_snips_version(self, hermes, intent_message):
        """Handle the intent LatestSnipsVersion."""
        try:
            latest = latest_snips_version()
            installed = version()
            result_sentence = i18n.RESULT_LATEST_SNIPS_VERSION.format(i18n.tts_version(latest))
            if installed < latest:
                result_sentence += i18n.RESULT_OLDER
        except URLError:
            result_sentence = i18n.RESULT_NO_RELEASE_NOTES

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent(i18n.INTENT_LATEST_SNIPS_VERSION_RUNNING)
    def handle_latest_snips_version_running(self, hermes, intent_message):
        """Handle the intent LatestSnipsVersionRunning."""
        try:
            latest = latest_snips_version()
            installed = version()
            if installed < latest:
                result_sentence = i18n.RESULT_NOT_UPDATED.format(i18n.tts_version(installed),
                                                                 i18n.tts_version(latest))
            else:
                result_sentence = i18n.RESULT_UPDATED
        except URLError:
            result_sentence = i18n.RESULT_NO_RELEASE_NOTES

        hermes.publish_end_session(intent_message.session_id, result_sentence)


if __name__ == "__main__":
    AssistantInformation()
