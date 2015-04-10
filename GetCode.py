import sublime
import sublime_plugin


class GetSelectionCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if len(sel) > 0:
            charcode = ord(self.view.substr(sel[0].begin()))
            msg = "%d 0x%x" % (charcode, charcode)
            self.view.set_status("Char Code", "Char Code: " + msg + " ::   ")
            sublime.set_clipboard(msg)
