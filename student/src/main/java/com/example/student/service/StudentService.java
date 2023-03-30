package com.example.student.service;
import java.util.List;
import com.example.student.entity.Student;
public interface StudentService {
	List<Student> getAllStudents();
	
	Student saveStudent(Student student);
	
	Student getStudentById(int id);
	
	Student updateStudent(Student student);
	
	void deleteStudentById(Long id);
}
