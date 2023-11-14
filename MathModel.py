def darcy_law():
    k = float(input("Введите проницаемость породы (k): "))
    A = float(input("Введите площадь поперечного сечения породы (A): "))
    delta_P = float(input("Введите перепад давления (ΔP): "))
    mu = float(input("Введите вязкость флюида (μ): "))
    L = float(input("Введите длину породы (L): "))
    Q = (k * A * delta_P) / (mu * L)
    print(f"Расход флюида (Q): {Q}")

def filtration_equation():
    print("Уравнение фильтрации (уравнение Раджабпура):")
    epsilon = float(input("Введите значение эпсилон: "))
    phi = float(input("Введите значение пористости (phi): "))
    c_t = float(input("Введите значение общей сжимаемости (c_t): "))
    B = float(input("Введите значение объемного коэффициента (B): "))
    S = float(input("Введите значение источника/стока (S): "))
    result = f"Уравнение фильтрации: (∂²p/∂x²) = {epsilon * phi * c_t / B} (∂p/∂t) + {S}"
    print(result)

def dupuit_equation():
    print("Закон Дюпюи для сжимаемости нефти:")
    B_o = float(input("Введите начальное значение объемного коэффициента нефти (B_o): "))
    B_oi = float(input("Введите значение B_oi: "))
    beta = float(input("Введите значение сжимаемости нефти (beta): "))
    delta_P = float(input("Введите изменение давления (delta_P): "))
    delta_P_i = float(input("Введите начальное изменение давления (delta_P_i): "))
    result = f"Закон Дюпюи: 1/B_o = 1/B_oi + {beta * (delta_P - delta_P_i) / B_oi}"
    print(result)

def material_balance():
    N_oi = float(input("Введите начальные запасы нефти (N_oi): "))
    N_o = float(input("Введите текущие запасы нефти (N_o): "))
    A = float(input("Введите площадь месторождения (A): "))
    phi = float(input("Введите пористость (phi): "))
    S_oi = float(input("Введите начальную насыщенность нефти (S_oi): "))
    S_o = float(input("Введите текущую насыщенность нефти (S_o): "))
    
    material_balance_result = A * phi * (S_oi - S_o)
    print(f"Изменение запасов нефти: {material_balance_result}")
def water_filtration_equation():
    print("Уравнение фильтрации для воды (уравнение Дюпюи):")
    S_wi = float(input("Введите насыщенность воды (S_wi): "))
    c_wi = float(input("Введите сжимаемость воды (c_wi): "))
    B_wi = float(input("Введите объемный коэффициент воды (B_wi): "))
    p = float(input("Введите давление (p): "))

    result = c_wi * S_wi * p / B_wi
    print(f"Результат уравнения фильтрации для воды: {result}")

def main():
    print("Выберите формулу:")
    print("1. Закон Дарси для расхода флюида через пористую среду.")
    print("2. Уравнение фильтрации (уравнение Раджабпура).")
    print("3. Закон Дюпюи для сжимаемости нефти.")
    print("4. Материальный баланс нефтяного месторождения.")
    print("5. Уравнение фильтрации для воды (уравнение Дюпюи).")
    choice = input("Введите номер выбранной формулы (1-5): ")

    if choice == "1":
        darcy_law()
    elif choice == "2":
        filtration_equation()
    elif choice == "3":
        dupuit_equation()
    elif choice == "4":
        material_balance()
    elif choice == "5":
        water_filtration_equation()
    else:
        print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()



