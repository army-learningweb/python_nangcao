def create_replace_file(file_name,file_content):
    f = open(file_name,"w", encoding="utf-8")
    f.write(file_content)
    f.close()
    return f

def read_file(file_name):
    f = open(file_name,"r", encoding="utf-8")
    return f

def readlines_file(file_name):
    f = file_name.readlines()
    return f

f1 = create_replace_file("btn_2cd.txt","Thân em vừa trắng lại vừa tròn\nBảy nổi ba chìm với nước non\n")
f2 = create_replace_file("btn_2cc.txt","Rắn nát mặc dù tay kẻ nặn\nMà em vẫn giữ tấm lòng son\n")

read_f1 = read_file("btn_2cd.txt")
read_f2 = read_file("btn_2cc.txt")

all_line_f1 = readlines_file(read_f1)
all_line_f2 = readlines_file(read_f2)

# f1 = open("btn_2cd.txt","w", encoding="utf-8")
# f1_write = f1.write("Thân em vừa trắng lại vừa tròn\nBảy nổi ba chìm với nước non\n")
# f1.close()

# f2 = open("btn_2cc.txt","w", encoding="utf-8")
# f2_write = f2.write("Rắn nát mặc dù tay kẻ nặn\nMà em vẫn giữ tấm lòng son\n")
# f2.close()

f_final = open("btn.txt","w", encoding="utf-8")
f_final.write('Bánh trôi nước\n')

# read_f1 = open("btn_2cd.txt","r", encoding="utf-8")
# read_f2 = open("btn_2cc.txt","r", encoding="utf-8")

# all_line_f1 = read_f1.readlines()
# all_line_f2 = read_f2.readlines()

for line in all_line_f1:
    f_final.write(line)

for line in all_line_f2:
    f_final.write(line)

f_final.write('-------------')
f_final.write('Hồ Xuân Hương')
f_final.close()