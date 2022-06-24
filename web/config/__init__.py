import os


def load_config(mode=os.environ.get('MODE')):
    """ Load Config """
    try:
        if mode == "PRODUCTION":
            from .production import ProductionConfig
            print(ProductionConfig)
            return ProductionConfig
        elif mode == "TESTING":
            from .testing import TestingConfig
            print(TestingConfig)
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            print(DevelopmentConfig)
            return DevelopmentConfig

    except ImportError:
        from .development import DevelopmentConfig
        return DevelopmentConfig
