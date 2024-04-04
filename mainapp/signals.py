from django.db.models.signals import post_save
from .models import Employee
from .models import Job_Post
from .models import Course

import re
import nltk
from nltk.stem import PorterStemmer


def preprocess(text):

    final_string = ""
    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', ' ', text)

    # Remove unwanted punctuation
    text = re.sub(r'"', ' ', text)  
    text = re.sub(r"[£'!$%&()*,-./:;<=>?@[\]^_`{|}~]",' ',text)
    text = re.sub(r"\s+",' ',text)
    

    # Remove stop words
    text = text.split()
    useless_words = nltk.corpus.stopwords.words("english")
    
    text_filtered = [word for word in text if not word in useless_words]
    stemmer = PorterStemmer() 
    text_stemmed = [stemmer.stem(y) for y in text_filtered]
    

    final_string = ' '.join(text_stemmed)
    return final_string


def ML(text):
    return 1


def preprocess_text(sender, instance, created, **kwargs):
    if created:  # Only process on new record creation
        # Access relevant text field based on sender model
        text_field_name = {
            Employee: lambda instance: instance.education + instance.experience + instance.awards + instance.skills,
            Job_Post: lambda instance: instance.jobDescription,
            Course:   lambda instance:instance.description,
        }.get(sender)

        if text_field_name:
            text = text_field_name(instance)
            clusterable_text = preprocess(text)
            instance.clusterable_text = clusterable_text

            try:
                predicted_cluster = ML(clusterable_text)  # Replace with your ML model
                instance.cluster = predicted_cluster
            except Exception as e:
                print(f"Error during prediction for {instance.__str__} {instance.id}: {e}")

            instance.save()
        else:
            # Handle unexpected sender model (optional)
            print(f"Unexpected sender model: {sender}")


post_save.connect(preprocess_text, sender=Employee)
post_save.connect(preprocess_text, sender=Job_Post)
post_save.connect(preprocess_text, sender=Course)


