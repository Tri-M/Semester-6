package com.example.captcha

import android.content.Intent
import android.graphics.Paint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val mobileField= findViewById<EditText>(R.id.mobileField)
        val captchaField=findViewById<TextView>(R.id.captchaField)
        val userInput=findViewById<EditText>(R.id.userInput)
        val submitBtn=findViewById<Button>(R.id.submitBtn)

        captchaField.apply {
            paintFlags = paintFlags or Paint.STRIKE_THRU_TEXT_FLAG
            text = makeCaptcha();

            submitBtn.setOnClickListener {
                if (mobileField.text.toString().matches(Regex("^([+]\\d{2})?\\d{10}\$"))) {
                    val intent: Intent = Intent(applicationContext, ShowActivity::class.java);
                    println(userInput.text.toString() + "AND" + captchaField.text.toString());
                    if(userInput.text.toString() == captchaField.text.toString()) {
                        intent.putExtra("mobNum", mobileField.text.toString());
                        intent.putExtra("message", "AUTH_SUCCESS");
                        startActivity(intent);
                    } else {
                        Toast.makeText(applicationContext, "Wrong captcha.", Toast.LENGTH_SHORT).show();
                    }
                } else {
                    Toast.makeText(applicationContext, "Invalid mobile number.", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }



    private fun makeCaptcha(): String {
        var captcha=""
        for(i in 1..5)
        {
            captcha+=(0..9).random()
        }
        return captcha;

    }
}