package com.example.lalitachandiany.monitoring;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

import com.daimajia.slider.library.Animations.DescriptionAnimation;
import com.daimajia.slider.library.SliderLayout;
import com.daimajia.slider.library.SliderTypes.BaseSliderView;
import com.daimajia.slider.library.SliderTypes.TextSliderView;

import java.util.HashMap;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        //inisialisasi
        SliderLayout sliderLayout = (SliderLayout) findViewById(R.id.slider);
        // Load image dari URL
        // Load Image Dari res/drawable
        HashMap<String,Integer> file_maps = new HashMap<String, Integer>();
        file_maps.put("Sudahkah Anda Siap",R.drawable.siap);
        file_maps.put("Bersihkan Sampah",R.drawable.sungai);
        file_maps.put("Banjir",R.drawable.banjirempat);
        file_maps.put("Tampilan Prototipe", R.drawable.full);
        for(String name : file_maps.keySet()){
            TextSliderView textSliderView = new TextSliderView(this);
            // initialize a SliderLayout
            textSliderView
                    .description(name)
                    .image(file_maps.get(name))
                    .setScaleType(BaseSliderView.ScaleType.Fit);
            //add your extra information
            textSliderView.bundle(new Bundle());
            textSliderView.getBundle()
                    .putString("extra",name);
            sliderLayout.addSlider(textSliderView);
        }
        sliderLayout.setPresetTransformer(SliderLayout.Transformer.Accordion);
        sliderLayout.setPresetIndicator(SliderLayout.PresetIndicators.Center_Bottom);
        sliderLayout.setCustomAnimation(new DescriptionAnimation());
        sliderLayout.setDuration(4000);


//inisialisasi
    ImageView awas = findViewById(R.id.awas);
        ImageView air = findViewById(R.id.air);
        ImageView banjir = findViewById(R.id.banjir);
        ImageView panic = findViewById(R.id.panic);

        awas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent awas = new Intent(HomeActivity.this, MonitoringActivity.class);
                startActivity(awas);
            }
        });

        banjir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent banjir = new Intent(HomeActivity.this, AboutActivity.class);
                startActivity(banjir);
            }
        });

        air.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent air = new Intent(HomeActivity.this, AirActivity.class);
                startActivity(air);
            }
        });

        panic.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent panic = new Intent(HomeActivity.this, PanicActivity.class);
                startActivity(panic);
            }
        });
    }
}
