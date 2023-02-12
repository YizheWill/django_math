build:
	docker build -t django-math .

run:
	docker run --rm -p 8000:8000 -v "$(PWD):/app" django-math
