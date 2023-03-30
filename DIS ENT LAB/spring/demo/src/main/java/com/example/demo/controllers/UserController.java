package com.example.demo.controllers;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demo.entity.Users;
import com.example.demo.service.UserService;

@RestController
@RequestMapping("/users")

public class UserController {
    private UserService userService;
    @GetMapping("/allUsers")
    public ResponseEntity<List<Users>> getAllUsers(){
        List<Users> users=null;
        try{
            users=userService.getAllUsers();
            // if(users==null)
            // {
            //     throw new Exception("No users found");
            // }
        }
        catch(Exception ex)
        {
            ex.getMessage();
        }
        return new ResponseEntity<List<Users>>(users,HttpStatus.OK);
    }
    
}
