package com.example.weather.Services;

import com.example.weather.Model.WeatherModel;
import com.example.weather.repository.WeatherRepo;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

@Service
public class WeatherServiceImpl implements WeatherService {
    @Autowired
    private WeatherRepo weatherRepo;

    public JsonNode getWeatherData(String c) throws JsonProcessingException {
        RestTemplate restTemplate = new RestTemplate();
        String URL = "https://api.openweathermap.org/data/2.5/weather?q="+c+"&appid=4aaf3f194039c2eae46d6693c587b8d8";
        String data = restTemplate.getForObject(URL, String.class);

        ObjectMapper objectMapper = new ObjectMapper();
        JsonNode jsonNode = objectMapper.readTree(data);
//        System.out.println(jsonNode.get("main").get("temp").asText());

        DateFormat df = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date d = new Date();
        df.format(d);

        weatherRepo.save(new WeatherModel(d,jsonNode.get("main").get("temp").asDouble(),jsonNode.get("name").asText()));
        return jsonNode;
    }

    public List<WeatherModel> getData(){
        return weatherRepo.findAllByOrderByIdDesc();
    }
}
