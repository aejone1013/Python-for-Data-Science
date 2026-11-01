import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Plot the life expectancy of France from 1800 to 2100."""
    try:
        country = "France"
        data = load("life_expectancy_years.csv")
        if data is None:
            return
        row = data[data["country"] == country]
        assert not row.empty, f"{country} not found in the dataset"
        years = [int(year) for year in row.columns[1:]]
        values = row.iloc[0, 1:].astype(float)

        plt.plot(years, values)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(range(1800, 2101, 40))
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
