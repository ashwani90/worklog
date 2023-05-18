from django.core.management.base import BaseCommand
import pandas as pd
from sentence_transformers import SentenceTransformer, InputExample
from sentence_transformers import models, losses
from torch.utils.data import DataLoader
import umap
import umap.plot
import hdbscan
import numpy as np
from sklearn.metrics import v_measure_score
import sklearn.cluster import KMeans



model_name = 'distilroberta-base'


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     /parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        data = pd.read_csv(path)
        data.head()
        reviews = data.Text.values.tolist()
        word_embedding_model = models.Transformer(model_name, max_seq_length=256)
        pooling_model = models.Pooling(
            word_embedding_model.get_word_embedding_dimension(),
            pooling_mode_mean_tokens=True
        )
        model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
        base_review_encodings = model.encode(reviews)
        # visualize embedding
        
        mapper = umap.UMAP().fit(base_review_encodings)
        p = umap.plot.points(mapper, labels=data.Cat1)
        umap.plot.show(p)
        
        umap_embs = mapper.transform(base_review_encodings)
        cluster_labels = KMeans(n_clusters=7).fit_predict(base_review_encodings)
        p = umap.plot.points(mapper, labels=cluster_labels)
        umap.plot.show(p)
        
        v_score = v_measure_score(data.Cat1, cluster_labels)
        train_data = [InputExample(texts=[text,text]) for text in reviews]
        train_dataloader = DataLoader(train_data, batch_size=20, shuffle=True)
        train_loss = losses.MultipleNegativeRankingLoss(model)
        model.fit(
            train_objectives=[(train_dataloader, train_loss)],
            epochs=2,
            show_progress_bar=True
        )
        model.save('output/simcse-model')
        
        model = SentenceTransformer('output/simcse-model')
        cse_review_encodings = model.encode(reviews)
        
        mapper = umap.UMAP().fit(cse_review_encodings)
        p = umap.plot.points(mapper, labels=data.Cat1)
        umap.plot.show()
        
        
        And a lot of work that is actually different
        
        
