def apply_all_func(int_list, *functions):
    results = {}
    try:
        for element in int_list:
            if isinstance(element, (int, float)):
                for func in functions:
                    results[func.__name__] = func(int_list)
                return results
            else:
                raise TypeError
        return results
    except TypeError:
        print('Все элементы списка должны быть числами')


if __name__ == '__main__':
    print(apply_all_func([6,20,15,9],  max, min))
    print(apply_all_func([6,20,15,9], len, sum,sorted))
    print(apply_all_func([6,'20',15,9], sum,max, min))
    print(apply_all_func([6,20,15,9], sum,max, min))

