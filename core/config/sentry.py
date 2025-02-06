import sentry_sdk
from config import secrets

class SentryConfig:
    def __init__(self):
        self.dsn = secrets.SENTRY_DSN
        self.send_default_pii = True
        self.traces_sample_rate = 1.0
        self.profiles_sample_rate = 1.0

    def config(self):
        sentry_sdk.init(
            dsn=self.dsn,
            send_default_pii=self.send_default_pii,
            traces_sample_rate=self.traces_sample_rate,
            profiles_sample_rate=self.profiles_sample_rate,
        )