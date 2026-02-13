from sys import stdin
def maximizeCuts_rec(n, x, y, z):
    if n == 0:
        return 0
    
    if n < 0:
        return -1
    
    cut_x = maximizeCuts_rec(n - x, x, y, z)
    cut_y = maximizeCuts_rec(n - y, x, y, z)
    cut_z = maximizeCuts_rec(n - z, x, y, z)

    max_cut = (cut_x, cut_y, cut_z)

    if max_cut == -1:
        return -1
    
    return max_cut + 1


def cut(n, x, y, z):
    memo = dict()
    answer = maximizeCuts_rec(n, x, y, z)
    #answer = maximizeCuts_dina(n, x, y, z, memo)
    if answer == -1:
        return 0
    return answer

def main():
    n, x, y, z = (int(i) for i in stdin.readline().strip().split())
    print(cut(n, x, y, z))

main()
