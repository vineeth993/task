import csv
import argparse

class StringManipulation():    

    def change_case(self, string, upperOrLower = 1):
        if upperOrLower == 1:
            return string.upper()
        elif upperOrLower == 0:
            return string.lower()

    def to_alternate_lower(self, string):
        temp_list = [value.upper() if index%2 else value.lower() for index, value in enumerate(string)]
        string = "".join(temp_list)
        return string  

    def to_csv(self, string, file_name):

        with open(file_name, mode="w+") as string_csv:
            csv_writer = csv.writer(string_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([char for char in string])
        string_csv.close()
        return "CSV created!"

    def argsMain(self):

        myParser = argparse.ArgumentParser()
        myParser.add_argument("-i", "--Input", help="String to manipulate in quotes", type=str, required=True)
        myParser.add_argument("-o", "--Outputfile", help="output file name", default="string_csv.csv")
        myParser.add_argument("-u", "--Upper", help="1 for uppercase 0 for lowercase", default=1, choices=[0, 1],type=int)

        args = vars(myParser.parse_args())
        string = args["Input"]
        print(self.change_case(string, args['Upper']))
        print(self.to_alternate_lower(string))
        print(self.to_csv(string, args.get("Outputfile")))

if __name__ == "__main__":

    manipulation = StringManipulation()
    manipulation.argsMain()

        