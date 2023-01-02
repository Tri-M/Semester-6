package com.example.exercise6

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val fName = findViewById<EditText>(R.id.names)
        val lName = findViewById<EditText>(R.id.lastName)
        val phone = findViewById<EditText>(R.id.Phone)
        val bday = findViewById<EditText>(R.id.dob)

        val address = findViewById<EditText>(R.id.address)
        val submitBtn = findViewById<Button>(R.id.button)
    }
}