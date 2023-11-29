from pathlib import Path
names = ""
aa = "请输入访客的名字(完成所有访客的名字输入后，按q终止）"
user = input(aa)
while user != "q":
    names += user + "\n"
    user = input(aa)
path = Path("./guest_book.txt")
path.write_text(names)