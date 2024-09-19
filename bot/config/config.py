from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    API_KEY: str

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: int = 1800

    ADD_TAPS_ON_TURBO: int = 2500

    AUTO_UPGRADE_TAP: bool = True
    MAX_TAP_LEVEL: int = 5
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_ENERGY_LEVEL: int = 5
    AUTO_UPGRADE_CHARGE: bool = True
    MAX_CHARGE_LEVEL: int = 3

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = False

    RANDOM_TAPS_COUNT: list[int] = [15, 75]
    SLEEP_BETWEEN_TAP: list[int] = [30, 60]
    ACTIVE_TURBO_DELAY: int = 10

    USE_PROXY_FROM_FILE: bool = False

    USE_TAP_BOT: bool = True
    EMERGENCY_STOP: bool = False


settings = Settings()
