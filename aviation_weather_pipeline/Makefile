.PHONY: all fetch analyze clean

analyze: fetch
	@echo "Starting analysis of METAR"
	./analyze_data.sh
	@echo "Finished Analysis of METAR. CSV is in weather_report.csv"

fetch:
	@echo "Fetching METAR Data"
	./fetch_metars.sh
	@echo "Finished Fetching METAR data. Check raw_metars/ to see data from airports"

clean:
	@echo "Cleaning generated data"
	rm -rf raw_metars/ weather_report.csv
	@echo "Clean complete, all generated files removed"

all: analyze
