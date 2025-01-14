
# Module 01 : Introduction of Generative AI (Gen AI) 			#

## What is Generative AI

Traditionally machine learning is used to predict and take decission based on input data and trained models.
Difference in Gen AI is it can generate new contents rather than supporting only in decision making.
Few examples for generative AI are creating a code snippet using chat GPT or creating a new image using DALL-E

## What is Machine Learning

Machine learning is a branch of AI used to train and develop models which perform specific tasks which human brain is capable of doing.
For training models you will need huge amount of data and algorithms which can use those data to train the models

## What is Deep Learning

Deep learning is used to deal with much more complex problems in machine learning not only for identifying objects or taking simple decission.
They are the replication of how human brain operates with cluster of neurons to process some information and get an output out of that.
'Neural network' is one of the ket technology used to perform Deep learning to solve the complex problems.

Below is a hierarchical diagram which described how each of these are linked
![Diagram](https://github.com/user-attachments/assets/9876b90f-75b7-432a-a178-e7dbea29a1e3)


## What is Garbage in - Garbage Out Terminology
When we train a model with a garbage data it can produce only garbage output which are not fit for the purpose
This is a common terminology used in machine learning.

## What is ChatGPT
ChatGPT is a large language model developed by OpenAI.
It is designed for natural language understanding and generation, specifically in a conversational context. It can also remember the context of the conversation as it progress.

# Module 02 : Understanding Key Terminologies in LLM

## What is Large Language Model (LLM)
Large language Models (LLMs) are powerful artificial intelligence models designed for understanding and generating human like text. just like auto proposed words while typing in WhatsApp.
LLM only handles text generation in the LLM, it is not responsible for image or audio or music or code or video.
LLM uses neural networks behind the scene to process and predict word by word and produce the result. It only predicts one next word at a time and provide as output.

Below is a diagram which represents how neural networks works.
![Neural networks](https://github.com/user-attachments/assets/bf8dc85a-df09-4501-897f-f7fd00981ccf)

## Key Points on LLM

### Pre Training on LLM
LLM are trained on huge corpus of data that is why it is used as Large Language Model to help with language, sentiment, grammar etc.
ChatGPT is trained on more than 500GB of text data which includes entire wikipedia etc.

### Size and Scale
It uses massive amount of neural networks such as transformers with billions of parameters to train the model. Higher the number of parameter better the performance of your model.
ChatGPt is trained on 500 billions of parameters.

### Fine Tuning
We can tune an existing LLM model to fine tune to further for a specific purpose, For example training a model with medical language.

## Use cases for LLM
It can be used mainly for few of the below purposes.

- Content Generation
- Chatbots and Virtual Assistants
- Language Translation
- Text Summarization
- Q & A

## What is a Prompt Engineering

Prompt is a specific question, command or input that you provide to an AI system to request a particular response, information or action.
To get better results you will need to ask questions with more relevant context, that is what Prompt engineering standards for.

For example the type of below two questions may vary its response and accuracy.

- How is the weather look like in Bangalore
  - Ans : The current weather in Bangalore is partly cloudy with temperatures around 29°C during the day and 14°C at night
- How is the weather look like in Bangalore during June Month
  - Ans : In June, Bangalore typically experiences hot and humid weather with temperatures ranging from 21°C to 30°C. It's also the beginning of the monsoon season, so you can expect high rainfall, averaging around 125 mm for the month. There are usually about 5 days of rain during this time)

## How to create a better Prompts
To get better results always make sure we write better prompts while asking question to LLM / GPT, few of the considerations could be

- Clearly convey the 'desired response'
- Provide 'context or background' information
- Balance 'Simplicity and Complexity'
- Iterative 'testing and refinement'

## Understanding Training LLM

### What is Tokenization
Tokenization is the process of splitting a sentence into smaller chunks of words so that LLM can represent them effectively in the input of output to the model.
For example if we have a word such as "I love Glasgow", as part of tokenization process this will be separated into smaller chunks  as ["I", "love", "Glasgow"].
Each token will then assign with an index number to identify them in the vocabulary of the model, here Glasgow will have a index number of 2.

### What is Vectors
This is the  process to convert the tokens into numbers which understand by machines where each word is represented by a number.
For example in the sentence "I love Glasgow", as part of tokenization process this will be separated into smaller chunks as ["I", "love", "Glasgow"] which creates 3 tokens.
Each token in reality will have a unique number which used to represent them as vectors which is referenced in the higher space of the model.

### What is a Embedding
Embeddings is the process of creating a semantic relationship between tokens or sub tokens during the training process so that model can create a relationship between various words.
This can be visualized as a cluster of words of in the three-dimensional block where group words will be represented closely to carry semantic relation between then.
For example tokens like Ice, Cream, Land, Antarctica might have very close vector numbers to represent they are semantically very close, at the same time Desert, Camel, dates may have close semantics but far from previous group.
This relationship is build during the training of models and it can have an impact on how models are being trained and its frameworks.

![Screenshot 2025-01-13 054438](https://github.com/user-attachments/assets/d0c7c0d1-c4b5-4ac3-ade0-26b40f0cd868)

### Sample Embedding During Training

For example we can say tokens: ["king", "queen", "man", "woman"]

Each token is assigned a unique index number
- "king": 1
- "queen": 2
- "man": 3
- "woman": 4

Each token is then converted into an embedding vector. These vectors are high-dimensional representations that capture the semantic meaning of the tokens.

For simplicity, we'll use a lower-dimensional space (3 dimensions) to illustrate this:
- king: [0.2, 0.4, 0.6]
- queen: [0.3, 0.4, 0.7]
- man: [0.1, 0.3, 0.5]
- woman: [0.1, 0.3, 0.6]

With this vector embedding of tokens now the model will be able to understand difference between King and Man and its relation, similarly Queen and Woman as well.
This representation is only in 3 dimension but in reality it will higher multi dimension with various pointers.

### What is Fine-Tuning

Fine-Tuning is the process of adjusting a pre-trained model to a specific tasks according to the use case. For example GPT models like OpenAI, LLaMA, Amazon Q and Gemini are general purpose models. 
In case you want to use them for some other specific purpose for your business use cases you need to additionally fine tun ethem with addition information.
For example if you want to use them for medical, you will need to fine tune the model with how diagnosis done for various different decease and scenarios.

Below are few of the Fine-Tuning techniques

- Self Supervised Learning : Here we provide a large pile of data which is needed to fine tune the model with 'domain specific knowledge'
- Supervised Learning      : This is labelled training data given to a model with custom definition on the purpose of input given. 
- Reinforcement Learning   : This is reward based learning program where you give high and low score of its accuracy and over period of time model will learn how to improve the model based on the feedback.  

## LLM Use Cases 
LLM can be used for various different scenarios within technology and non-tech use cases. 

### Software Development  
LLM can be used for generating code snippets in various different programming languages as you needed, But when we try to generate the code its important to mention in the prompt below key information 
- As what role LLm should generate the code 
- What language it should write the code 
- What is the inteded purpose of the code and any target system to fetch details 
- What you are going to do with the output 
- If any time or filter details to inlcude with the code 

Example below is sample prompt 

```
# prompt
You are Azure Site reliability Engineer trying to create a application which alert based on service health alerts . 
Please write a code to connect to Azure service health api and fetch the output and detect if it has Service health outage. 
If yes collect the outage tracking ID and description and return to the consumer program for the last 1 hour. 
Make sure the program in Enterprise standard with all required error handling and documentation it it.

# Code Snippet Generated 

import requests
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AzureServiceHealth:
    """
    AzureServiceHealth is a class to interact with Azure Service Health API.
    """
    def __init__(self, tenant_id, client_id, client_secret):
        """
        Initialize the AzureServiceHealth instance.

        :param tenant_id: Azure Tenant ID
        :param client_id: Azure Client ID
        :param client_secret: Azure Client Secret
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_access_token()

    def get_access_token(self):
        """
        Obtain the access token for Azure Service Health API.

        :return: Access token as a string
        """
        url = f'https://login.microsoftonline.com/{self.tenant_id}/oauth2/token'
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'resource': 'https://management.azure.com/'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json().get('access_token')

    def fetch_service_health_alerts(self):
        """
        Fetch the service health alerts from Azure Service Health API for the last hour.

        :return: JSON response containing service health alerts
        """
        now = datetime.utcnow()
        one_hour_ago = now - timedelta(hours=1)
        start_time = one_hour_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f'https://management.azure.com/providers/Microsoft.ResourceHealth/events?api-version=2021-04-01&$filter=properties/status eq \'Active\' and properties/eventType eq \'ServiceHealth\' and properties/occurredTime ge {start_time} and properties/occurredTime le {end_time}'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def check_for_outages(self):
        """
        Check for service health outages from the fetched alerts.

        :return: List of dictionaries containing tracking ID and description of outages
        """
        try:
            alerts = self.fetch_service_health_alerts()
            outages = []
            for event in alerts.get('value', []):
                tracking_id = event.get('properties', {}).get('incidentId')
                description = event.get('properties', {}).get('title')
                outages.append({'tracking_id': tracking_id, 'description': description})
            return outages
        except requests.exceptions.RequestException as e:
            logging.error(f'Error fetching service health alerts: {e}')
            return []

if __name__ == "__main__":
    # Replace these with your actual Azure credentials
    tenant_id = 'your_tenant_id'
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'

    azure_service_health = AzureServiceHealth(tenant_id, client_id, client_secret)
    outages = azure_service_health.check_for_outages()

    if outages:
        for outage in outages:
            logging.info(f"Outage detected! Tracking ID: {outage['tracking_id']}, Description: {outage['description']}")
    else:
        logging.info('No service health outages detected in the last hour.')

```

- Software Testing      : 










# Things pending to Learn.

- Transformers





