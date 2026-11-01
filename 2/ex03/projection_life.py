import matplotlib.pyplot as plt
import pandas as pd
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
    """Plot life expectancy against GDP per person for the year 1900."""
    try:
        year = "1900"
        income = load("income_per_person_gdppercapita_ppp_"
                      "inflation_adjusted.csv")
        life = load("life_expectancy_years.csv")
        if income is None or life is None:
            return
        assert year in income.columns and year in life.columns, (
            f"{year} is missing in the datasets")

        merged = pd.merge(income[["country", year]],
                          life[["country", year]],
                          on="country", suffixes=("_gdp", "_life"))
        merged = merged.dropna()
        gdp = [to_number(v) for v in merged[f"{year}_gdp"]]
        expectancy = [to_number(v) for v in merged[f"{year}_life"]]

        plt.scatter(gdp, expectancy, label="Countries")
        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.legend()
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
