import com.accuweather.AccuweatherAPI;
import com.accuweather.AccuweatherAPIException;
import com.accuweather.location.City;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class WeatherController {
    private static final String API_KEY = "YOUR_API_KEY_HERE";

    @GetMapping("/")
    public String showForm() {
        return "locationForm";
    }

    @RequestMapping("/current-location")
    public String getCurrentLocation(String cityName, Model model) {
        try {
            City city = AccuweatherAPI.getCurrentCity(API_KEY, cityName);
            Location location = new Location(city.getName(), city.getCountry().getName());
            model.addAttribute("location", location);
        } catch (AccuweatherAPIException e) {
            model.addAttribute("error", "Error fetching current location: " + e.getMessage());
        }

        return "currentLocation";
    }
}
