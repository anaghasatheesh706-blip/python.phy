
frontend_students = {"Alice", "Bob", "Charlie", "David"}
backend_students = {"Charlie", "Eve", "Frank", "Grace"}
backend_students.add("Heidi")
frontend_students.remove("David")
print(f"Frontend Students: {frontend_students}")
print(f"Backend Students: {backend_students}")
 
 
enrolled_in_both = frontend_students.intersection(backend_students)
print(f"Students enrolled in both courses: {enrolled_in_both}")
only_backend = backend_students.difference(frontend_students)
print(f"Students enrolled only in Backend: {only_backend}")
 

unique_students = frontend_students.union(backend_students)
print(f"Total number of unique students: {len(unique_students)}")


course_enrollments = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
for course, count in course_enrollments.items():
    print(f"Course: {course}, Students: {count}")
    
fullstack_enrollments = {
    course: count for course, count in course_enrollments.items()
}
fullstack_enrollments["Fullstack"] = len(frontend_students) + len(only_backend)

print(f"Fullstack Enrollments Dictionary: {fullstack_enrollments}")