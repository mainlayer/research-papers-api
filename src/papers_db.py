"""
In-memory academic paper database with 20 realistic records.

Each record contains: id, title, authors, abstract, full_text, and metadata.
"""

from typing import Dict, List, Optional
from src.models import Author, PaperDetail, PaperSummary

# ---------------------------------------------------------------------------
# Raw data store
# ---------------------------------------------------------------------------

_PAPERS_RAW: List[dict] = [
    {
        "id": "paper-001",
        "title": "Attention Is All You Need",
        "authors": [
            {"name": "Ashish Vaswani", "affiliation": "Google Brain"},
            {"name": "Noam Shazeer", "affiliation": "Google Brain"},
            {"name": "Niki Parmar", "affiliation": "Google Research"},
            {"name": "Jakob Uszkoreit", "affiliation": "Google Research"},
        ],
        "abstract": (
            "The dominant sequence transduction models are based on complex recurrent or "
            "convolutional neural networks that include an encoder and a decoder. The best "
            "performing models also connect the encoder and decoder through an attention mechanism. "
            "We propose a new simple network architecture, the Transformer, based solely on "
            "attention mechanisms, dispensing with recurrence and convolutions entirely."
        ),
        "year": 2017,
        "category": "machine-learning",
        "doi": "10.48550/arXiv.1706.03762",
        "keywords": ["transformers", "attention", "NLP", "sequence modeling"],
        "citations": 98412,
        "journal": "NeurIPS 2017",
        "full_text": (
            "# Attention Is All You Need\n\n"
            "## 1. Introduction\n\n"
            "Recurrent neural networks, long short-term memory and gated recurrent neural networks "
            "in particular, have been firmly established as state of the art approaches in sequence "
            "modeling and transduction problems such as language modeling and machine translation. "
            "Numerous efforts have since continued to push the boundaries of recurrent language "
            "models and encoder-decoder architectures.\n\n"
            "Recurrent models typically factor computation along the symbol positions of the input "
            "and output sequences. Aligning the positions to steps in computation time, they generate "
            "a sequence of hidden states h_t, as a function of the previous hidden state h_{t-1} and "
            "the input for position t. This inherently sequential nature precludes parallelization "
            "within training examples, which becomes critical at longer sequence lengths, as memory "
            "constraints limit batching across examples.\n\n"
            "## 2. Model Architecture\n\n"
            "Most competitive neural sequence transduction models have an encoder-decoder structure. "
            "Here, the encoder maps an input sequence of symbol representations to a sequence of "
            "continuous representations. Given z, the decoder then generates an output sequence of "
            "symbols one element at a time.\n\n"
            "The Transformer follows this overall architecture using stacked self-attention and "
            "point-wise, fully connected layers for both the encoder and decoder, shown in the left "
            "and right halves of Figure 1, respectively.\n\n"
            "## 3. Attention\n\n"
            "An attention function can be described as mapping a query and a set of key-value pairs "
            "to an output, where the query, keys, values, and output are all vectors. The output is "
            "computed as a weighted sum of the values, where the weight assigned to each value is "
            "computed by a compatibility function of the query with the corresponding key.\n\n"
            "We call our particular attention 'Scaled Dot-Product Attention'. The input consists of "
            "queries and keys of dimension d_k, and values of dimension d_v. We compute the dot "
            "products of the query with all keys, divide each by sqrt(d_k), and apply a softmax "
            "function to obtain the weights on the values.\n\n"
            "## 4. Experiments\n\n"
            "We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 "
            "million sentence pairs. Sentences were encoded using byte-pair encoding, which has a "
            "shared source-target vocabulary of about 37000 tokens. For English-French, we used the "
            "significantly larger WMT 2014 English-French dataset consisting of 36M sentences.\n\n"
            "On the WMT 2014 English-to-German translation task, the big transformer model outperforms "
            "the best previously reported models including ensembles by more than 2.0 BLEU, establishing "
            "a new state-of-the-art BLEU score of 28.4.\n\n"
            "## 5. Conclusion\n\n"
            "In this work, we presented the Transformer, the first sequence transduction model based "
            "entirely on attention, replacing the recurrent layers most commonly used in "
            "encoder-decoder architectures with multi-headed self-attention. The Transformer can be "
            "trained significantly faster than architectures based on recurrent or convolutional layers."
        ),
    },
    {
        "id": "paper-002",
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "authors": [
            {"name": "Jacob Devlin", "affiliation": "Google AI Language"},
            {"name": "Ming-Wei Chang", "affiliation": "Google AI Language"},
            {"name": "Kenton Lee", "affiliation": "Google AI Language"},
            {"name": "Kristina Toutanova", "affiliation": "Google AI Language"},
        ],
        "abstract": (
            "We introduce a new language representation model called BERT, which stands for "
            "Bidirectional Encoder Representations from Transformers. Unlike recent language "
            "representation models, BERT is designed to pre-train deep bidirectional representations "
            "from unlabeled text by jointly conditioning on both left and right context in all layers."
        ),
        "year": 2018,
        "category": "natural-language-processing",
        "doi": "10.48550/arXiv.1810.04805",
        "keywords": ["BERT", "transformers", "pre-training", "NLP"],
        "citations": 67213,
        "journal": "NAACL 2019",
        "full_text": (
            "# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding\n\n"
            "## 1. Introduction\n\n"
            "Language model pre-training has been shown to be effective for improving many natural "
            "language processing tasks. These include sentence-level tasks such as natural language "
            "inference and paraphrasing, which aim to predict the relationships between sentences by "
            "analyzing them holistically, as well as token-level tasks such as named entity recognition "
            "and question answering, where models are required to produce fine-grained output at the "
            "token level.\n\n"
            "## 2. BERT\n\n"
            "BERT's model architecture is a multi-layer bidirectional Transformer encoder based on "
            "the original implementation described in Vaswani et al. (2017) and released in the "
            "tensor2tensor library. We denote the number of layers (i.e., Transformer blocks) as L, "
            "the hidden size as H, and the number of self-attention heads as A.\n\n"
            "BERT_BASE: L=12, H=768, A=12, Total Parameters=110M\n"
            "BERT_LARGE: L=24, H=1024, A=16, Total Parameters=340M\n\n"
            "## 3. Pre-training BERT\n\n"
            "Unlike Peters et al. (2018a) and Radford et al. (2018), we do not use traditional "
            "left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train "
            "BERT using two unsupervised tasks: Masked Language Model (MLM) and Next Sentence "
            "Prediction (NSP).\n\n"
            "## 4. Fine-tuning BERT\n\n"
            "Fine-tuning is straightforward since the self-attention mechanism in the Transformer "
            "allows BERT to model many downstream tasks — whether they involve single text or text "
            "pairs — by swapping out the appropriate inputs and outputs.\n\n"
            "## 5. Experiments\n\n"
            "We evaluate our approach on eleven NLP tasks. Our best system improves upon the "
            "previous state of the art on GLUE by 7.7%, MultiNLI by 4.6%, SQuAD v1.1 exact match "
            "by 1.5%, and SQuAD v2.0 F1 by 5.1%."
        ),
    },
    {
        "id": "paper-003",
        "title": "Deep Residual Learning for Image Recognition",
        "authors": [
            {"name": "Kaiming He", "affiliation": "Microsoft Research"},
            {"name": "Xiangyu Zhang", "affiliation": "Microsoft Research"},
            {"name": "Shaoqing Ren", "affiliation": "Microsoft Research"},
            {"name": "Jian Sun", "affiliation": "Microsoft Research"},
        ],
        "abstract": (
            "Deeper neural networks are more difficult to train. We present a residual learning "
            "framework to ease the training of networks that are substantially deeper than those "
            "used previously. We explicitly reformulate the layers as learning residual functions "
            "with reference to the layer inputs, instead of learning unreferenced functions."
        ),
        "year": 2016,
        "category": "computer-vision",
        "doi": "10.1109/CVPR.2016.90",
        "keywords": ["ResNet", "deep learning", "image recognition", "residual connections"],
        "citations": 142890,
        "journal": "CVPR 2016",
        "full_text": (
            "# Deep Residual Learning for Image Recognition\n\n"
            "## 1. Introduction\n\n"
            "Deep convolutional neural networks have led to a series of breakthroughs for image "
            "classification. Deep networks naturally integrate low/mid/high-level features and "
            "classifiers in an end-to-end multilayer fashion, and the 'levels' of features can be "
            "enriched by the number of stacked layers (depth).\n\n"
            "## 2. Deep Residual Learning\n\n"
            "Instead of hoping each few stacked layers directly fit a desired underlying mapping, "
            "we explicitly let these layers fit a residual mapping. Formally, denoting the desired "
            "underlying mapping as H(x), we let the stacked nonlinear layers fit another mapping "
            "of F(x) := H(x) - x. The original mapping is recast into F(x) + x.\n\n"
            "## 3. Network Architectures\n\n"
            "For fair comparison, we follow the philosophy of VGG nets. The plain/residual nets "
            "have 2 fewer filter maps than the VGG nets, having 11.3 and 41.6 billion FLOPs, "
            "respectively, which is 18% and 34% of VGG-16 (196.7 billion FLOPs).\n\n"
            "## 4. Experiments\n\n"
            "We evaluate residual nets on the ImageNet 2012 classification dataset that consists "
            "of 1000 classes. The models are trained on the 1.28 million training images, and "
            "evaluated on the 50k validation images. Our ensemble achieves 3.57% error on the "
            "ImageNet test set and won 1st place in ILSVRC 2015."
        ),
    },
    {
        "id": "paper-004",
        "title": "Generative Adversarial Networks",
        "authors": [
            {"name": "Ian J. Goodfellow", "affiliation": "Université de Montréal"},
            {"name": "Jean Pouget-Abadie", "affiliation": "Université de Montréal"},
            {"name": "Mehdi Mirza", "affiliation": "Université de Montréal"},
            {"name": "Bing Xu", "affiliation": "Université de Montréal"},
            {"name": "Yoshua Bengio", "affiliation": "Université de Montréal"},
        ],
        "abstract": (
            "We propose a new framework for estimating generative models via an adversarial process, "
            "in which we simultaneously train two models: a generative model G that captures the "
            "data distribution, and a discriminative model D that estimates the probability that a "
            "sample came from the training data rather than G."
        ),
        "year": 2014,
        "category": "machine-learning",
        "doi": "10.48550/arXiv.1406.2661",
        "keywords": ["GAN", "generative models", "adversarial training", "deep learning"],
        "citations": 55672,
        "journal": "NeurIPS 2014",
        "full_text": (
            "# Generative Adversarial Networks\n\n"
            "## 1. Introduction\n\n"
            "The promise of deep learning is to discover rich, hierarchical models that represent "
            "probability distributions over the kinds of data encountered in artificial intelligence "
            "applications, such as natural images, audio waveforms and symbols in natural language "
            "corpora.\n\n"
            "## 2. Adversarial Nets\n\n"
            "The adversarial modeling framework is most straightforward to apply when the models "
            "are both multilayer perceptrons. To learn the generator's distribution p_g over data x, "
            "we define a prior on input noise variables p_z(z), then represent a mapping to data "
            "space as G(z; θ_g). G is a differentiable function represented by a multilayer "
            "perceptron with parameters θ_g.\n\n"
            "## 3. Theoretical Results\n\n"
            "Proposition 1. The global minimum of the virtual training criterion C(G) is achieved "
            "if and only if p_g = p_data. At that point, C(G) achieves the value − log 4.\n\n"
            "## 4. Experiments\n\n"
            "We trained adversarial nets on MNIST, the Toronto Face Database (TFD), and CIFAR-10. "
            "The generator nets used a mixture of rectifier linear activations and sigmoid "
            "activations, while the discriminator net used maxout activations."
        ),
    },
    {
        "id": "paper-005",
        "title": "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
        "authors": [
            {"name": "Nitish Srivastava", "affiliation": "University of Toronto"},
            {"name": "Geoffrey Hinton", "affiliation": "University of Toronto"},
            {"name": "Alex Krizhevsky", "affiliation": "University of Toronto"},
            {"name": "Ilya Sutskever", "affiliation": "University of Toronto"},
        ],
        "abstract": (
            "Deep neural nets with a large number of parameters are very powerful machine learning "
            "systems. However, overfitting is a serious problem in such networks. Large networks are "
            "also slow to use, making it difficult to deal with overfitting by combining the "
            "predictions of many different large neural nets at test time. Dropout is a technique "
            "for addressing this problem."
        ),
        "year": 2014,
        "category": "machine-learning",
        "doi": "10.5555/2627435.2670313",
        "keywords": ["dropout", "regularization", "overfitting", "neural networks"],
        "citations": 38941,
        "journal": "JMLR 2014",
        "full_text": (
            "# Dropout: A Simple Way to Prevent Neural Networks from Overfitting\n\n"
            "## 1. Introduction\n\n"
            "A motivation for dropout comes from a theory of the role of sex in evolution. One "
            "possible explanation for the role of sex is that it acts as a strong regularizer. "
            "Combining the genetic material of two parents to produce an offspring is similar to "
            "performing dropout and combining the surviving units.\n\n"
            "## 2. The Model\n\n"
            "Consider a neural network with L hidden layers. Let z^l denote the vector of inputs "
            "into layer l, y^l denote the vector of outputs from layer l (y^0 = x is the input). "
            "W^l and b^l are the weights and biases at layer l. Dropout can be described as a "
            "thinned version of the neural network where each unit is retained with probability p.\n\n"
            "## 3. Learning Dropout Nets\n\n"
            "The objective function with dropout is to maximize the expected log-likelihood of the "
            "training labels given the training data, where the expectation is taken over the "
            "dropout masks. This is equivalent to performing Monte-Carlo sampling.\n\n"
            "## 4. Results\n\n"
            "Using dropout on fully-connected layers improved results on all benchmark datasets "
            "tested: MNIST, CIFAR-10, CIFAR-100, SVHN, ImageNet, Reuters-RCV1, and TIMIT."
        ),
    },
    {
        "id": "paper-006",
        "title": "Adam: A Method for Stochastic Optimization",
        "authors": [
            {"name": "Diederik P. Kingma", "affiliation": "University of Amsterdam"},
            {"name": "Jimmy Ba", "affiliation": "University of Toronto"},
        ],
        "abstract": (
            "We introduce Adam, an algorithm for first-order gradient-based optimization of "
            "stochastic objective functions, based on adaptive estimates of lower-order moments. "
            "The method is straightforward to implement, is computationally efficient, has little "
            "memory requirements, is invariant to diagonal rescaling of gradients."
        ),
        "year": 2014,
        "category": "optimization",
        "doi": "10.48550/arXiv.1412.6980",
        "keywords": ["Adam", "optimization", "gradient descent", "adaptive learning rates"],
        "citations": 121344,
        "journal": "ICLR 2015",
        "full_text": (
            "# Adam: A Method for Stochastic Optimization\n\n"
            "## 1. Introduction\n\n"
            "Stochastic gradient-based optimization is of core practical importance in many fields "
            "of science and engineering. Many problems in these fields can be cast as the "
            "optimization of some scalar parameterized objective function requiring maximization or "
            "minimization with respect to its parameters.\n\n"
            "## 2. Algorithm\n\n"
            "We propose Adam, a method for efficient stochastic optimization that only requires "
            "first-order gradients with little memory requirement. The method computes individual "
            "adaptive learning rates for different parameters from estimates of first and second "
            "moments of the gradients.\n\n"
            "Algorithm 1: Adam, proposed algorithm for stochastic optimization.\n"
            "Require: α (step size), β1, β2 ∈ [0,1) (exponential decay rates for moment estimates)\n"
            "Require: f(θ) (stochastic objective function with parameters θ)\n"
            "Require: θ0 (initial parameter vector)\n"
            "m0 ← 0; v0 ← 0; t ← 0\n\n"
            "## 3. Convergence Analysis\n\n"
            "We analyze the convergence of Adam using the online learning framework. We show that "
            "Adam satisfies the regret bound O(sqrt(T)) for general convex online learning problems "
            "under the assumption that the gradient is bounded and the learning rate follows the "
            "schedule α_t = α/sqrt(t).\n\n"
            "## 4. Experiments\n\n"
            "We demonstrate Adam's advantages on logistic regression, multilayer fully-connected "
            "neural networks, and deep convolutional neural networks for image recognition tasks."
        ),
    },
    {
        "id": "paper-007",
        "title": "Playing Atari with Deep Reinforcement Learning",
        "authors": [
            {"name": "Volodymyr Mnih", "affiliation": "DeepMind Technologies"},
            {"name": "Koray Kavukcuoglu", "affiliation": "DeepMind Technologies"},
            {"name": "David Silver", "affiliation": "DeepMind Technologies"},
            {"name": "Alex Graves", "affiliation": "DeepMind Technologies"},
        ],
        "abstract": (
            "We present the first deep learning model to successfully learn control policies directly "
            "from high-dimensional sensory input using reinforcement learning. The model is a "
            "convolutional neural network, trained with a variant of Q-learning, whose input is raw "
            "pixels and whose output is a value function estimating future rewards."
        ),
        "year": 2013,
        "category": "reinforcement-learning",
        "doi": "10.48550/arXiv.1312.5602",
        "keywords": ["DQN", "reinforcement learning", "Atari", "deep learning"],
        "citations": 18923,
        "journal": "NIPS 2013 Workshop",
        "full_text": (
            "# Playing Atari with Deep Reinforcement Learning\n\n"
            "## 1. Introduction\n\n"
            "Learning to control agents directly from high-dimensional sensory inputs like vision "
            "and speech is one of the long-standing challenges of reinforcement learning. Most "
            "successful RL applications that have operated on these domains have relied on "
            "hand-crafted features combined with linear value functions or policy representations.\n\n"
            "## 2. Background\n\n"
            "We consider tasks in which an agent interacts with an environment E (the Atari emulator) "
            "in a sequence of actions, observations and rewards. At each time-step the agent selects "
            "an action a_t from the set of legal game actions A = {1,...,K}. The action is passed to "
            "the emulator and modifies its internal state and the game score.\n\n"
            "## 3. Deep Q-Network\n\n"
            "We use a deep convolutional neural network to approximate the optimal action-value "
            "function Q*(s,a) = max_π E[r_t + γr_{t+1} + γ²r_{t+2} + ... | s_t = s, a_t = a, π]. "
            "This is trained using experience replay and a separate target network to stabilize "
            "learning.\n\n"
            "## 4. Results\n\n"
            "The DQN agent outperformed a professional human games tester across all 49 Atari games "
            "evaluated, achieving at least 75% of human-level performance on 43 of the 49 games."
        ),
    },
    {
        "id": "paper-008",
        "title": "Mastering the Game of Go with Deep Neural Networks and Tree Search",
        "authors": [
            {"name": "David Silver", "affiliation": "DeepMind"},
            {"name": "Aja Huang", "affiliation": "DeepMind"},
            {"name": "Chris J. Maddison", "affiliation": "DeepMind"},
            {"name": "Arthur Guez", "affiliation": "DeepMind"},
            {"name": "Demis Hassabis", "affiliation": "DeepMind"},
        ],
        "abstract": (
            "The game of Go has long been viewed as the most challenging of classic games for "
            "artificial intelligence, owing to its enormous search space and the difficulty of "
            "evaluating board positions and moves. We introduce a new approach to computer Go that "
            "uses value networks and policy networks, both represented by deep neural networks."
        ),
        "year": 2016,
        "category": "reinforcement-learning",
        "doi": "10.1038/nature16961",
        "keywords": ["AlphaGo", "Go", "MCTS", "reinforcement learning"],
        "citations": 16503,
        "journal": "Nature 2016",
        "full_text": (
            "# Mastering the Game of Go with Deep Neural Networks and Tree Search\n\n"
            "## 1. Introduction\n\n"
            "Games have provided a useful testbed for developing and evaluating game-playing methods "
            "in AI research. Go is the most challenging of classic games, with a search space of "
            "10^170 positions — far larger than chess. The best human players have intuitions built "
            "over years of study that no program has previously been able to replicate.\n\n"
            "## 2. Policy and Value Networks\n\n"
            "We trained a 13-layer policy network by supervised learning from 30 million positions "
            "from the KGS Go Server. It predicted expert moves with 57% accuracy (vs 44% for the "
            "previous state of the art). We then trained the network further by self-play using "
            "policy gradient reinforcement learning.\n\n"
            "## 3. Monte Carlo Tree Search with Neural Networks\n\n"
            "AlphaGo combines the policy and value networks with Monte Carlo tree search (MCTS). "
            "Each edge (s,a) in the search tree stores a prior probability P(s,a), visit count "
            "N(s,a), and action value Q(s,a). The algorithm iterates over select, expand, evaluate, "
            "and backup steps.\n\n"
            "## 4. Results\n\n"
            "AlphaGo defeated the European Go champion Fan Hui 5-0 in October 2015 — the first "
            "time a computer program had defeated a professional human Go player without handicap. "
            "It subsequently defeated Lee Sedol 4-1 in March 2016."
        ),
    },
    {
        "id": "paper-009",
        "title": "Language Models are Few-Shot Learners",
        "authors": [
            {"name": "Tom B. Brown", "affiliation": "OpenAI"},
            {"name": "Benjamin Mann", "affiliation": "OpenAI"},
            {"name": "Nick Ryder", "affiliation": "OpenAI"},
            {"name": "Melanie Subbiah", "affiliation": "OpenAI"},
            {"name": "Ilya Sutskever", "affiliation": "OpenAI"},
        ],
        "abstract": (
            "We demonstrate that scaling language models greatly improves task-agnostic, few-shot "
            "performance, sometimes even reaching competitiveness with prior state-of-the-art "
            "fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model "
            "with 175 billion parameters, and test its performance in the few-shot setting."
        ),
        "year": 2020,
        "category": "natural-language-processing",
        "doi": "10.48550/arXiv.2005.14165",
        "keywords": ["GPT-3", "few-shot learning", "language models", "in-context learning"],
        "citations": 29817,
        "journal": "NeurIPS 2020",
        "full_text": (
            "# Language Models are Few-Shot Learners\n\n"
            "## 1. Introduction\n\n"
            "Recent years have featured a trend towards pre-trained language representations in NLP "
            "systems, applied in increasingly flexible and task-agnostic ways for downstream transfer. "
            "First, single-layer representations were learned using word vectors, then RNNs with "
            "multiple layers, and recently transformers trained on next-word prediction.\n\n"
            "## 2. Approach\n\n"
            "Our basic pre-training approach, including model, data, and training, is similar to the "
            "process described in GPT-2, with relatively straightforward scaling up of the model "
            "size, dataset size and diversity, and length of training. GPT-3 is trained on a mixture "
            "of Common Crawl, WebText2, Books1, Books2, and Wikipedia.\n\n"
            "## 3. Few-Shot Learning\n\n"
            "We evaluate GPT-3 in zero-shot, one-shot, and few-shot settings. In the few-shot "
            "setting we allow the model to see K examples of the task at test time as a prompt. "
            "K is typically in the range 10-100. GPT-3 achieves strong performance in this setting "
            "across many tasks.\n\n"
            "## 4. Results\n\n"
            "GPT-3 achieves 88.6% one-shot accuracy on TriviaQA, surpassing the state-of-the-art "
            "fine-tuned model. It achieves 71.8% on WebQs in few-shot setting, approaching "
            "fine-tuned models. On SuperGLUE it achieves 71.8 in few-shot setting."
        ),
    },
    {
        "id": "paper-010",
        "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
        "authors": [
            {"name": "Alexey Dosovitskiy", "affiliation": "Google Research"},
            {"name": "Lucas Beyer", "affiliation": "Google Research"},
            {"name": "Alexander Kolesnikov", "affiliation": "Google Research"},
            {"name": "Dirk Weissenborn", "affiliation": "Google Research"},
        ],
        "abstract": (
            "While the Transformer architecture has become the de-facto standard for natural language "
            "processing tasks, its applications to computer vision remain limited. We show that this "
            "reliance on CNNs is not necessary and a pure transformer applied directly to sequences "
            "of image patches can perform very well on image classification tasks."
        ),
        "year": 2020,
        "category": "computer-vision",
        "doi": "10.48550/arXiv.2010.11929",
        "keywords": ["ViT", "vision transformer", "image classification", "patches"],
        "citations": 27104,
        "journal": "ICLR 2021",
        "full_text": (
            "# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale\n\n"
            "## 1. Introduction\n\n"
            "Inspired by the Transformer scaling successes in NLP, we experiment with applying a "
            "standard Transformer directly to images, with as few modifications as possible. To do "
            "so, we split an image into patches and provide the sequence of linear embeddings of "
            "these patches as an input to a Transformer.\n\n"
            "## 2. Method\n\n"
            "In model design we follow the original Transformer as closely as possible. The image "
            "x ∈ R^{H×W×C} is reshaped into a sequence of flattened 2D patches x_p ∈ R^{N×(P²·C)}, "
            "where (H, W) is the resolution of the original image, C is the number of channels, "
            "(P, P) is the resolution of each image patch, and N = HW/P² is the resulting number "
            "of patches.\n\n"
            "## 3. Experiments\n\n"
            "We train ViT on JFT-300M, ImageNet-21k, and ImageNet at various scales. ViT-H/14 and "
            "ViT-L/16 outperform BiT-L (which is trained on JFT-300M) on most classification "
            "benchmarks, while taking substantially less computational resources to pre-train.\n\n"
            "## 4. Results\n\n"
            "ViT-H/14 achieves 88.55% top-1 accuracy on ImageNet, outperforming all previous models "
            "while requiring 2.5x fewer pre-training compute than the best existing models."
        ),
    },
    {
        "id": "paper-011",
        "title": "Denoising Diffusion Probabilistic Models",
        "authors": [
            {"name": "Jonathan Ho", "affiliation": "UC Berkeley"},
            {"name": "Ajay Jain", "affiliation": "UC Berkeley"},
            {"name": "Pieter Abbeel", "affiliation": "UC Berkeley"},
        ],
        "abstract": (
            "We present high quality image synthesis results using diffusion probabilistic models, "
            "a class of latent variable models inspired by considerations from nonequilibrium "
            "thermodynamics. Our best results are obtained by training on a weighted variational "
            "bound designed according to a novel connection between diffusion probabilistic models "
            "and denoising score matching with Langevin dynamics."
        ),
        "year": 2020,
        "category": "generative-models",
        "doi": "10.48550/arXiv.2006.11239",
        "keywords": ["diffusion models", "DDPM", "image synthesis", "generative models"],
        "citations": 14502,
        "journal": "NeurIPS 2020",
        "full_text": (
            "# Denoising Diffusion Probabilistic Models\n\n"
            "## 1. Introduction\n\n"
            "A diffusion probabilistic model is a parameterized Markov chain trained using variational "
            "inference to produce samples matching the data after finite time. Transitions of this "
            "chain are learned to reverse a diffusion process, which is a Markov chain that gradually "
            "adds noise to the data in the opposite direction of sampling until signal is destroyed.\n\n"
            "## 2. Background\n\n"
            "A diffusion model defines a forward process q(x_t|x_{t-1}) that adds Gaussian noise at "
            "each step. The reverse process p_θ(x_{t-1}|x_t) is parameterized as Gaussian. Training "
            "minimizes the variational lower bound on the negative log likelihood.\n\n"
            "## 3. Diffusion Models and Denoising Score Matching\n\n"
            "Our simplified training objective is L_simple = E_{t,x_0,ε}[||ε - ε_θ(√ᾱ_t x_0 + "
            "√(1-ᾱ_t)ε, t)||²]. This trains a network ε_θ to predict the noise ε added to x_0.\n\n"
            "## 4. Experiments\n\n"
            "Our DDPM model achieves FID of 3.17 on CIFAR-10, outperforming the previous state of "
            "the art. On CelebA-HQ 256x256, we achieve FID of 7.90 which is competitive with "
            "state-of-the-art models including GANs."
        ),
    },
    {
        "id": "paper-012",
        "title": "Training Language Models to Follow Instructions with Human Feedback",
        "authors": [
            {"name": "Long Ouyang", "affiliation": "OpenAI"},
            {"name": "Jeff Wu", "affiliation": "OpenAI"},
            {"name": "Xu Jiang", "affiliation": "OpenAI"},
            {"name": "Diogo Almeida", "affiliation": "OpenAI"},
        ],
        "abstract": (
            "Making language models bigger does not inherently make them better at following a user's "
            "intent. Large language models can generate outputs that are untruthful, toxic, or simply "
            "not helpful to the user. We show an avenue for aligning language models with user intent "
            "using reinforcement learning from human feedback (RLHF)."
        ),
        "year": 2022,
        "category": "natural-language-processing",
        "doi": "10.48550/arXiv.2203.02155",
        "keywords": ["RLHF", "InstructGPT", "alignment", "human feedback"],
        "citations": 8941,
        "journal": "NeurIPS 2022",
        "full_text": (
            "# Training Language Models to Follow Instructions with Human Feedback\n\n"
            "## 1. Introduction\n\n"
            "Increasing model size doesn't guarantee that the model is better aligned with the user's "
            "intentions. Large language models can fail to follow simple instructions, make up facts, "
            "produce harmful content, or be sycophantic.\n\n"
            "## 2. Methods\n\n"
            "We use RLHF to fine-tune GPT-3 using the following steps: (1) Collect demonstration "
            "data and train a supervised learning policy. (2) Collect comparison data and train a "
            "reward model. (3) Optimize a policy against the reward model using PPO.\n\n"
            "## 3. Human Evaluation\n\n"
            "Our 1.3B parameter InstructGPT model is preferred over the 175B GPT-3 by 85% of "
            "human labelers in terms of being helpful, honest, and harmless. This shows model "
            "size alone is not sufficient for alignment.\n\n"
            "## 4. Discussion\n\n"
            "This work demonstrates that RLHF can meaningfully align large language models with "
            "human preferences. The alignment tax — performance decrease on NLP benchmarks — is "
            "small (less than 5% on most benchmarks)."
        ),
    },
    {
        "id": "paper-013",
        "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
        "authors": [
            {"name": "Patrick Lewis", "affiliation": "Facebook AI Research"},
            {"name": "Ethan Perez", "affiliation": "Facebook AI Research"},
            {"name": "Aleksandra Piktus", "affiliation": "Facebook AI Research"},
            {"name": "Fabio Petroni", "affiliation": "Facebook AI Research"},
        ],
        "abstract": (
            "Large pre-trained language models have been shown to store factual knowledge in their "
            "parameters, and achieve state-of-the-art results on knowledge-intensive NLP tasks. "
            "However, their ability to access and precisely manipulate knowledge is still limited. "
            "We propose RAG, combining parametric and non-parametric memory for language generation."
        ),
        "year": 2020,
        "category": "natural-language-processing",
        "doi": "10.48550/arXiv.2005.11401",
        "keywords": ["RAG", "retrieval augmentation", "open-domain QA", "knowledge-intensive NLP"],
        "citations": 6821,
        "journal": "NeurIPS 2020",
        "full_text": (
            "# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks\n\n"
            "## 1. Introduction\n\n"
            "We explore a general-purpose fine-tuning recipe for retrieval-augmented generation "
            "(RAG) — models which combine pre-trained parametric and non-parametric memory for "
            "language generation. We use a dense vector index of Wikipedia and a pre-trained "
            "neural retriever to retrieve documents.\n\n"
            "## 2. Methods\n\n"
            "RAG models take an input sequence x, retrieve text documents z using a retriever "
            "p_η(z|x), and then use them as additional context when generating the target sequence y "
            "using a generator p_θ(y_i|x, z, y_{1:i-1}). Both the retriever and generator are "
            "jointly fine-tuned end-to-end.\n\n"
            "## 3. Results\n\n"
            "RAG models achieve new state-of-the-art results on a wide range of open-domain QA "
            "tasks, outperforming both parametric-only seq2seq models and task-specific retrieve-"
            "then-read approaches. On Natural Questions, RAG achieves 44.5 EM.\n\n"
            "## 4. Ablations\n\n"
            "We show that both components (retrieval and generation) are essential for RAG's "
            "performance. Removing either component significantly degrades results across all "
            "evaluated benchmarks."
        ),
    },
    {
        "id": "paper-014",
        "title": "Scaling Laws for Neural Language Models",
        "authors": [
            {"name": "Jared Kaplan", "affiliation": "Johns Hopkins University"},
            {"name": "Sam McCandlish", "affiliation": "OpenAI"},
            {"name": "Tom Henighan", "affiliation": "OpenAI"},
            {"name": "Tom B. Brown", "affiliation": "OpenAI"},
        ],
        "abstract": (
            "We study empirical scaling laws for language model performance on the cross-entropy "
            "loss. The loss scales as a power-law with model size, dataset size, and the amount "
            "of compute used for training, with some trends spanning more than seven orders of "
            "magnitude. Other architectural details such as network width or depth have minimal "
            "effects within a wide range."
        ),
        "year": 2020,
        "category": "machine-learning",
        "doi": "10.48550/arXiv.2001.08361",
        "keywords": ["scaling laws", "language models", "compute", "power-law"],
        "citations": 4922,
        "journal": "arXiv 2020",
        "full_text": (
            "# Scaling Laws for Neural Language Models\n\n"
            "## 1. Introduction\n\n"
            "Language modeling is a well-defined, easily measured, and fundamental problem. We study "
            "how performance on the cross-entropy loss depends on the number of parameters in the "
            "model, the size of the training dataset, and the compute budget available for training.\n\n"
            "## 2. Summary of Scaling Laws\n\n"
            "1. Performance depends strongly on scale (N, D, C) and weakly on model shape.\n"
            "2. Smooth power laws: performance improves as a power-law in each scale factor.\n"
            "3. Universality of overfitting: performance is determined by N/D ratio.\n"
            "4. Universality of training: curves can be extrapolated from shorter runs.\n"
            "5. Transfer improves with test performance: in-distribution improvements transfer OOD.\n\n"
            "## 3. Optimal Allocation of Compute\n\n"
            "For a fixed compute budget C, the optimal model size N* ∝ C^0.73. This means as "
            "compute is scaled up, most of it should go into making models larger rather than "
            "training them longer.\n\n"
            "## 4. Implications\n\n"
            "These results suggest that larger models are more sample-efficient and that we should "
            "train much larger models on proportionally larger datasets. This has significant "
            "implications for how compute budgets should be allocated."
        ),
    },
    {
        "id": "paper-015",
        "title": "Proximal Policy Optimization Algorithms",
        "authors": [
            {"name": "John Schulman", "affiliation": "OpenAI"},
            {"name": "Filip Wolski", "affiliation": "OpenAI"},
            {"name": "Prafulla Dhariwal", "affiliation": "OpenAI"},
            {"name": "Alec Radford", "affiliation": "OpenAI"},
            {"name": "Oleg Klimov", "affiliation": "OpenAI"},
        ],
        "abstract": (
            "We propose a new family of policy gradient methods for reinforcement learning, which "
            "alternate between sampling data through interaction with the environment, and optimizing "
            "a 'surrogate' objective function using stochastic gradient ascent. Whereas standard "
            "policy gradient methods perform one gradient update per data sample, we propose a novel "
            "objective function that enables multiple epochs of minibatch updates."
        ),
        "year": 2017,
        "category": "reinforcement-learning",
        "doi": "10.48550/arXiv.1707.06347",
        "keywords": ["PPO", "policy gradient", "reinforcement learning", "TRPO"],
        "citations": 13211,
        "journal": "arXiv 2017",
        "full_text": (
            "# Proximal Policy Optimization Algorithms\n\n"
            "## 1. Introduction\n\n"
            "Recent years have seen a great deal of interest in using deep neural networks as "
            "function approximators for reinforcement learning. Policy gradient methods have "
            "generally favored newer methods such as trust region policy optimization (TRPO), "
            "which is relatively complicated and not compatible with architectures that include "
            "noise or parameter sharing.\n\n"
            "## 2. Background: Policy Gradient Methods\n\n"
            "Policy gradient methods work by computing an estimator of the policy gradient and "
            "plugging it into a stochastic gradient ascent algorithm. The most commonly used "
            "gradient estimator has the form: ĝ = Ê_t[∇_θ log π_θ(a_t|s_t) Â_t].\n\n"
            "## 3. Clipped Surrogate Objective\n\n"
            "The PPO clipped objective is: L^CLIP(θ) = Ê_t[min(r_t(θ)Â_t, clip(r_t(θ), "
            "1-ε, 1+ε)Â_t)]. Here r_t(θ) = π_θ(a_t|s_t) / π_{θ_old}(a_t|s_t), and ε is "
            "a hyperparameter, typically 0.1 or 0.2.\n\n"
            "## 4. Experiments\n\n"
            "PPO outperforms TRPO on most tasks while being simpler to implement. On the Mujoco "
            "continuous control benchmarks, PPO achieves state-of-the-art results. On Atari "
            "games, PPO matches or exceeds the performance of A3C."
        ),
    },
    {
        "id": "paper-016",
        "title": "ImageNet Large Scale Visual Recognition Challenge",
        "authors": [
            {"name": "Olga Russakovsky", "affiliation": "Stanford University"},
            {"name": "Jia Deng", "affiliation": "Stanford University"},
            {"name": "Hao Su", "affiliation": "Stanford University"},
            {"name": "Jonathan Krause", "affiliation": "Stanford University"},
            {"name": "Li Fei-Fei", "affiliation": "Stanford University"},
        ],
        "abstract": (
            "The ImageNet Large Scale Visual Recognition Challenge (ILSVRC) is a benchmark in "
            "object category classification and detection on hundreds of thousands of images and "
            "hundreds of object categories. We discuss the creation of this benchmark dataset, "
            "report on the advances in object recognition obtained by challenge participants, "
            "and present the current state of the art."
        ),
        "year": 2015,
        "category": "computer-vision",
        "doi": "10.1007/s11263-015-0816-y",
        "keywords": ["ImageNet", "ILSVRC", "object recognition", "benchmark"],
        "citations": 51234,
        "journal": "International Journal of Computer Vision 2015",
        "full_text": (
            "# ImageNet Large Scale Visual Recognition Challenge\n\n"
            "## 1. Introduction\n\n"
            "The ImageNet dataset is a hand-annotated database of images from the web, organized "
            "according to the WordNet hierarchy. We created ILSVRC using a subset of ImageNet with "
            "1000 object categories and 1.2 million training images, 50k validation images, and "
            "150k test images.\n\n"
            "## 2. The Dataset\n\n"
            "The dataset contains 1,000 object categories, 1.2 million training images, 50,000 "
            "validation images, and 100,000 test images. Images were collected from the web and "
            "labeled by Amazon Mechanical Turk workers, with multiple levels of quality control.\n\n"
            "## 3. The Challenge\n\n"
            "ILSVRC runs annually from 2010 to 2017. Participants are evaluated on image "
            "classification (top-5 error), single-object localization, and object detection. "
            "The challenge has driven major advances in computer vision.\n\n"
            "## 4. Major Results\n\n"
            "From 2010 to 2015, top-5 error fell from 28.2% to 3.57%, largely driven by deep "
            "convolutional neural networks starting in 2012 with AlexNet (16.4%). GoogLeNet "
            "(6.67%), VGGNet (7.3%), and ResNet (3.57%) continued this trend."
        ),
    },
    {
        "id": "paper-017",
        "title": "DALL-E 2: Hierarchical Text-Conditional Image Generation with CLIP Latents",
        "authors": [
            {"name": "Aditya Ramesh", "affiliation": "OpenAI"},
            {"name": "Prafulla Dhariwal", "affiliation": "OpenAI"},
            {"name": "Alex Nichol", "affiliation": "OpenAI"},
            {"name": "Casey Chu", "affiliation": "OpenAI"},
            {"name": "Mark Chen", "affiliation": "OpenAI"},
        ],
        "abstract": (
            "Contrastive models like CLIP have been shown to learn robust representations of "
            "images that capture both semantics and style. To leverage these representations for "
            "image generation, we propose a two-stage model: a prior that generates a CLIP image "
            "embedding given a text caption, and a decoder that generates an image conditioned "
            "on the image embedding."
        ),
        "year": 2022,
        "category": "generative-models",
        "doi": "10.48550/arXiv.2204.06125",
        "keywords": ["DALL-E 2", "text-to-image", "CLIP", "diffusion"],
        "citations": 3402,
        "journal": "arXiv 2022",
        "full_text": (
            "# DALL-E 2: Hierarchical Text-Conditional Image Generation with CLIP Latents\n\n"
            "## 1. Introduction\n\n"
            "We present DALL-E 2, a system that can create realistic images and art from a "
            "description in natural language. DALL-E 2 has learned more diverse capabilities "
            "including combining concepts, attributes, and styles than previous models.\n\n"
            "## 2. Method\n\n"
            "Given a text y, we first generate a CLIP image embedding ĩ using a prior P(z_i|y). "
            "We then use a diffusion decoder P(x|z_i, y) to generate an image x conditioned on "
            "the CLIP image embedding. We experimented with autoregressive and diffusion priors.\n\n"
            "## 3. Capabilities\n\n"
            "DALL-E 2 can create photorealistic images from text descriptions, can modify images "
            "in a variety of ways using natural language, can produce realistic images of objects "
            "and concepts that don't exist, and can create images in the style of famous artists.\n\n"
            "## 4. Evaluation\n\n"
            "Human evaluators prefer DALL-E 2 outputs to DALL-E 1 in terms of both realism (71%) "
            "and caption match (67%). DALL-E 2 achieves an FID of 10.39 on MS-COCO zero-shot."
        ),
    },
    {
        "id": "paper-018",
        "title": "Neural Architecture Search with Reinforcement Learning",
        "authors": [
            {"name": "Barret Zoph", "affiliation": "Google Brain"},
            {"name": "Quoc V. Le", "affiliation": "Google Brain"},
        ],
        "abstract": (
            "Neural networks are powerful and flexible models that work well for many difficult "
            "learning tasks in image, speech and natural language understanding. Despite their "
            "success, neural networks are still hard to design. We use a recurrent network to "
            "generate the model descriptions of neural networks and train this RNN with "
            "reinforcement learning to maximize the expected accuracy of the generated "
            "architectures on a validation set."
        ),
        "year": 2016,
        "category": "machine-learning",
        "doi": "10.48550/arXiv.1611.01578",
        "keywords": ["NAS", "neural architecture search", "reinforcement learning", "AutoML"],
        "citations": 5123,
        "journal": "ICLR 2017",
        "full_text": (
            "# Neural Architecture Search with Reinforcement Learning\n\n"
            "## 1. Introduction\n\n"
            "Designing neural networks typically requires expert knowledge and extensive trial and "
            "error. We propose a method to use reinforcement learning to automatically design "
            "neural networks, making AutoML a more practical reality.\n\n"
            "## 2. Methods\n\n"
            "The controller RNN generates a neural network architecture as a sequence of tokens. "
            "The generated network is trained to convergence on the training data, and the "
            "validation accuracy is used as the reward signal to train the controller using "
            "the REINFORCE algorithm.\n\n"
            "## 3. Architecture Search Space\n\n"
            "For convolutional networks, the controller predicts: filter height, filter width, "
            "stride height, stride width, and number of filters for each layer. For recurrent "
            "networks, it predicts: the tree structure and combination methods at each node.\n\n"
            "## 4. Results\n\n"
            "The best architecture found achieves 3.65% error rate on the Penn Treebank dataset, "
            "outperforming the previous state-of-the-art. On CIFAR-10, it achieves 3.65% test "
            "error, comparable to the best human-designed architectures."
        ),
    },
    {
        "id": "paper-019",
        "title": "Constitutional AI: Harmlessness from AI Feedback",
        "authors": [
            {"name": "Yuntao Bai", "affiliation": "Anthropic"},
            {"name": "Saurav Kadavath", "affiliation": "Anthropic"},
            {"name": "Sandipan Kundu", "affiliation": "Anthropic"},
            {"name": "Amanda Askell", "affiliation": "Anthropic"},
            {"name": "Jackson Kernion", "affiliation": "Anthropic"},
        ],
        "abstract": (
            "As AI systems become more capable, we would like to enlist their help to supervise "
            "other AIs. We experiment with methods for training a harmless AI assistant through "
            "self-improvement, without any human labels identifying harmful outputs. The only human "
            "oversight is provided through a list of rules or principles, and so we call the method "
            "Constitutional AI (CAI)."
        ),
        "year": 2022,
        "category": "ai-safety",
        "doi": "10.48550/arXiv.2212.08073",
        "keywords": ["Constitutional AI", "AI safety", "harmlessness", "RLHF", "alignment"],
        "citations": 2841,
        "journal": "arXiv 2022",
        "full_text": (
            "# Constitutional AI: Harmlessness from AI Feedback\n\n"
            "## 1. Introduction\n\n"
            "Anthropic's goal is to develop AI systems that are helpful, harmless, and honest. "
            "Constitutional AI is a technique that uses a set of principles (the 'constitution') "
            "to guide AI systems to be more harmless without relying solely on human labelers "
            "to identify harmful content.\n\n"
            "## 2. The Constitutional AI Method\n\n"
            "Stage 1 (Supervised Learning): We generate a dataset of AI-revised responses using "
            "principles from the constitution. We then fine-tune the initial model on these "
            "revised responses.\n"
            "Stage 2 (RL from AI Feedback): We generate comparison data using feedback from an "
            "AI, trained using a set of principles. We then train a preference model and fine-tune "
            "using RL.\n\n"
            "## 3. The Constitution\n\n"
            "The constitution is a set of principles used to evaluate AI outputs. It includes "
            "principles from various sources including the UN Declaration of Human Rights, Apple's "
            "Terms of Service, and principles around non-deception and non-manipulation.\n\n"
            "## 4. Results\n\n"
            "Constitutional AI models are significantly less harmful than RLHF models trained "
            "with human feedback, while maintaining similar levels of helpfulness. Human raters "
            "prefer CAI responses to RLHF responses 72% of the time on harmlessness."
        ),
    },
    {
        "id": "paper-020",
        "title": "Toolformer: Language Models Can Teach Themselves to Use Tools",
        "authors": [
            {"name": "Timo Schick", "affiliation": "Meta AI Research"},
            {"name": "Jane Dwivedi-Yu", "affiliation": "Meta AI Research"},
            {"name": "Roberto Dessi", "affiliation": "Meta AI Research"},
            {"name": "Roberta Raileanu", "affiliation": "Meta AI Research"},
            {"name": "Maria Lomeli", "affiliation": "Meta AI Research"},
        ],
        "abstract": (
            "Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few "
            "examples or textual instructions, especially at scale. They also, paradoxically, struggle "
            "with basic functionality, such as arithmetic or factual lookup, where much simpler and "
            "smaller models excel. In this paper, we show that LMs can teach themselves to use "
            "external tools via simple APIs and that this can be done in a self-supervised way."
        ),
        "year": 2023,
        "category": "natural-language-processing",
        "doi": "10.48550/arXiv.2302.04761",
        "keywords": ["Toolformer", "tool use", "language models", "APIs", "self-supervised"],
        "citations": 1923,
        "journal": "NeurIPS 2023",
        "full_text": (
            "# Toolformer: Language Models Can Teach Themselves to Use Tools\n\n"
            "## 1. Introduction\n\n"
            "Large language models are impressive in their ability to perform complex tasks from "
            "natural language descriptions, but they have well-known weaknesses: they cannot access "
            "real-time information, struggle with arithmetic, and can hallucinate facts. Tools can "
            "fix these weaknesses, but how to teach LMs to use them?\n\n"
            "## 2. Method\n\n"
            "Toolformer is trained using a self-supervised approach: (1) We generate candidate API "
            "calls by prompting a pre-trained LM. (2) We filter these calls by checking if they "
            "reduce perplexity on the continuation. (3) We fine-tune the model on the resulting "
            "annotated dataset.\n\n"
            "## 3. Tools\n\n"
            "Toolformer can use five tools: a calculator, a Q&A system, a Wikipedia search, a "
            "translation system, and a calendar. Each tool is accessed through a simple API that "
            "takes text input and returns text output.\n\n"
            "## 4. Results\n\n"
            "Toolformer dramatically outperforms GPT-3 on math benchmarks (SVAMP: 83.7% vs 69.8%) "
            "and factual QA tasks (WebQs: 53.0% vs 43.0%), while maintaining competitive "
            "performance on language modeling benchmarks."
        ),
    },
]

# ---------------------------------------------------------------------------
# Derived lookups
# ---------------------------------------------------------------------------

PAPERS_BY_ID: Dict[str, dict] = {p["id"]: p for p in _PAPERS_RAW}

CATEGORIES: List[dict] = [
    {
        "id": "machine-learning",
        "name": "Machine Learning",
        "description": "Core machine learning algorithms, theory, and applications.",
    },
    {
        "id": "natural-language-processing",
        "name": "Natural Language Processing",
        "description": "Language understanding, generation, and representation.",
    },
    {
        "id": "computer-vision",
        "name": "Computer Vision",
        "description": "Image recognition, object detection, and visual understanding.",
    },
    {
        "id": "reinforcement-learning",
        "name": "Reinforcement Learning",
        "description": "Learning through interaction, reward signals, and policy optimization.",
    },
    {
        "id": "generative-models",
        "name": "Generative Models",
        "description": "Models that learn to generate data: GANs, diffusion, VAEs.",
    },
    {
        "id": "optimization",
        "name": "Optimization",
        "description": "Gradient methods, convergence theory, and training algorithms.",
    },
    {
        "id": "ai-safety",
        "name": "AI Safety",
        "description": "Alignment, harmlessness, and robustness of AI systems.",
    },
]

CATEGORY_BY_ID: Dict[str, dict] = {c["id"]: c for c in CATEGORIES}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_all_papers() -> List[PaperSummary]:
    return [_to_summary(p) for p in _PAPERS_RAW]


def get_paper_detail(paper_id: str) -> Optional[PaperDetail]:
    raw = PAPERS_BY_ID.get(paper_id)
    if raw is None:
        return None
    return _to_detail(raw)


def get_paper_full_text(paper_id: str) -> Optional[dict]:
    return PAPERS_BY_ID.get(paper_id)


def search_papers(query: str) -> List[PaperSummary]:
    q = query.lower()
    results = []
    for p in _PAPERS_RAW:
        searchable = " ".join([
            p["title"],
            p["abstract"],
            " ".join(p.get("keywords", [])),
            p["category"],
            " ".join(a["name"] for a in p["authors"]),
        ]).lower()
        if q in searchable:
            results.append(_to_summary(p))
    return results


def get_category_paper_counts() -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for p in _PAPERS_RAW:
        counts[p["category"]] = counts.get(p["category"], 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _to_summary(raw: dict) -> PaperSummary:
    return PaperSummary(
        id=raw["id"],
        title=raw["title"],
        authors=[Author(**a) for a in raw["authors"]],
        abstract=raw["abstract"],
        year=raw["year"],
        category=raw["category"],
        price_usd=0.05,
        doi=raw.get("doi"),
    )


def _to_detail(raw: dict) -> PaperDetail:
    return PaperDetail(
        id=raw["id"],
        title=raw["title"],
        authors=[Author(**a) for a in raw["authors"]],
        abstract=raw["abstract"],
        year=raw["year"],
        category=raw["category"],
        price_usd=0.05,
        doi=raw.get("doi"),
        keywords=raw.get("keywords", []),
        citations=raw.get("citations", 0),
        journal=raw.get("journal"),
    )
