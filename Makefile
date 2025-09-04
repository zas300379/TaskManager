.PHONY: docker test logs stop clean help

help:
	@echo "Available commands:"
	@echo "  make docker    - Start Docker"
	@echo "  make test      - Run tests"
	@echo "  make logs      - View logs"
	@echo "  make stop      - Stop Docker"
	@echo "  make clean     - Clean up"

docker:
	@./scripts/start-docker.sh

test:
	@./scripts/test.sh

logs:
	@docker-compose logs -f

stop:
	@./scripts/stop-docker.sh

clean:
	@./scripts/cleanup.sh