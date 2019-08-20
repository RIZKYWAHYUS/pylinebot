# pylinebot
Opensource code untuk membuat Line Bot menggunakan bahasa python dan memanfaatkan layanan AWS


## Cara Penggunaan :
1. Buat Line Bot Channel di https://developers.line.biz/en/
2. Buat AWS Lambda Function yang memiliki trigger API Gateway
3. Buat RDS dengan engine DB MySQL
4. Download source code di repository ini, extract !
5. Ganti LINE_ACCESS_TOKEN dengan punyamu di dalam file lambda_function.py 
6. Ganti Konfigurasi DB RDS dengan punyamu di dalam file rds_config.py
7. Zip semuanya lagi
8. Upload di Lambda Function
9. Ubah isian Handler jadi ini "lambda_function.lambda_handler"
10. Copy URL endpoint API Gateway punyanya Lambda Function 
11. Paste URL adi ke isian URL Webhook di Line Developer
12. Selesai. Bertemanlah dengan Bot Line mu !




### Sumber Belajar dan Inspirasi :
https://ubunifu.co/aws/line-bot-aws-lambda-python 
https://github.com/c-bata/chalice-linebot
https://www.isc.upenn.edu/accessing-mysql-databases-aws-python-lambda-function
https://blog.skbali.com/2018/11/aws-lambda-layer-example-in-python/
