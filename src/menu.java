/inisialisasi
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
