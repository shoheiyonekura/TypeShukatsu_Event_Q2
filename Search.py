def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    l = 0 #配列の左端のインデックス
    r = len(sorted_array) - 1 #配列の右端のインデックス

    while l <= r:
        md = (l + r) // 2 #配列の中心のインデックス
        if sorted_array[md] <  target_number:
            l = md + 1 #左端を中心の隣に移動
        elif sorted_array[md] > target_number:
            r = md - 1 #右端を中心の隣に移動
        else:
            return md

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()