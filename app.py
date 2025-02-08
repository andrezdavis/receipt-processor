from flask import Flask, request, jsonify
from db import receipts
import uuid
from util import calculatePoints

app = Flask(__name__)
app.debug = True

@app.post("/receipts/process")
def post_receipt():
    receipt_data = request.get_json()
    id = uuid.uuid4().hex
    receipt = {**receipt_data, "id": id}
    receipts[id] = receipt

    return receipts[id]

@app.get("/receipts/<string:id>/points")
def get_points(id):
    receipt = receipts[id]
    points = calculatePoints.alphaNumericCalc(receipt['retailer'])
    if calculatePoints.roundDollar(receipt['total']): points += 50
    if calculatePoints.multiple25(receipt['total']): points += 25
    points += calculatePoints.lenOfItemsCalc(receipt['items'])
    points += calculatePoints.parseItems(receipt['items'])
    if calculatePoints.getDayIsOdd(receipt['purchaseDate']): points += 6
    if calculatePoints.checkTimes(receipt['purchaseTime']): points += 10
    
    return {"points": points}
    

if __name__ == '__main__':
    app.run()
