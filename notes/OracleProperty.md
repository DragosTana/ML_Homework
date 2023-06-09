# Oracle Property

## Definition

The oracle property is a desirable property for an estimator in the context of **high-dimensional regression**. The idea behind this property is that the **estimator has the ability to correctly identify which predictors are relevant** (i.e., have non-zero coefficients) and which are irrelevant (i.e., have zero coefficients).

More specifically, for an estimator to have the oracle property, it must satisfy the following two conditions:

**Consistency**: The estimator must converge to the true coefficients as the sample size increases, even in high-dimensional settings.

**Asymptotic selection consistency**: The estimator must correctly identify the relevant predictors with probability tending to one as the sample size increases, even in high-dimensional settings.

The second condition means that as the number of predictors increases relative to the sample size, the estimator must still be able to identify the relevant predictors with high probability. In other words, **the estimator should be able to separate signal from noise and distinguish the predictors that actually contribute to the outcome variable from those that do not.**

OLS does not have the oracle property because it is not well-suited for high-dimensional settings. In high-dimensional settings, the number of predictors can be much larger than the sample size, which violates the assumptions underlying OLS. On the other hand, some regularized estimators such as the Lasso and the Elastic Net have been shown to have the oracle property under certain conditions. These estimators are designed to handle high-dimensional settings and have been shown to be effective in correctly identifying the relevant predictors even when the number of predictors is much larger than the sample size.

## Conditions under which lasso and elastic net have oracle property

The conditions for Lasso to have the oracle property are:

1. **Sparsity**: The true model has only a few non-zero coefficients, i.e., it is sparse.

2. **Irrepresentable Condition**: This condition essentially states that the correlation between any two predictors in the model should not be too high. In other words, the true model should not have strong multicollinearity.

3. **Cone Condition**: This condition is a bit technical and involves the geometry of the solution space. It essentially states that the solution vector obtained from Lasso regression should lie within a certain cone-shaped region that is centered at the true solution vector.

Similarly, the conditions for Elastic Net to have the oracle property are:

1. **Sparsity**: The true model has only a few non-zero coefficients, i.e., it is sparse.

2. **Irrepresentable Condition**: This condition is the same as for Lasso, i.e., the true model should not have strong multicollinearity.

3. **Restricted Eigenvalue Condition**: This condition is a bit different from the Cone Condition for Lasso. It essentially states that the matrix of predictor variables should have certain properties that ensure that the Elastic Net solution lies within a certain neighborhood of the true solution. This condition is stronger than the Cone Condition, and requires that the matrix satisfies certain properties related to the smallest eigenvalue of the matrix.
