
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












# Things pending to Learn.

- Transformers





