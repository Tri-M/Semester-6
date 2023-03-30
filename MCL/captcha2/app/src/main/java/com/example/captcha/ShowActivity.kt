package com.example.captcha


import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ShowActivity : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_show)
        val displayText=findViewById<TextView>(R.id.displayField);
        val prevBtn=findViewById<Button>(R.id.prevBtn);
        val intent=intent;
        var str = "{\n\t\t\tmobile:";
        str += intent.getStringExtra("mobNum");
        str += ",\n\t\t\tstatus:";
        str += intent.getStringExtra("message");
        str += ",\n}";

        displayText.text = str;

        prevBtn.setOnClickListener{
            finish();
        }

    }
}
