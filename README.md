# MockupToCode



*Generating HTML Code from a hand-drawn mockup*



MockupToCode is a deep learning model that takes hand-drawn web mockups and converts them into working HTML code. It uses keras which provides interface for artificial neural networks for training the model. 
<b>Note:</b> This project can only give HTML for inputs resembling to the core dataset and not genralized data.</br> Dataset source: Tony beltramelli's mockup dataset


## Setup

### Install dependencies

```sh
pip install -r requirements.txt
```
### Download [data](http://sketch-code.s3.amazonaws.com/data/all_data.zip) to train the model
 

Unzip the data and use it for the training of the model.

Train the model:
```sh
python3 train.py 
```
Note : It will ask for paths. Specify the appropiate inputs. 


