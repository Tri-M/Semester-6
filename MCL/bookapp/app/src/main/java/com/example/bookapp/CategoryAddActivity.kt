package com.example.bookapp

import android.app.ProgressDialog
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.swiperefreshlayout.widget.CircularProgressDrawable.ProgressDrawableSize
import com.example.bookapp.databinding.ActivityCategoryAddBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase

class CategoryAddActivity : AppCompatActivity() {
    private lateinit var binding:ActivityCategoryAddBinding
    private lateinit var firebaseAuth: FirebaseAuth
    private lateinit var progresDialog: ProgressDialog
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityCategoryAddBinding.inflate(layoutInflater)
        setContentView(binding.root)
        firebaseAuth=FirebaseAuth.getInstance()
        progresDialog= ProgressDialog(this)
        progresDialog.setTitle("Please wait")
        progresDialog.setCanceledOnTouchOutside(false)
        binding.backBtn.setOnClickListener {
            onBackPressed()
        }
        binding.submitBtn.setOnClickListener {
            validateData()
        }
    }
    private var category=""
    private fun validateData() {
        category=binding.categoryEt.text.toString().trim()
        if(category.isEmpty()){
            Toast.makeText(this,"Enter category",Toast.LENGTH_SHORT).show()
        }
        else
        {
            addCategoryFirebase()
        }
    }

    private fun addCategoryFirebase() {
        progresDialog.show()
        val timestamp=System.currentTimeMillis()
        val hashMap=HashMap<String,Any>()
        hashMap["id"]="$timestamp"
        hashMap["category"]=category
        hashMap["timestamp"]=timestamp
        hashMap["uid"]="${firebaseAuth.uid}"
        val ref=FirebaseDatabase.getInstance().getReference("Categories")
        ref.child("$timestamp")
            .setValue(hashMap)
            .addOnSuccessListener {
                progresDialog.dismiss()
                Toast.makeText(this,"Added successfully",Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener{e->
                progresDialog.dismiss()
                Toast.makeText(this,"Failed to add due to ${e.message}",Toast.LENGTH_SHORT).show()

            }
    }
}