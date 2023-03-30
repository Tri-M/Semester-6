package com.example.weather.repository;

import com.example.weather.Model.WeatherModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WeatherRepo extends JpaRepository<WeatherModel, Integer> {
    List<WeatherModel> findAllByOrderByIdDesc();
}
