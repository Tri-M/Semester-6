package com.example.buttonemoji

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val b = findViewById(R.id.button) as Button
        val img = findViewById<ImageView>(R.id.angry)
        val t = findViewById<TextView>(R.id.angry1)
        b.setOnClickListener{
            if (b.text=="EAT"){
                b.text="DONE"
                t.text="I'm so full"
                img.setImageResource(R.drawable.hungry)

            } else {
                b.text="EAT"
                t.text="I'm so hungry"
                img.setImageResource(R.drawable.angry)
            }
        }
    }
}