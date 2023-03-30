package com.example.emoji

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val button2 = findViewById(R.id.cookie) as Button

        button2.setOnClickListener{
            val myintent1 = Intent(this,MainActivity2::class.java)
            startActivity(myintent1)
        }

    }
}