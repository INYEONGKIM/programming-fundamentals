def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level=="하": return 6
    if level == "중": return 8
    if level == "상": return 10
print(get_level())