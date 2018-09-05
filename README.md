
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


Run script to copy the bash and Python script to /usr/bin/ and creates api key in user home folder

```
sudo setup.sh
```

Run the following to change/set your api key, setup.sh automatically runs this. You can run it again later to change your api keys.

```
python set-api-key.py
```


