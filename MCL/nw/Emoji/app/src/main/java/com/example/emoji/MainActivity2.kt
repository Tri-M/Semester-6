package com.example.emoji

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity


class MainActivity2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        val button2 = findViewById(R.id.Done) as Button

        button2.setOnClickListener{
            val myintent = Intent(this,MainActivity::class.java)
            startActivity(myintent)
        }

    }
}