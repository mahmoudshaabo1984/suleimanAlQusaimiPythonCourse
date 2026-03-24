# Program 1: Text file operations (write, append, read)
# All open() calls include encoding="utf-8" for proper Arabic support

# ===== Part 1: Writing with mode "w" =====

# Open file data.txt in write mode "w" with utf-8 encoding
# If the file does not exist, Python creates it automatically
# If it exists, ALL old content is deleted
file = open("data.txt", "w", encoding="utf-8")

# Write a greeting inside the file using the write() method
file.write("السلام عليكم ورحمة الله وبركاته")

# Close the file to save changes - this step is essential
file.close()

# ===== Trying to write to a closed file =====

# If we try to write after closing, we get this error:
# ValueError: I/O operation on closed file.
# file.write("some text")  # <-- This would cause an error

# ===== Part 2: Rewriting with mode "w" (erases old content) =====

# Open the file again in "w" mode - this erases everything written before
file = open("data.txt", "w", encoding="utf-8")

# Write the word "python" - it replaces the old greeting
file.write("python")

# Close the file
file.close()

# ===== Part 3: Writing two strings with mode "w" =====

# Open the file again in "w" mode - erases content again
file = open("data.txt", "w", encoding="utf-8")

# Write first string
file.write("هذا نص")

# Write second string right after the first (no new line between them)
file.write("هذا نص آخر")

# Close the file
file.close()

# ===== Part 4: Appending with mode "a" =====

# Open the file in append mode "a"
# This mode adds new text at the end WITHOUT erasing old content
file = open("data.txt", "a", encoding="utf-8")

# Add new text at the end of the file (no new line)
file.write("سليمان القسيمي")

# Close the file
file.close()

# ===== Part 5: Appending with a new line =====

# Open the file in append mode again
file = open("data.txt", "a", encoding="utf-8")

# Add text on a NEW line using \n
# The character \n means: go to a new line before writing the text
file.write("\nسليمان القسيمي")

# Close the file
file.close()

# ===== Part 6: Another append with new line =====

# Open file in append mode with utf-8 encoding
file = open("data.txt", "a", encoding="utf-8")

# Add another line of Arabic text
file.write("\nسليمان القسيمي")

# Close the file
file.close()

# ===== Part 7: Reading with mode "r" =====

# Open the file in read mode "r" with utf-8 encoding
file = open("data.txt", "r", encoding="utf-8")

# Read the entire file content at once and store it in a variable
content = file.read()

# Print the content
print(content)

# ===== Part 8: Moving the read cursor with seek() =====

# After reading, the cursor is at the end of the file
# To move it back to the beginning we use seek(0)
# The number 0 means: go back to the first character in the file
file.seek(0)

# Close the file
file.close()

# ===== Part 9: Reading one line at a time with readline() =====

# Open the file for reading again
file = open("data.txt", "r", encoding="utf-8")

# Read only the first line
line1 = file.readline()
print("السطر الأول:", line1)

# Read the second line
line2 = file.readline()
print("السطر الثاني:", line2)

# Read the third line
line3 = file.readline()
print("السطر الثالث:", line3)

# Read the fourth line
line4 = file.readline()
print("السطر الرابع:", line4)

# If no lines remain, readline() returns an empty string ''
line5 = file.readline()
print("السطر الخامس (فارغ إذا انتهى الملف):", repr(line5))

# ===== Part 10: Reading all lines as a list with readlines() =====

# Move the cursor back to the beginning
file.seek(0)

# Read all lines and store them in a list
# Each line becomes one item in the list
lines = file.readlines()

# Access the first line using index 0
print("أول سطر:", lines[0])

# Access the last line using index -1
print("آخر سطر:", lines[-1])

# Close the file
file.close()

print("\n===== انتهى البرنامج الأول بنجاح =====")
