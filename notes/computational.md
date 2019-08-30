# Computational methods structure

## Introduction

- Provide context on the importance of computational chemistry and how it can support experiment

## Atomistic modelling

- Evaluate forces
- Pros and cons versus ab initio techniques

### Interatomic potentials

- General introduction to the concept of a potential model
- System can be described as the sum of zero through n body terms
- We typically truncate to low body terms
  - This is less expensive
  - Also, it is difficult to concieve of a equation form which might be used to express a meaningful 15 boody interaction
- Two body terms are generally subdivided into the short range and long range (coulombic)
  - In this work, the Buckingham potential is used, although it is noted that some of the problems encountered may be more easily solved using another potential form
  - A potential form can be thought of as trying to capture some physical behaviour in a simplified and calculable manner. Such forms must be 