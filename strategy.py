"""Strategyの練習."""
# coding: utf-8


class TestScore():
    """商品知識テストのスコア."""

    def __init__(self, name=None, kanri=None, baibai=None):
        self.name = name
        self.kanri = kanri
        self.baibai = baibai


class TestChecker():
    """テストの結果をチェックしたい人."""

    def __init__(self, score_comparator):
        self.score_comparator = score_comparator

    def compare(self, test_score1, test_score2):
        return self.score_comparator.compare(test_score1, test_score2)


class ScoreComparator():
    """スコアを比較する人."""

    def compare(self, test_score1, test_score2):
        raise NotImplementedError()


class KanriScoreComparator(ScoreComparator):
    """管理のスコアを比較する人."""

    def compare(self, test_score1, test_score2):
        if test_score1.kanri > test_score2.kanri:
            return test_score1.name
        if test_score1.kanri < test_score2.kanri:
            return test_score2.name
        return "引き分け"


class BaibaiScoreComparator(ScoreComparator):
    """売買のスコアを比較する人."""

    def compare(self, test_score1, test_score2):
        if test_score1.baibai > test_score2.baibai:
            return test_score1.name
        if test_score1.baibai < test_score2.baibai:
            return test_score2.name
        return "引き分け"


class TotalScoreComparator(ScoreComparator):
    """合計スコアを比較する人."""

    def compare(self, test_score1, test_score2):
        total_score1 = test_score1.kanri + test_score1.baibai
        total_score2 = test_score2.kanri + test_score2.baibai

        if total_score1 > total_score2:
            return test_score1.name
        if total_score1 < total_score2:
            return test_score2.name
        return "引き分け"


if __name__ == '__main__':
    tada_score = TestScore('Tada', 90, 82)
    kanehira_score = TestScore('Kanehira', 84, 100)

    shimada = TestChecker(KanriScoreComparator())
    print(shimada.compare(tada_score, kanehira_score))

    saiki = TestChecker(BaibaiScoreComparator())
    print(saiki.compare(tada_score, kanehira_score))

    ueki = TestChecker(TotalScoreComparator())
    print(ueki.compare(tada_score, kanehira_score))
