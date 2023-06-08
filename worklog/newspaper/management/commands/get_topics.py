from django.core.management.base import BaseCommand, CommandError
from contextualized_topic_models.models.ctm import CombinedTM
from contextualized_topic_models.utils.data_preparation import bert_embeddings_from_file, TopicModelDataPreparation
from contextualized_topic_models.datasets.dataset import CTMDataset
from contextualized_topic_models.evaluation.measures import CoherenceNPMI, InvertedRBO
from gensim.corpora.dictionary import Dictionary
from gensim.models import ldamodel
import os
import numpy as np
import pickle

# topics can be get from the data and stored as tags in news, and then can be used to implement search
class Command(BaseCommand):


    def handle(self, *args, **options):
        with open("newspaper/data/dbpedia_sample_abstract_20k_prep.txt", 'r') as fr_prep:
            text_training_preprocessed = [line.strip() for line in fr_prep.readlines()]
        with open("newspaper/data/dbpedia_sample_abstract_20k_unprep.txt", 'r') as fr_unprep:
            text_training_not_preprocessed = [line.strip() for line in fr_unprep.readlines()]
        training_bow_documents = text_training_preprocessed[0:15000]
        training_contextual_document = text_training_not_preprocessed[0:15000]
        testing_bow_documents = text_training_preprocessed[15000:]
        testing_contextual_documents = text_training_not_preprocessed[15000:]
        
        tp = TopicModelDataPreparation("paraphrase-distilroberta-base-v2")
        testing_dataset = tp.transform(text_for_contextual=testing_contextual_documents, text_for_bow=testing_bow_documents)

        # n_sample how many times to sample the distribution (see the doc)
        data = ctm.get_doc_topic_distribution(testing_dataset, n_samples=20) 
        print(data)
        return 0
        
        training_dataset = tp.fit(text_for_contextual=training_contextual_document, text_for_bow=training_bow_documents)

        ctm = CombinedTM(bow_size=len(tp.vocab), contextual_size=768, n_components=50) # 50 topics

        print(ctm.fit(training_dataset)) # run the model

        # ctm.get_topics()
        # training_dataset = tp.create_training_set(training_contextual_document, training_bow_documents)
        # tp.vocab[:10]
        
        # # training our model
        # ctm = CombinedTM(input_size=len(tp.vocab), bert_input_size=768, num_epochs=100, n_components=50)
        # ctm.fit(training_dataset)
        # ctm.save(models_dir="./")
        # ctm.load("contextualized_topic_model_nc_50_tpm_0.0_tpv_0.98_hs_prodLDA_ac(100, 100)_do_softplus_lr_0.2_mo_0.002_rp_0.99/", epoch=26)
        # ctm.get_topic_lists(5)
        
        # testing_dataset = tp.create_test_set(testing_contextual_documents,testing_bow_documents)
        # predictions = ctm.get_doc_topic_distribution(testing_dataset, n_samples=10)
        # print(testing_contextual_documents[15])
        # topic_index = np.argmax(predictions[15])
        # print(ctm.get_topic_lists(5)[topic_index])
        
        
        