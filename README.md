# Surahealth API Documentation

This documentation provides details about the Surahealth API endpoints and their usage.

# Base URL

'http://surahealth-388810.et.r.appspot.com/'

Home
URL: '/'
Method: GET

This endpoint provides a welcome message and instructions on how to access the prediction.

Response
csharp
Hello, this is Surahealth API. To access the prediction, please enter your longitude and latitude on /v1/predict/your_longitude/your_latitude

Prediction
URL: /v1/predict/{longitude}/{latitude}
Method: GET

This endpoint allows you to retrieve predictions by providing longitude and latitude values.

Notes
Input your longitude and latitude on the URL. For example: /v1/predict/300/300

Response
The response will be a JSON array containing multiple objects representing hospital data. Each object will have the following attributes:

- Kode Rumah Sakit: Hospital code
- Nama Rumah Sakit: Hospital name
- Tipe: Hospital type
- Alamat: Hospital address
- Telepon: Hospital phone number
- Kelas: Hospital class
- Jumlah Bed: Number of beds
- BPJS: BPJS status
- Longitude: Hospital longitude
- Latitude: Hospital latitude
- Cluster: Hospital cluster
- Hospital Distance: Distance from the hospital (in a nested array)
 
Here's an example of a response object:
{
  "Kode Rumah Sakit": "3372234.0",
  "Nama Rumah Sakit": "RS Umum Daerah Ibu Fatmawati Soekarno",
  "Tipe": "C",
  "Alamat": "Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari",
  "Telepon": "0271-715300",
  "Kelas": "ICU",
  "Jumlah Bed": 5,
  "BPJS": 0,
  "Longitude": -0.1479292116,
  "Latitude": 2.5127901385,
  "Cluster": 4,
  "Hospital Distance": [[24369.4619669771]]
}
Please note that the above response is just an example, and you'll receive multiple objects in the actual response.

You can use this documentation as a starting point and add more details if needed. Make sure to update it whenever there are changes to the API endpoints or responses.

# SurahealthCC

Endpoint: http://surahealth-388810.et.r.appspot.com/

HOME

URL: '/'

Method : GET

RESPONSE

Hello, this is Surahealth API. To access the prediction, please enter your longitude and latitude on /v1/predict/your_longitude/your_latitude


PREDICTION

URL: /v1/predict/{longitude}/{latitude}

NOTES: Input your longitude and latitude on the URL. For example: /v1/predict/300/300

Method : GET


RESPONSE

[{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"ICU","Jumlah Bed":5,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]},{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"VVIP\/Super VIP","Jumlah Bed":0,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]},{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"VIP","Jumlah Bed":1,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]},{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"Kelas I","Jumlah Bed":9,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]},{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"Kelas II","Jumlah Bed":18,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]},{"Kode Rumah Sakit":"3372234.0","Nama Rumah Sakit":"RS Umum Daerah Ibu Fatmawati Soekarno","Tipe":"C","Alamat":"Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari","Telepon":"0271-715300","Kelas":"Kelas III","Jumlah Bed":72,"BPJS":0,"Longitude":-0.1479292116,"Latitude":2.5127901385,"Cluster":4,"Hospital Distance":[[24369.4619669771]]}]

