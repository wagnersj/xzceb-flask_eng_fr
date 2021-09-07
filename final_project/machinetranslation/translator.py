'''
Translator application
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv('./machinetranslation/.env')


apikey = os.environ['apikey']
url = os.environ['url']

# Set up the translator service
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-07',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def translate(text, model_id):
    '''
    Translates the text into the target language of the model_id
    '''
    apiret = language_translator.translate(text=text, model_id=model_id).get_result()
    translation = apiret['translations'][0]['translation']
    return translation


def english_to_french(english_text):
    '''
    Translates English text to French
    '''
    french_text = translate(english_text, 'en-fr')
    return french_text


def french_to_english(french_text):
    '''
    Translates French text to English
    '''
    english_text = translate(french_text, 'fr-en')
    return english_text
