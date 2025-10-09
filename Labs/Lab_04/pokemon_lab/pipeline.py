import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Starting Production Pipeline", file=sys.stderr)
    print("Updating portfolio...", file=sys.stderr)
    update_portfolio.main()
    print("Generating summary...", file=sys.stderr)
    generate_summary.main()
    print("Pipeline Complete", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()