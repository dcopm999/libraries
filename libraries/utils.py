import logging
from libraries.models import Registration

LOGGER = logging.getLogger(__name__)


def get_token(host=None):
    '''
    Получение параметры подключения к API
    '''
    try:
        # Находим запись с заданным доменом
        query = Registration.objects.get(host=host)
    except IndexError:
        LOGGER.exception("Незаданы параметры подключения к API")
        raise Registration.DoesNotExist("Незаданы параметры подключения к API")
    else:
        return query.token
