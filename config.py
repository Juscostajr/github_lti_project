import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Chave secreta do Flask
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'super_secreta_flask_456')

    # Configuração do LTI
    PYLTI_CONFIG = {
        'consumers': {
            os.environ.get('LTI_KEY', 'key'): {
                'secret': os.environ.get('LTI_SECRET', 'secret')
            }
        }
    }

    # Caminho do banco de dados
    DB_PATH = os.environ.get('DB_PATH', 'github_lti.db')

    # Token do GitHub
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
