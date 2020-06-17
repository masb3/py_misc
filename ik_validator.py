def ik_validator(ik: int) -> bool:
    """
    Verifies Estonian national id (isikukood) validity
    :param ik: Estonian national id (isikukood)
    :return: True if ik valid, otherwise False
    """
    multipliers1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    multipliers2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    divider = 11

    ik_list = list(map(int, str(ik)))
    check_num = sum(list(map(lambda x, y: x * y, ik_list, multipliers1))) % divider
    
    if check_num == 10:
        check_num = sum(list(map(lambda x, y: x * y, ik_list, multipliers2))) % divider
        
    if check_num == 10:
        check_num = 0

    return ik_list[-1] == check_num
