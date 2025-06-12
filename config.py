import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7605952520:AAHUIE32hgpQwCAHh6b7iNdIurXj7w-GTYw")

    APP_ID = int(os.environ.get("APP_ID", 20602242))

    API_HASH = os.environ.get("API_HASH", "010b3ab1779e7ebd28f02cc3be663992")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1O3mnlptOnv0hUTveEVAIZ60VZxAJBaEGpswhCYiyFM23l6D0EZXNNHM&s=10")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1O3mnlptOnv0hUTveEVAIZ60VZxAJBaEGpswhCYiyFM23l6D0EZXNNHM&s=10")
