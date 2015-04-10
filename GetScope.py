import sublime
import sublime_plugin

def mkxml(text):
	return '''
			<dict>
				<key>name</key>
				<string>%s</string>
				<key>scope</key>
				<string>%s</string>
				<key>settings</key>
				<dict>
					<key>foreground</key>
					<string>#f00</string>
				</dict>
			</dict>
	''' %(text, text)


class GetSelectionScopeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if len(sel) > 0:
            msg = self.view.scope_name(sel[0].begin())
            self.view.set_status("Scope", "Scope: " + msg + " ::   ")
            sublime.set_clipboard(mkxml(msg))
