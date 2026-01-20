import os

src_img_name = input("Nhập tên file cần copy: ").strip()

if os.path.exists(src_img_name):
    new_name = input("Nhập tên mới cho file (Enter bỏ qua lấy tên mặc định của file cũ) : ").strip()

    old_file = open(src_img_name,'rb')
    data_binary = old_file.read()

    if new_name == "":
        name,ext = os.path.splitext(src_img_name)
        new_src_img_name = name + "_copy_1" + ext

        new_file = open(new_src_img_name,'wb')
        new_file.write(data_binary)

        print("Đã copy file mới")
else:
    print("File ảnh không tồn tại")