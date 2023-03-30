package com.example.bookapp

import android.app.ProgressDialog
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.bookapp.databinding.ActivityPdfAddBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener

class PdfAddActivity : AppCompatActivity() {
    private lateinit var binding: ActivityPdfAddBinding
    private lateinit var firebaseAuth: FirebaseAuth
    private lateinit var progressDialog: ProgressDialog
    private lateinit var categoryArrayList: ArrayList<ModelCategory>
    private var pdfUri: Uri? =null
    private val TAG="PDF_ADD_TAG"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPdfAddBinding.inflate(layoutInflater)
        setContentView(binding.root)
        firebaseAuth=FirebaseAuth.getInstance()
//        loadPdfCategories()

        progressDialog= ProgressDialog(this)
        progressDialog.setTitle("Please Wait")
        progressDialog.setCanceledOnTouchOutside(false)


    }

//    private fun loadPdfCategories() {
//        Log.d(TAG,"loadPdfCategories:Loading Pdf Categories")
//        categoryArrayList = ArrayList()
//        val ref=FirebaseDatabase.getInstance().getReference("Categories")
//        ref.addListenerForSingleValueEvent(object:ValueEventListener{
//            override fun onDataChange(snapshot: DataSnapshot){
//                categoryArrayList.clear()
//
//            }
//        })
//    }
}