students=['Đạt 1 lít', 'Lít mai bôn', 'Khốn lành']
for student in students:
    print(student)
print(students[1])
students.append("Táo Anh Đuân") # them vao cuoi danh sach
#them vao vi tri cu the
students.insert(10,"Việt Vị")
print(students)
# noi 1 danh sach vao
students.extend(['1','2','3'])
students+=['5','4','4']
print(students)

# xoa theo gtri
students.remove('Khốn lành')

#xoa theo chi so'
students.pop(0)
# xoa theo danh sach
del students[:3]
print(students)

for i, student in enumerate(students):
    print(f'{i}.student')