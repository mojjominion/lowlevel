p=""

test-design-patterns: 
	python3 -m unittest discover -v ./design_patterns ${p}

test-ds: 
	python3 -m unittest discover -v ./data_structures ${p}
