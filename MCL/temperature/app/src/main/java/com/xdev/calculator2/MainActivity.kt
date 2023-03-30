package com.xdev.calculator2

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextUtils
import android.text.TextWatcher
import android.view.View
import android.widget.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        
        var et1: EditText = findViewById(R.id.input1)
        var et2: EditText = findViewById(R.id.input2)
        var spinner1: Spinner = findViewById(R.id.spinner1)

        var spinner1Stat: String = ""

        var val1: Float = 0f

        var val1String: String

        var resultVal1: Float

        var resVal1: String

        var convert: Converter = Converter()

        ArrayAdapter.createFromResource(this, R.array.Temperature,
            android.R.layout.simple_spinner_item).also {
            adapter ->
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            spinner1.adapter = adapter
        }


        //Convertion Function
        fun ConvertionFromInput1(spinner1Stat: String, value: Float): Float {
            if (spinner1Stat.equals("Reamur to Celcius", true)){
                resultVal1 = convert.ReamurToCelcius(value)
                return resultVal1
            } else if (spinner1Stat.equals("Celcius to Reamur", true)){
                resultVal1 = convert.CelciusToReamur(value)
                return resultVal1
            } else if (spinner1Stat.equals("Celcius to Kelvin", true)){
                resultVal1 = convert.CelciusToKelvin(value)
                return resultVal1
            } else if (spinner1Stat.equals("Kelvin to Celcius", true)) {
                resultVal1 = convert.KelvinToCelcius(value)
                return resultVal1
            } else if (spinner1Stat.equals("Celcius to Fahrenheit", true)){
                resultVal1 = convert.CelciusToFahrenheit(value)
                return resultVal1
            } else if (spinner1Stat.equals("Fahrenheit to Celcius", true)){
                resultVal1 = convert.FahrenheitToCelcius(value)
                return resultVal1
            }
            return 0f
        }
        //Listener Text Changed
        et1.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(p0: Editable?) {

            }

            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun onTextChanged(string: CharSequence?, p1: Int, p2: Int, p3: Int) {
                val1String = et1.text.toString()
                val1 = val1String.toFloat()
                resultVal1 = ConvertionFromInput1(spinner1Stat, val1)
                resVal1 = resultVal1.toString()
                et2.setText(resVal1)
            }
        })

        //Spinner Selected Listener
        spinner1.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onNothingSelected(p0: AdapterView<*>?) {
                TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
            }

            override fun onItemSelected(parent: AdapterView<*>, view: View, pos: Int, id: Long) {
                spinner1Stat = parent.getItemAtPosition(pos).toString()
                resultVal1 = ConvertionFromInput1(spinner1Stat, val1)
                resVal1 = resultVal1.toString()
                et2.setText(resVal1)
            }
        }
    }
}
