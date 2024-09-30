import os
from dotenv import load_dotenv
import json

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    MIN_AVAILABLE_ENERGY = int(os.getenv("MIN_AVAILABLE_ENERGY", '100'))
    SLEEP_BY_MIN_ENERGY = json.loads(os.getenv("SLEEP_BY_MIN_ENERGY", '[1800, 3600]'))

    ADD_TAPS_ON_TURBO = int(os.getenv("ADD_TAPS_ON_TURBO", '2500'))

    AUTO_UPGRADE_TAP = os.getenv("AUTO_UPGRADE_TAP", 'True')
    MAX_TAP_LEVEL = int(os.getenv("MAX_TAP_LEVEL", '5'))
    AUTO_UPGRADE_ENERGY = os.getenv("AUTO_UPGRADE_ENERGY", 'True')
    MAX_ENERGY_LEVEL = int(os.getenv("MAX_ENERGY_LEVEL", '5'))
    AUTO_UPGRADE_CHARGE = os.getenv("AUTO_UPGRADE_CHARGE", 'True')
    MAX_CHARGE_LEVEL = int(os.getenv("MAX_CHARGE_LEVEL", '3'))

    APPLY_DAILY_ENERGY = os.getenv("APPLY_DAILY_ENERGY", 'True')
    APPLY_DAILY_TURBO = os.getenv("APPLY_DAILY_TURBO", 'True')

    AUTO_CLEAR_MISSION = os.getenv("AUTO_CLEAR_MISSION", 'True')
    AUTO_PLAY_SPIN = os.getenv("AUTO_PLAY_SPIN", 'False')

    RANDOM_TAPS_COUNT = json.loads(os.getenv("RANDOM_TAPS_COUNT", '[15, 75]'))
    SLEEP_BETWEEN_TAP = json.loads(os.getenv("SLEEP_BETWEEN_TAP", '[15, 60]'))
    ACTIVE_TURBO_DELAY = int(os.getenv("ACTIVE_TURBO_DELAY", '4'))

    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", 'False')

    USE_TAP_BOT = os.getenv("USE_TAP_BOT", 'True')


settings = Settings()
