import json
from pprint import pprint as pp

from anki.hooks import addHook
from aqt.qt import *
from aqt import mw

addon_path = os.path.dirname(__file__)

def gc(arg, fail=False):
    conf = mw.addonManager.getConfig(__name__)
    if conf:
        return conf.get(arg, fail)
    else:
        return fail

prefix = '<code class="c-mono">'
suffix = '</code>'

def wrap_mono(editor):
    selection = editor.web.selectedText()
    html = """{0}{1}{2}""".format(prefix, selection, suffix)
    editor.web.eval(
            "document.execCommand('insertHTML', false, %s);"
            % json.dumps(html))

def setupEditorButtonsFilter(buttons, editor):
    key = QKeySequence(gc('Key_wrap_mono'))
    keyStr = key.toString(QKeySequence.SequenceFormat.NativeText)
    if gc('Key_wrap_mono'):
        b = editor.addButton(
            os.path.join(addon_path, "icons", "source-code.png"),
            "monobutton",
            wrap_mono,
            tip="Warp text to monospace ({})".format(keyStr),
            keys=gc('Key_wrap_mono')
            )
        buttons.append(b)
    return buttons

addHook("setupEditorButtons", setupEditorButtonsFilter)
