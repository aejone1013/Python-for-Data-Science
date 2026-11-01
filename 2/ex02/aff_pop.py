import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def to_number(value) -> float:
    """Turn values like '3.28M', '60k' or 42 into a float."""
    if isinstance(value, (int, float)):
        return float(value)
    units = {"k": 1e3, "M": 1e6, "B": 1e9}
    text = str(value).strip()
    if text and text[-1] in units:
        return float(text[:-1]) * units[text[-1]]
    return float(text)


def main():
    """Plot the population of France vs Belgium from 1800 to 2050."""
    try:
        countries = {"Belgium": "tab:blue", "France": "green"}
        data = load("population_total.csv")
        if data is None:
            return
        years = [str(year) for year in range(1800, 2051)]
        assert all(y in data.columns for y in years), "years are missing"

        for country, color in countries.items():
            row = data[data["country"] == country]
            assert not row.empty, f"{country} not found in the dataset"
            values = [to_number(v) for v in row.iloc[0][years]]
            plt.plot([int(y) for y in years], values,
                     label=country, color=color)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(range(1800, 2051, 40))
        plt.gca().yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, _: f"{x / 1e6:.0f}M"))
        plt.legend(loc="lower right")
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
