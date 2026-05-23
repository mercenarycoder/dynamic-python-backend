import csv
import random
from datetime import date, timedelta


def random_dob_from_age(age):
    # age in years; pick a random day within that year
    today = date.today()
    start = date(today.year - age, 1, 1)
    end = date(today.year - age, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))


def generate_csv(path, rows=100, seed=42):
    random.seed(seed)
    fieldnames = ["Date-of-birth", "Yearsofexperience", "Salary"]
    base_salaries = [30000, 35000, 40000]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(rows):
            years = random.randint(0, 35)
            base = random.choice(base_salaries)
            # 15% chance to be an innovator with 20% yearly increase
            innovator = random.random() < 0.15
            growth = 0.20 if innovator else 0.10
            salary = base * ((1 + growth) ** years)
            salary = round(salary, 2)

            # estimate age: years of experience + starting age between 22 and 30
            start_age = random.randint(22, 30)
            age = years + start_age
            dob = random_dob_from_age(age)

            writer.writerow({
                "Date-of-birth": dob.isoformat(),
                "Yearsofexperience": years,
                "Salary": salary,
            })

    print(f"Wrote {rows} rows to {path}")


if __name__ == "__main__":
    out_path = "C:\\Users\\91738\\Desktop\\dynamic-python-bankend\\Regression\\salary.csv"
    generate_csv(out_path, rows=100, seed=2026)
