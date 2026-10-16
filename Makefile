.PHONY: research-status research-verify research-source-gp200jr research-commit-gp200jr

research-status:
	python3 scripts/research_tools.py status

research-verify:
	python3 scripts/research_tools.py verify

research-source-gp200jr:
	python3 scripts/research_tools.py gp200jr

.PHONY: research-render-gp200jr
research-render-gp200jr:
	python3 scripts/research_tools.py render-gp200jr

research-commit-gp200jr:
	python3 scripts/research_tools.py commit-gp200jr
