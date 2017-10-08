triangular = []
pentagonal = []
hexagonal = []
for number in range(1, 100001):
    triangular.append(int(number*(number + 1) / 2))
    pentagonal.append(int(number*((3*number) - 1) / 2))
    hexagonal.append(int(number*(2*number - 1)))
set_triangular = {number_t for number_t in triangular}
set_pentagonal = {number_p for number_p in pentagonal}
set_hexagonal = {number_h for number_h in hexagonal}
set_intersection_t_p = set_triangular & set_pentagonal
set_intersection_final = set_intersection_t_p & set_hexagonal
print(set_triangular & set_pentagonal & set_hexagonal)
