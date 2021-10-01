from app.utils.configParser import Parser
import os


def getDataBasePath():
    appDir = os.path.dirname(os.path.dirname(__file__))
    dataBasePath = os.path.join(appDir, 'database')
    return dataBasePath


def getConfiguration(ctype):
    print(ctype)
    if ctype == 'app':

        config = Parser.parse(os.path.join(
            os.path.dirname(__file__), 'appConfiguration.json'))

        if config["type"] == "csv":
            # This is done to get the absolute path
            dataBasePath = getDataBasePath()
            config["dbpath"] = os.path.join(dataBasePath, config["dbpath"])
            config["metadata"] = os.path.join(dataBasePath, config["metadata"])

        return config

    elif ctype == 'privacy':
        return Parser.parse(os.path.join(os.path.dirname(__file__), 'privacyConfiguration.json'))
