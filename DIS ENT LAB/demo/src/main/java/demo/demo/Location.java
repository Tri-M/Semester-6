package demo.demo;

public class Location {
    private String name;
    private String country;

    public Location(String name, String country) {
        this.name = name;
        this.country = country;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return this.name;
    }
    public void setCountry(String country) {
        this.country = country;
    }
    public String getCountry() {
        return this.country;
    }
    
}

