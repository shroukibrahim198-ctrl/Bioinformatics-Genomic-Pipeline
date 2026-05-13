import os
import subprocess

def run_full_pipeline():
    print("====================================================")
    print("   STARTING BIOINFORMATICS ANALYSIS PIPELINE       ")
    print("====================================================\n")

    # 1. تشغيل كود الفلترة والتحليل
    print("[1/2] Running Data Filtering and QC Analysis...")
    try:
        # بنشغل ملف filtering.py اللي جوه src
        subprocess.run(["python", "src/filtering.py"], check=True)
        print("✅ Data analysis completed successfully.\n")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return

    # 2. تشغيل كود الرسومات البيانية
    print("[2/2] Generating Visualization Plots...")
    try:
        # بنشغل ملف generate_plots.py اللي جوه results/plots
        subprocess.run(["python", "results/plots/generate_plots.py"], check=True)
        print("✅ Plots generated successfully.\n")
    except Exception as e:
        print(f"❌ Error during visualization: {e}")

    print("====================================================")
    print("   PIPELINE FINISHED! ALL RESULTS ARE READY.       ")
    print("====================================================")

if __name__ == "__main__":
    run_full_pipeline()