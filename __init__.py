from anki.hooks import wrap
from aqt import reviewer, clayout, previewer

# NOTE This may cause a double refresh every 100 reps?
def refreshReviewerWebView(self):
    if self.card:
        self._initWeb()
reviewer.Reviewer.nextCard = wrap(reviewer.Reviewer.nextCard, refreshReviewerWebView, 'before')

# TODO This causes weird formatting on the back
#reviewer.Reviewer._showAnswer = wrap(reviewer.Reviewer._showAnswer, refreshWebView, 'before')

def refreshClayoutWebView(self):
    self.preview_web.stdHtml(
        self.mw.reviewer.revHtml(),
        css=["css/reviewer.css"],
        js=[
            "js/mathjax.js",
            "js/vendor/mathjax/tex-chtml.js",
            "js/reviewer.js",
        ],
        context=self,
    )
clayout.CardLayout._renderPreview = wrap(clayout.CardLayout._renderPreview, refreshClayoutWebView, 'before')

previewer.Previewer.render_card = wrap(previewer.Previewer.render_card, previewer.Previewer._setup_web_view, 'before')