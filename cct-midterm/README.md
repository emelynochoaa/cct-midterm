# CCT Midterm - Emelyn Ochoa

## Objective

This project implements the basic Cultural Consensus Theory (CCT) model using PyMC to analyze plant knowledge data, estimating consensus answers and individual competence.

## Model

The Cultural Consensus Theory (CCT) model was implemented using a Bernoulli likelihood. For informant competence (D), a Uniform prior (0.5 to 1) was chosen, reflecting knowledge better than chance. For consensus answers (Z), a non-informative Bernoulli(0.5) prior was used.

## Results

**Posterior for Informant Competence (D):**

![Informant Competence](./data/Figure1-CCT.png)

**Posterior for Consensus Answers (Z):**

![Consensus Answers](./data/Figure2-CCT.png)

## My Interpretation of Model Results

**Informant Competence (D)**

Each graph represents a respondent, and the mean displayed in the center of the graph corresponds to the informant's competence. Informant 6 (5 on the graph) has a competence score of 0.87, meaning they have strong knowledge, whereas Informant 1 (0 on the graph) has a score of 0.57. This means most of their responses are likely to have high uncertainty. The model will also trust them more, meaning respondents with high competence will have more influence on the consensus.

**Consensus Answers (Z)**

Each item represents a question about plant knowledge, which has its own consensus score. The closer the mean is to 0, the more the group generally agrees that the answer is false. The closer the mean is to 1, the more the group generally agrees that the answer is true. For items where the mean is near 0.5, there is high uncertainty about that specific question. For example, Question 5 (4 on the graph) has a mean of 0.57, which is also visible in the bars, as they are almost equal in height.

**Z & D**

Since each informant's answer is weighted by competence, a reliable respondent may influence a question's consensus more. In the consensus graphs, the questions that are split are because the more competent informants are divided in their answers (e.g., Questions 4 and 12). If most competent respondents agree (e.g., Questions 0, 2, 3, 6, etc.), the bars will not be split, making only one visible (or taller). This illustrates how competence influences the consensus, as reflected in the graphs.



## GitHub Repo Link:

[(https://github.com/emelynochoaa/cct-midterm/tree/main/cct-midterm/data)]