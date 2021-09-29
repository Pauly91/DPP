import json


class Parser:
    @staticmethod
    def parse(configFile):
        data = []
        try:
            with open(configFile, "r") as jsonfile:
                data = json.load(jsonfile)
        except Exception as error:
            print(error)
        return data
