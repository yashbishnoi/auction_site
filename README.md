# auction_site

Sample format for registration as Vendor and Bidder



URL- localhost:8000/register/

REQUEST FOR VENDOR

{
    "type":"Vendor",
    "first_name": "asassa",
    "last_name": "asasas",
    "email": "asdfgg@sdfg.asdfg",
    "password": "asasasas",
    "company_name": "asfdf",
    "mobile": "223322",
    "telephone": "324354",
    "address_line1": "24354fdfdfd",
    "address_line2": "wewf4tfv dsf",
    "city": "dsfffss",
    "pincode": "224421",
    "country": 2,
    "state": "sdsddssd"
}


REQUEST FOR BIDDER

{
    "type":"Bidder",
    "first_name": "asassa",
    "last_name": "asasas",
    "email": "asdfgg@sdfg.asdfg",
    "password": "asasasas",
    "company_name": "asfdf",
    "mobile": "223322",
    "telephone": "324354",
    "address_line1": "24354fdfdfd",
    "address_line2": "wewf4tfv dsf",
    "city": "dsfffss",
    "pincode": "224421",
    "country": 2,
    "state": "sdsddssd"
}

Response for bidder-

{
    "id": 1,
    "first_name": "asassa",
    "last_name": "asasas",
    "email": "asdfgg@sdfg.asdfg",
    "password": "asasasas",
    "company_name": "asfdf",
    "mobile": "223322",
    "telephone": "324354",
    "address_line1": "24354fdfdfd",
    "address_line2": "wewf4tfv dsf",
    "city": "dsfffss",
    "pincode": "224421",
    "country": 2,
    "state": "sdsddssd"
}




Sample format for login as Vendor and Bidder-

URL- localhost:8000/login/


REQUEST FOR VENDOR

{
    "type":"Vendor",
    "email": "asdfgg@sdfg.asdfg",
    "password": "asasasas"
}



REQUEST FOR BIDDER

{
    "type":"Bidder",
    "email": "asdfgg@sdfg.asdfg",
    "password": "asasasas"
}


Response FOR BIDDER

"Hi asassa! You are a great Bidder"

