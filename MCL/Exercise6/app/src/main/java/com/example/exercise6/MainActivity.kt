package com.example.exercise6

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
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
        val email = findViewById<EditText>(R.id.email)
        val bday = findViewById<EditText>(R.id.dob)
        val gender = findViewById<Spinner>(R.id.gender)
        val address = findViewById<EditText>(R.id.address)
        val submitBtn = findViewById<Button>(R.id.submitBtn)


        ArrayAdapter.createFromResource(
            this,
            R.array.genderOptions,
            android.R.layout.simple_spinner_item
        ).also { adapter ->
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            gender.adapter = adapter
        }


        submitBtn.setOnClickListener {
            intent = Intent(this, MiddleActivity::class.java);
            intent.putExtra("fName", fName.text.toString());
            intent.putExtra("lName", lName.text.toString());
            intent.putExtra("phone", phone.text.toString());
            intent.putExtra("email", email.text.toString());
            intent.putExtra("dob", bday.text.toString());
            intent.putExtra("gender", gender.selectedItem.toString());
            intent.putExtra("address", address.text.toString());
            startActivity(intent);
        }
    }


}