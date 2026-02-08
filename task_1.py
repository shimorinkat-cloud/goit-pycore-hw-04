def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0
    except ValueError:
        print("Помилка у форматі даних")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума: {total}, Середня: {average}")
