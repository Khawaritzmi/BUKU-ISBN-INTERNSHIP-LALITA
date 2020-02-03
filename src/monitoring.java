package com.example.lalitachandiany.monitoring;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import id.co.telkom.iot.AntaresHTTPAPI;
import id.co.telkom.iot.AntaresResponse;

public class MonitoringActivity extends AppCompatActivity implements AntaresHTTPAPI.OnResponseListener {
  //Deklarasi button , text view dll atau deklarasi variabel
    private Button btnRefresh;
    private Button btnback;

    private TextView txtData, txtData2;
    private String TAG = "ANTARES-API";
    private AntaresHTTPAPI antaresAPIHTTP;
    private String dataDevice;

    private ProgressBar progressBar;
    private TextView persentase;
    private int Value;
    private int Hasil;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_monitoring);
// inisialisasi butron progresbar text view dll
        progressBar = findViewById(R.id.progress);
        persentase = findViewById(R.id.persentase);
        progressBar.setProgress(0); //Set Progress Dimulai Dari O

        // --- Inisialisasi UI yang digunakan di aplikasi --- //
        btnRefresh = (Button) findViewById(R.id.btnRefresh);
        btnback = (Button) findViewById(R.id.back);
        txtData = (TextView) findViewById(R.id.txtData);
        txtData2 = (TextView) findViewById(R.id.txtDatadua);

        // --- Inisialisasi API Antares --- //
        //antaresAPIHTTP = AntaresHTTPAPI.getInstance();
        antaresAPIHTTP = new AntaresHTTPAPI();
        antaresAPIHTTP.addListener(this);
        btnRefresh.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                antaresAPIHTTP.getLatestDataofDevice("d5e3724d6720d3e2:164864b3c1aef838","nodemcu-banjir","ketinggia-air");

            }
        });


        Button btnback = (Button) findViewById(R.id.back);
// setonclik merupakan method untuk memberikan perintah apa yg hrus di lakukan ketika klik buton
        btnback.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // TODO Auto-generated method stub
                startActivity(new Intent(MonitoringActivity.this, HomeActivity.class));
                finish();
            }
        });
    }



    @Override
    public void onResponse(AntaresResponse antaresResponse) {
        // --- Cetak hasil yang didapat dari ANTARES ke System Log --- //

        Log.d(TAG,Integer.toString(antaresResponse.getRequestCode()));
        if(antaresResponse.getRequestCode()==0){
            try {
                JSONObject body = new JSONObject(antaresResponse.getBody());
                dataDevice = body.getJSONObject("m2m:cin").getString("con");
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        //txtData.setText(dataDevice);
                        String s = dataDevice;
                        String parts[] = s.split(":");


                        txtData.setText(parts[1].substring(0,1));
                        Hasil = Integer.parseInt(parts[1].substring(0,1));
                        persentase.setText(String.valueOf(Hasil) + "m");
                        txtData2.setText(parts[2].substring(0,3));
                        final Handler handler = new Handler(){
                            @Override
                            public void handleMessage(Message msg) {
                                super.handleMessage(msg);
                                // Menampung semua data yang ingin diproses oleh thread
                                persentase.setText(String.valueOf(Value)+ "m");


                                if(Value == Hasil && Value != 0){
                                    Toast.makeText(getApplicationContext(), "Progress Completed", Toast.LENGTH_SHORT).show();
                                }
                                Value++;
                            }

                        };


                        Thread thread = new Thread(new Runnable() {
                            @Override
                            public void run() {
                                try{
                                    for(int w=0; w<=Hasil; w++){
                                        progressBar.setProgress(w); // Memasukan Value pada ProgressBar
                                        // Mengirim pesan dari handler, untuk diproses didalam thread
                                        handler.sendMessage(handler.obtainMessage());
                                        Thread.sleep(100); // Waktu Pending 100ms/0.1 detik
                                    }
                                }catch(InterruptedException ex){
                                    ex.printStackTrace();
                                }
                            }
                        });
                        thread.start();



                    }
                });
                Log.d(TAG,dataDevice);
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
}
