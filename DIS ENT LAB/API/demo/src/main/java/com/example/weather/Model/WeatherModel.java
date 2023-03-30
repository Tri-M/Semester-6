package com.example.weather.Model;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table
public class WeatherModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Integer id;
    @Column
    Date date;
    @Column
    double temp;
    @Column
    String city;

    public WeatherModel() {
    }

    public WeatherModel(Date date, double temp, String city) {
        this.date = date;
        this.temp = temp;
        this.city = city;
    }

    public Integer getId() {
        return id;
    }

    public Date getDate() {
        return date;
    }

    public double getTemp() {
        return temp;
    }

    public String getCity() {
        return city;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public void setTemp(double temp) {
        this.temp = temp;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
