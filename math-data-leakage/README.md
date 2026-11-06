# Data Leakage

Advanced | data-processing

### The problem, from first principles

Imagine building a model to predict whether a hospital patient will be readmitted, and one of your "input" features happens to be `discharge_summary_mentions_followup_scheduled`, a note that only gets written AFTER a doctor already knows the patient's outcome. Train on this feature and you'll see suspiciously, almost impossibly good accuracy, because the model isn't predicting the future, it's reading an answer that was written down after the fact. This is **data leakage**: information that wouldn't actually be available at real prediction time has snuck into the training data, making the model look far better than it will ever perform in the real world.

`03-correlation-matrix`'s own Theory flagged exactly this trap in passing; this question builds the actual detection tool: an automatable, first-pass check that flags any feature suspiciously, almost implausibly correlated with the target, the numerical fingerprint leakage very often leaves behind.

### From theory to code

Theory reuses `03-probability/03-covariance-correlation`'s correlation, applied between every feature and the target specifically (not between features, `03-correlation-matrix`'s job) and flags anything above a high threshold as suspicious.

Implement `feature_target_correlations(x, target)` first, then `find_suspicious_features(x, target, threshold=0.95)` on top of it.

### Constraints

- `x` is `(num_samples, num_features)`, `target` is `(num_samples,)`.
- `find_suspicious_features` returns the INDICES of flagged features (an array of ints), not a boolean mask.
- `threshold` compares against absolute correlation (a suspiciously strong NEGATIVE correlation counts too).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`feature_target_correlations` loops over each feature column, computing `correlation(x[:, i], target)` for each and collects the results into an array.

</details>

<details>
<summary>Hint 2</summary>

`np.where(np.abs(correlations) > threshold)[0]` gives you exactly the indices where a condition holds.

</details>
