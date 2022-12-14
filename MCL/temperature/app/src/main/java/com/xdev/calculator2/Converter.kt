package com.xdev.calculator2

class Converter {
    fun ReamurToCelcius(i: Float): Float {
        var celciusResult: Float = i * 4/5
        return celciusResult;
    }

    fun CelciusToReamur(i: Float): Float {
        var reamurResult: Float = i * 5/4
        return reamurResult
    }

    fun KelvinToCelcius(i: Float): Float {
        var celciusResult: Float = i - 273
        return celciusResult
    }

    fun CelciusToKelvin(i: Float): Float {
        var kelvinResult: Float = 273 - i
        return kelvinResult
    }

    fun FahrenheitToCelcius(i: Float): Float {
        var celciusResult: Float = (i * 9/5) + 32
        return celciusResult
    }

    fun CelciusToFahrenheit(i: Float): Float {
        var fahrenheitResult: Float = (i - 32) * 5/9
        return fahrenheitResult
    }
}