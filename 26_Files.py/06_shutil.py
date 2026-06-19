import shutil

shutil.rmtree("delete")
shutil.copy("myinfo.txt", "Ayush.txt")
shutil.move("move_me.txt","delete/")
shutil.move("move2.txt","fake_for_code/fake/")