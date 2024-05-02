# Chatbot for Abaya's Store using Keras
- [Description](#description)
- [Prerequisite](#prerequisite)
- [Instructions](#instructions)
- [Files Descriptions](#files-descriptions)
- [Limitations](#limitations)
- [Resources](#resources)


## Description
In the current retail landscape, a significant number of customers prefer to engage with stores prior to making a purchase or visiting in person. However, many stores lack dedicated customer support personnel. This project aims to alleviate this issue by developing a chatbot designed to handle Frequently Asked Questions (FAQs) in a user-friendly manner, thereby reducing the workload on store employees.

The chatbot has been specifically designed for Abayas, a type of clothing worn by Muslims in Saudi Arabia. The chatbot is highly customizable and can be tailored to suit specific needs by modifying the data\intents.json file. This flexibility allows for a more personalized and efficient customer service experience.

## Prerequisite
1. Install Python version 3.11.1
2. Install Flask.

## Instructions:
1. Run `app.py`.
2. Open the terminal on your `IDE`.
3. Click on the link after the phrase `* Running on...`.
4. App will be opend in your browser.
5. Use `Arabic` for chatting with the chatbot in your browser.
   

## Files Descriptions
1. `data_preparing.py`: Prepare `data/dataset.csv` from `intents.json` file.
2. `preprocessing.py`: Required preprocessing steps for text data.
3. `train.py`: Build model.
4. `test.py`: Test model response.
5. `app.py`: Run user interface.

## Limitations
1. Small data size in `intents.json`.
2. Data is generated personally, this may not reflect the real-world Abaya store experience.
3. Can't handle continuous conversation.

## Resources
[Creating Chatbots Using TensorFlow | Edureka](https://www.youtube.com/live/BBUvl9C6D-0?si=a8fh8sZ74XL4rDhd)

[User Interface from binary hood](https://github.com/binary-hood/ChatBot)






