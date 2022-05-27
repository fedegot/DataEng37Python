import json

class RatesParser:
    # retrieve the data from json file
    def __init__(self, filepath):
        rates_data = self._open_json_file(filepath)
        self.base_rate = rates_data["base"]
        self.date = rates_data["date"]
        self.gbp = rates_data["rates"]["GBP"]
        self.usd = rates_data["rates"]["USD"]
        self.jpy = rates_data["rates"]["JPY"]

    # open file json file
    def _open_json_file(self, filepath: str) -> dict:
        with open(filepath) as jsonfile:
            return json.load(jsonfile)

    def to_GBP(self, amount):
        return amount * self.gbp

if __name__ == "__main__":
    rp = RatesParser("exchange_rates.json")
    print(rp.gbp)
    # rates = rp._open_json_file("exchange_rates.json")
    # print(rates)
