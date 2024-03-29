package com.example.bookapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.renderscript.Sampler.Value
import android.text.Editable
import android.text.TextWatcher
import com.example.bookapp.databinding.ActivityDashboardAdminBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener

class DashboardAdminActivity : AppCompatActivity() {
    private lateinit var binding:ActivityDashboardAdminBinding
    private lateinit var firebaseAuth: FirebaseAuth
    private lateinit var categoryArrayList: ArrayList<ModelCategory>
    private lateinit var adapterCategory: AdapterCategory
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityDashboardAdminBinding.inflate(layoutInflater)
        setContentView(binding.root)
        firebaseAuth=FirebaseAuth.getInstance()
        checkUser()
        loadCategories()
        binding.logoutBtn.setOnClickListener{
            firebaseAuth.signOut()
            checkUser()
            loadCategories()
            binding.searchEt.addTextChangedListener(object:TextWatcher{
                override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {
                    TODO("Not yet implemented")
                }

                override fun onTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {
                    TODO("Not yet implemented")
                    try{
                        adapterCategory.filter!!.filter(s)
                    }
                    catch(e:Exception){

                    }
                }

                override fun afterTextChanged(p0: Editable?) {
                    TODO("Not yet implemented")
                }
            })
        }
        binding.addCategoryBtn.setOnClickListener {
//            println("HELLO")
            startActivity(Intent(this,CategoryAddActivity::class.java))
        }

    }

    private fun loadCategories() {
        TODO("Not yet implemented")
        categoryArrayList= ArrayList()
        val ref=FirebaseDatabase.getInstance().getReference("Categories")
        ref.addValueEventListener(object:ValueEventListener{
            override fun onDataChange(snapshot: DataSnapshot){
                categoryArrayList.clear()
                for(ds in snapshot.children){
                    val model=ds.getValue(ModelCategory::class.java)
                    categoryArrayList.add(model!!)
                }
                adapterCategory= AdapterCategory(this@DashboardAdminActivity,categoryArrayList)
                binding.categoriesRv.adapter=adapterCategory
            }

            override fun onCancelled(error: DatabaseError) {
                TODO("Not yet implemented")
            }
        })
    }

    private fun checkUser() {
        val firebaseUser=firebaseAuth.currentUser
        if (firebaseUser==null){
            startActivity(Intent(this,MainActivity::class.java))
            finish()
        }
        else{
            val email=firebaseUser.email
            binding.subTitleTv.text=email
        }
    }
}
