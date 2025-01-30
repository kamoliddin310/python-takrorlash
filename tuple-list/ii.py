def lst_raqam_qushish( a ):
    son = int("".join(map(str, a)))
    son += 1
    return list(map(int, str(son)))

print(lst_raqam_qushish([1,2,3]))
print(lst_raqam_qushish([9]))
print(lst_raqam_qushish([9,9,9,9]))