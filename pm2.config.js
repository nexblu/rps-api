module.exports = {
  apps: [
    {
      name: 'rps-api',
      script: 'python3 -m uvicorn app.rps:app',
      args: '--host 0.0.0.0 --port 8000',
      instances: 1, // Jumlah instance yang ingin Anda jalankan
      exec_mode: 'cluster', // Mode eksekusi, bisa 'cluster' atau 'fork'
      watch: false, // Setel ke true jika ingin PM2 memantau perubahan file
      env: {
        NODE_ENV: 'production', // Atur environment jika perlu
      },
    },
  ],
};
