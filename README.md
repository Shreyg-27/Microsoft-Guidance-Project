# Microsoft_Guidance

## Aim

**Working on extending the functionality of an open-source library called Guidance.** 

It’s a library by Microsoft that allows you to query LLMs better. The goal is to add the ability to connect to different existing databases to the Guidance code so that it can augment LLMs with our own private data. 

## My Research Work 

I had to research a bit about this and these are the details I gained during my research and knowledge for this - 

1) Guidance is a Microsoft-developed open-source library that provides additional functionality to improve the querying of Language Models. It empowers developers to guide and control the output of LLMs by providing instructions and constraints, making them more effective and relevant for various language-related tasks.
2) LLMs are language models that leverage deep learning techniques to understand and generate human-like text. They have been trained on vast amounts of textual data and can perform various language-related tasks by generating text based on given prompts or inputs. LLMs have numerous applications and are widely used in natural language processing and artificial intelligence research.
3) Guidance is like a toolbox that Microsoft has created to help developers get better and more precise answers when they ask questions to Language Models. It provides tools and features that make it easier to interact with these Language Models and get the information you need.
4) Querying means asking questions or requesting information from these Language Models. When you query a Language Model, you provide it with a prompt or a question, and it generates a response based on what it has learned.

It was important for me to know these basic terms and functionalities. 

## My Approach

**Extending Guidance with Private Dataset Connectivity**

1) In this project, I have extended the functionality of the open-source library called Guidance, developed by Microsoft, to connect with my own private dataset. Guidance is a powerful tool that enhances the querying of Language Models (LLMs) and allows for more precise control over their outputs.
2) By integrating my private dataset, I enabled the Language Model to access and augment its responses with information specific to my data. When a question is asked from my dataset, the system provides the relevant answer directly from the dataset.
3) However, when the question is outside the scope of my private data, the system seamlessly falls back to the gpt2 model to generate an appropriate answer.
4) To interact with this enhanced Language Model, I have created a user-friendly website using HTML, CSS, and Flask, where users can input their queries and get accurate responses tailored to my private dataset when available, thanks to the extended Guidance library.

## Results 

### Front Page:

![image](https://github.com/Shreyg-27/Microsoft-Guidance-Project/assets/98229024/c7b603e1-9e1f-45bf-bd94-8b2972b4b656)

### Outside the dataset: 

![image](https://github.com/Shreyg-27/Microsoft-Guidance-Project/assets/98229024/97d2aa2c-1498-4dbf-8a8a-e469a25a4118)

### From the dataset: 

![image](https://github.com/Shreyg-27/Microsoft-Guidance-Project/assets/98229024/10498a35-4be5-48d0-9655-ad8c5e2d6fd1)

