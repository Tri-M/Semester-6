package com.example.demo.service;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.Users;
import com.example.demo.repository.UserRepository;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserRepository userRepository;
    @Override
    public List<Users>getAllUsers()
    {
        return (List<Users>) userRepository.findAll();
    }
    @Override
    public Users getUserById(int userId)
    {
        return userRepository.findById(userId).orElse(null);
    }

    @Override
    public Users addorUpdateUser(Users user) {
        // TODO Auto-generated method stub
        return userRepository.save(user);
    }
    @Override
    public Users deleteUser(int userId) throws Exception
    {
        Users deletedUser=null;
        try{
            deletedUser=userRepository.findById(userId).orElse(null);
            if(deletedUser==null)
            {
                throw new Exception("user not found");
            }
            else
            {
                userRepository.deleteById(userId);
            }
        }
        catch(Exception ex){
            throw ex;
        }
        return deletedUser;
    }
}
