
intr185_5let = 1280 + 2139 + 2067 + 1994 + 1920
intr185_10let = intr185_5let + 1844 + 1767 + 1689 + 1609 + 1527 + 1444
intr185_15let = intr185_10let + 1359+1273+1185+1096+1005
intr185_20let = intr185_15let + 912+817+721+623+523
intr185_25let = intr185_20let + 421+318+212+104+11


kred185_5let = 101607
kred185_10let = 80148
kred185_15let = 56612
kred185_20let = 30795


#################################################################


intr195_5let = 1352+2272+2213+2153+2091
intr195_10let = intr195_5let + 2029+1965+1900+1834+1766
intr195_15let = intr195_10let + 1697+1627+1555+1482+1408
intr195_20let = intr195_15let + 1332+1254+1175+1095+1013
intr195_25let = intr195_20let + 929+843+756+668+577
intr195_30let = intr195_25let + 485+391+295+197+97+10


kred195_5let = 105540
kred195_10let = 88689
kred195_15let = 70113
kred195_20let = 49637
kred195_25let = 27066


kred = 119610


if __name__ == '__main__':
    print('intress za 5 let (v konce)\n')

    print("\t1.85%\t1.95%\tIntr diff\t")

    print("5y:")
    print("\t{}\t{}\t{}".format(intr185_5let, intr195_5let, intr195_5let - intr185_5let))

    print("10y:")
    print("\t{}\t{}\t{}".format(intr185_10let, intr195_10let, intr195_10let-intr185_10let))

    print("15y:")
    print("\t{}\t{}\t{}".format(intr185_15let, intr195_15let, intr195_15let-intr185_15let))

    print("20y:")
    print("\t{}\t{}\t{}".format(intr185_20let, intr195_20let, intr195_20let-intr185_20let))

    print("25y:")
    print("\t{}\t{}\t{}".format(intr185_25let, intr195_25let, intr195_25let-intr185_25let))

    print("30y:")
    print("\t-----\t{}\ttotal diff {}".format(intr195_30let, intr195_30let-intr185_25let))

    print('\n' + '-' * 37 + '\n')

    print('kredit ostatok za 5 let (v konce)\n')

    print("\t1.85%\t\t\t1.95%\t\t\tOstatok diff\t")

    print("5y:")
    print("\t{} ({})\t{} ({})\t{}".format(kred185_5let, kred-kred185_5let, kred195_5let, kred-kred195_5let, kred195_5let - kred185_5let))

    print("10y:")
    print("\t{} ({})\t{} ({})\t{}".format(kred185_10let, kred-kred185_10let, kred195_10let, kred-kred195_10let, kred195_10let-kred185_10let))

    print("15y:")
    print("\t{} ({})\t{} ({})\t{}".format(kred185_15let, kred-kred185_15let, kred195_15let, kred-kred195_15let, kred195_15let-kred185_15let))

    print("20y:")
    print("\t{} ({})\t{} ({})\t{}".format(kred185_20let, kred-kred185_20let, kred195_20let, kred-kred195_20let, kred195_20let-kred185_20let))

    print("25y:")
    print("\t-----\t\t\t{} ({})\t{}".format(kred195_25let, kred-kred195_25let, kred195_25let - 0))
