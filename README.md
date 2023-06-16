This is a sentiment analyzer. It takes text as an input and gives the sentiment of the text as an output. I use distilbert-base-uncased-finetuned-sst-2-english model as my sentiment analysis model.

## Getting Started

```bash
pip install -r requirments.txt
```
Then run

```bash
python manage.py migrate
```
Then run 
```bash
python manage.py runserver
```
It will start the server.
Open [http://localhost:8000/analyze](http://localhost:8000/analyze) with your browser or postman to see the result.

Method: POST
```json
{"text":"your text"}
```


