from app.utils.configParser import Parser
import os


def getDataBasePath():
    appDir = os.path.dirname(os.path.dirname(__file__))
    dataBasePath = os.path.join(appDir, 'database')
    return dataBasePath


def getConfiguration():

    config = Parser.parse(os.path.join(
        os.path.dirname(__file__), 'configuration.json'))

    if config["type"] == "csv":
        # This is done to get the absolute path
        dataBasePath = getDataBasePath()
        config["dbpath"] = os.path.join(dataBasePath, config["dbpath"])
        config["metadata"] = os.path.join(dataBasePath, config["metadata"])

    return config
