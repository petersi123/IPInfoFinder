import pandas as pd
import requests


def add_word_to_csv_row(input_csv, output_csv):
    try:
        df = pd.read_csv(input_csv)
        mylist = []
        num_rows = df.shape[0]
        print(f"There are {num_rows} IP's")
        for number in range(0, num_rows):
            selected_row = df.iloc[number]
            mylist.append(selected_row.to_string(index=False))
        number = 0
        for things in mylist:
            url = f'https://ipinfo.io/{things}/json?'
            response = requests.get(url)
            data = response.json()
            if "country" in data:
                country = data["country"]
                df.at[number, 'Country'] = country
            if "org" in data:
                country = data["org"]
                df.at[number, 'ISP'] = country
            number = number + 1

        df.to_csv(output_csv, index=False)
        user = input("All Done")
    except Exception as e:
        print(f"")

if __name__ == "__main__":
    user = input("Put all ip's in input csv: ")
    input_csv = ("input.csv")
    output_csv = ("output.csv")
    add_word_to_csv_row(input_csv, output_csv)
