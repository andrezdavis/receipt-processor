# Receipt Processor
## API
The API endpoints are the following:

<code>receipts/process/</code> methods: <code>POST</code>

<code>receipts/<:id>/points/</code> methods: <code>GET</code>

accessed from the localhost after running the application <code>http://127.0.0.1:5000/</code>

## Docker Setup
The repo contains a Dockerfile that will generate an image with <code>docker build -t receipt-processor-python .</code>

Have Docker Desktop/Client open to then run <code>docker run -d -p 5000:5000 receipt-processor-python</code>

