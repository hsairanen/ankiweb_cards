try:
	import aqt  # only present when running inside Anki
except Exception:
	# Skip auto-setup when running in test or non-Anki environments
	pass
else:
	from .ui.menu_setup import setup

	setup()