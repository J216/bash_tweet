
# bash_tweet

bash script using python script to send tweet of image and or status update text.

## Getting Started
Example Status Update
```
tweet 'Your tweet here' 
```
Example Tweet Image
```
tweet 'Your image tweet here' /path/to/your/image.jpg
```

### Prerequisites

Python and the following modules are required

```
TwitterAPI
```

### Installing


Copy the bash and Python script to /usr/bin/

```
sudo mv ./tweet /usr/bin/tweet
sudo mv ./tweet.py /usr/bin/tweet.py
```

Add folder and file for storing Twitter API key

```
python set-api-key.py
```


