# CCT Midterm - Emelyn Ochoa

## Objective

This project implements the basic Cultural Consensus Theory (CCT) model using PyMC to analyze plant knowledge data, estimating consensus answers and individual competence.

**Model**

The Cultural Consensus Theory (CCT) model was implemented using a Bernoulli likelihood. For informant competence (D), a Uniform prior (0.5 to 1) was chosen, reflecting knowledge better than chance. For consensus answers (Z), a non-informative Bernoulli(0.5) prior was used.

**Results (Raw Data)**

Posterior Mean Competence (D) for each Informant:
 
  Informant 1: 0.575

  Informant 2: 0.757

  Informant 3: 0.561

  Informant 4: 0.568

  Informant 5: 0.800

  Informant 6: 0.872

  Informant 7: 0.686

  Informant 8: 0.700

  Informant 9: 0.564

  Informant 10: 0.570


Posterior Mean for each Consensus Answer (Z):

  Item 1: Mean = 0.013, Estimated Consensus = 0

  Item 2: Mean = 0.825, Estimated Consensus = 1

  Item 3: Mean = 0.990, Estimated Consensus = 1

  Item 4: Mean = 0.018, Estimated Consensus = 0

  Item 5: Mean = 0.581, Estimated Consensus = 1

  Item 6: Mean = 0.929, Estimated Consensus = 1

  Item 7: Mean = 0.998, Estimated Consensus = 1

  Item 8: Mean = 0.924, Estimated Consensus = 1

  Item 9: Mean = 0.972, Estimated Consensus = 1

  Item 10: Mean = 0.924, Estimated Consensus = 1

  Item 11: Mean = 0.985, Estimated Consensus = 1

  Item 12: Mean = 0.010, Estimated Consensus = 0

  Item 13: Mean = 0.284, Estimated Consensus = 0

  Item 14: Mean = 0.903, Estimated Consensus = 1

  Item 15: Mean = 0.276, Estimated Consensus = 0

  Item 16: Mean = 0.023, Estimated Consensus = 0

  Item 17: Mean = 0.009, Estimated Consensus = 0

  Item 18: Mean = 0.062, Estimated Consensus = 0

  Item 19: Mean = 0.029, Estimated Consensus = 0

  Item 20: Mean = 0.997, Estimated Consensus = 1


Majority Vote (raw data) for each item:
  Item 1: 0

  Item 2: 0

  Item 3: 1

  Item 4: 0

  Item 5: 1

  Item 6: 0

  Item 7: 1

  Item 8: 0

  Item 9: 1

  Item 10: 0

  Item 11: 1

  Item 12: 0

  Item 13: 0

  Item 14: 0

  Item 15: 0

  Item 16: 0

  Item 17: 0

  Item 18: 0

  Item 19: 0

  Item 20: 1
  

**Interpretation**

The model yielded posterior mean competence estimates ranging from 0.56 (Informant 3) to 0.87 (Informant 6), this suggests different levels of knowledge among the informants (regarding plant identification). The consensus answers, showed notable differences when compared to majority vote of the responses. For example, for Items 2, 6, 8, 10, and 14, the CCT model predicted a consensus answer of 1, while the majority vote was 0. These differences suggest that the CCT model, by taking into account competence, produces a consensus that's different from simply averaging all responses. Specifically, in these cases, the more competent informants (like Informant 6) likely showed a pattern of agreement on the answer that was not the most frequent response in the overall group. 

This shows the CCT model's ability to reveal a "correct" answer which might otherwise be hidden by the opinions of less "competent" individuals in a majority vote.

## Issues
-I was unable to succesfully produce the plots, therefore could not visualize the results. My report is based on the printed output [inserted above] 
-I also had difficulty installing all libraries so I created a second (different) enviroment to re-install packages.


## GitHub Repo Link:

[(https://github.com/emelynochoaa/cct-midterm/tree/main/cct-midterm/data)]