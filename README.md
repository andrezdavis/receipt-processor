# Receipt Processor
## API
The API endpoints are the following:
### Create Receipt
<code>receipts/process/</code> methods: <code>POST</code> - where a receipt is created with the following:

```
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```

### Get Points
<code>receipts/{id}/points/</code> methods: <code>GET</code> - where a receipt, selected by its id, is processed for the total points it is eligible for

The endpoints are accessible via localhost <code>http://127.0.0.1:5000/</code>

## Docker Setup
The repo contains a Dockerfile that will generate an image with <code>docker build -t receipt-processor-python .</code>

Have Docker Desktop/Client open to then run <code>docker run -d -p 5000:5000 receipt-processor-python</code>

## Testing
For ease of use, access endpoints with cURL in a BASH or Linux terminal:
### Create Receipt
```
curl -H "Content-Type: application/json" \
-d '{
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
        {
        "shortDescription": "Gatorade",
        "price": "2.25"
        },{
        "shortDescription": "Gatorade",
        "price": "2.25"
        },{
        "shortDescription": "Gatorade",
        "price": "2.25"
        },{
        "shortDescription": "Gatorade",
        "price": "2.25"
        }
    ],
    "total": "9.00"
}' \
http://127.0.0.1:5000/receipts/process
```
### Get Points
```
curl -H "Content-Type: application/json" http://127.0.0.1:5000/receipts/:id/points
```

