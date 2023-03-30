package com.example.demo.service;
import java.util.List;

import com.example.demo.entity.Users;

public interface UserService {
    public List<Users> getAllUsers();
    public Users getUserById(int userId); 
    public Users addorUpdateUser(Users user);
    public Users deleteUser(int userId) throws Exception;


    
}
