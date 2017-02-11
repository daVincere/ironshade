package edu.sfsu.cs.orange.ocr;

import android.app.Activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import edu.sfsu.cs.orange.ocr.language.StringInfo;

/**
 * Created by jaskaran singh on 2/11/2017.
 */

public class MainActivity extends Activity {

    ImageView Scan_medicine,Scan_report;
    ImageView emergency;
    StringInfo stringinfo;
    String Came_from_scanning;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Scan_medicine=(ImageView) findViewById(R.id.imageView2);
        Scan_report=(ImageView) findViewById(R.id.imageView3);
        emergency=(ImageView)findViewById(R.id.imageView);
        stringinfo=new StringInfo();


    }
    public void fun(View v){
        if(v.getId()==R.id.image_view){
            Intent i=new Intent(MainActivity.this,Emergency.class);
            startActivity(i);
            //stringinfo.setAbc();
        }
        else {
            Intent i2 = new Intent(MainActivity.this, R.class);
            startActivity(i2);
        }
    }

}
