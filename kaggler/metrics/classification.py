from __future__ import division
from sklearn.metrics import roc_auc_score as auc
from sklearn.metrics import log_loss


from ..const import EPS


def logloss(y, p):
    """Bounded log loss error.

    Args:
        y (numpy.array): target
        p (numpy.array): prediction

    Returns:
        bounded log loss error
    """

    p[p < EPS] = EPS
    p[p > 1 - EPS] = 1 - EPS
    return log_loss(y, p)
