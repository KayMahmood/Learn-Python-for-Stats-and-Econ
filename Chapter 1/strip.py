#strip.py
spaces = "    Look at all the spaces in the text!    "
print("no spaces removed:\n", spaces)

remove_left_spaces = spaces.lstrip()
remove_right_spaces = spaces.rstrip()
remove_left_and_right_spaces = spaces.strip()

print("Remove left spaces:\n" + remove_left_spaces)
print("Remove right spaces:\n" + remove_right_spaces)
print("Remove left and right spaces:\n" + remove_left_and_right_spaces)

