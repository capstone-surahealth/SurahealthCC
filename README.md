# Surahealth API Documentation

Endpoint: http://surahealth-388810.et.r.appspot.com/

Introduction
The Surahealth API provides hospital recommendations based on latitude and longitude coordinates. It uses a machine learning model to predict the class and recommend hospitals based on the user's location.


# Hello
	URL: "/"
	Method: GET
	Description: Returns a welcome message and instructions on how to access the prediction.
	Headers: None
	Parameters: None
	Response:
	Status: 200 OK
	Body: "Hello, this is Surahealth API. To access the prediction, please enter your longitude and latitude on /v1/predict/your_longitude/your_latitude"
	
# Predict Recommended Hospitals
	URL: /v1/predict/<Longitude>/<Latitude>
	Method: GET
	Description: Predicts the class and recommends hospitals based on the provided longitude and latitude.
	Headers: None
	Parameters:
	<Longitude> (float): The longitude coordinate of the user's location.
	<Latitude> (float): The latitude coordinate of the user's location.
	Response:
	Status: 200 OK
	Body: JSON array containing the recommended hospitals' information.
	Example URL: http://surahealth-388810.et.r.appspot.com/v1/predict/2.5127901385/-0.1479292116
	Example Response:

	[
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
    },
    {
        "Kode Rumah Sakit": "3372234.0",
        "Nama Rumah Sakit": "RS Umum Daerah Ibu Fatmawati Soekarno",
        "Tipe": "C",
        "Alamat": "Jl. Lettu Sumarto No. 1 Kel. Kadipiro Kec. Banjarsari",
        "Telepon": "0271-715300",
        "Kelas": "VVIP/Super VIP",
        "Jumlah Bed": 0,
        "BPJS": 0,
        "Longitude": -0.1479292116,
        "Latitude": 2.5127901385,
        "Cluster": 4,
        "Hospital Distance": [[24369.4619669771]]
    },
    ...
	]
	Headers
	The API does not require any headers.

	Response
	The API responds with JSON data containing information about the recommended hospitals. The response includes the following fields for each hospital:

	Kode Rumah Sakit: Hospital code
	Nama Rumah Sakit: Hospital name
	Tipe: Type of hospital
	Alamat: Hospital address
	Telepon: Hospital contact number
	Kelas: Class of the hospital
	Jumlah Bed: Number of beds in the hospital
	BPJS: Indicator of whether the hospital accepts BPJS (0 for no, 1 for yes)
	Longitude: Longitude coordinate of the hospital
	Latitude: Latitude coordinate of the hospital
	Cluster: Cluster number
	Hospital Distance: Distance between the user's location and the hospital
	Please note that the response may contain multiple hospitals, and the number of hospitals returned can be customized by changing the value of the n variable in the code.
