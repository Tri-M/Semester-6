package com.example.weather.Services;

import com.example.weather.Model.WeatherModel;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.List;


public interface WeatherService {
    JsonNode getWeatherData(String s) throws JsonProcessingException;
    List<WeatherModel> getData();
}
