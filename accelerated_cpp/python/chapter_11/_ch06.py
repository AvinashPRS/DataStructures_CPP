# Load chapter 6's analysis functions. This chapter's own grade/median
# modules shadow chapter 6's because this directory comes first on sys.path.
from _paths import use_chapter

use_chapter(6)
import analysis  # noqa: E402,F401
