package com.example.chatapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toolbar
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.viewpager.widget.PagerAdapter
import androidx.viewpager2.adapter.FragmentStateAdapter
import androidx.viewpager2.widget.ViewPager2
import com.google.android.material.tabs.TabLayout
import com.google.android.material.tabs.TabLayoutMediator

class MainActivity : AppCompatActivity() {
    private lateinit var viewPager2:ViewPager2
    private lateinit var tabLayout: TabLayout
    private lateinit var appPagerAdapter: AppPagerAdapter
    private val titles= arrayListOf("Chat","Status","Calls")
    private lateinit var toolbar: androidx.appcompat.widget.Toolbar
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        toolbar=findViewById(R.id.toolbarMain)
        tabLayout=findViewById(R.id.tabLayoutMain)
        viewPager2=findViewById(R.id.viewPager2Main)
        toolbar.title="Chat app"
        setSupportActionBar(toolbar)
        appPagerAdapter= AppPagerAdapter(this)
        viewPager2.adapter=appPagerAdapter
        TabLayoutMediator(tabLayout.viewPager2){
            tab.position->
            tab.text=titles[position]

        }

    }
    class AppPagerAdapter(fragmentActivity: FragmentActivity):FragmentStateAdapter(fragmentActivity)
    {
        override fun getItemCount(): Int {
            return 3
        }
        override fun createFragment(position:Int):Fragment{
            return when(position)
            {
                0->Chats()
                2->Status()
                3->Calls()
                else->Chats()
            }
        }

    }
}