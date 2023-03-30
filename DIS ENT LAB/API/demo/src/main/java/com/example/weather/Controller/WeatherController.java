package com.example.weather.Controller;

import com.example.weather.Model.WeatherModel;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.ui.Model;
import com.example.weather.Services.WeatherServiceImpl;
import com.fasterxml.jackson.core.JsonProcessingException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class WeatherController {

    @Autowired
    private WeatherServiceImpl weatherService;

    @GetMapping("/")
    public String WeatherData(Model model) {
        model.addAttribute("city", "");
        model.addAttribute("temp", "");
        return "form";
    }

    @PostMapping("/query-city")
    public String getWeather(@RequestParam("city") String city, Model model) throws JsonProcessingException {
        JsonNode jsonNode = weatherService.getWeatherData(city);
        model.addAttribute("city", city);
        model.addAttribute("temp", jsonNode.get("main").get("temp").asText());
        return "form";
    }

    @GetMapping("/history")
    public String getHistory(Model model) {
        List<WeatherModel> temperatures = weatherService.getData();
        model.addAttribute("temperatures", temperatures);
        return "history";
    }
}
