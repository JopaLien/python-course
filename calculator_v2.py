def enter_mark(mark):
    if 1 < mark < 6:
        return mark
    else:
        raise ValueError("Оценки могут быть только между двойкой и пятеркой включительно")


def calculate_marks():
    mark_sum = 0
    mark_count = 0
    while True:
        try:
            mark = int(input())
            enter_mark(mark)
        except ValueError:
            print("Оценки могут быть только целым числом между двойкой и пятеркой включительно")
        except KeyboardInterrupt:
            print()
            return mark_sum, mark_count
        else:
            mark_sum += mark
            mark_count += 1

        
def main():
    print("Введите свои оценки (CTRL + C для завершения программы):")
    mark_sum, mark_count = calculate_marks()
    if mark_count == 0:
        print("Не было введено ни одного числа")
    else:
        print("Средняя оценка за период =", mark_sum / mark_count)


if __name__ == "__main__":
    main()
