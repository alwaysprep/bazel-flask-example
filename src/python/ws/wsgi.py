from src.python.ws import create_app

if __name__ == "__main__":
    create_app("src.python.ws.conf.DevelopmentConfig").run()
