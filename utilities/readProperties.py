import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getServername():
        url = config.get("common_info","server")
        return url

    @staticmethod
    def getDatabasename():
        username = config.get("common_info", "database")
        return username
