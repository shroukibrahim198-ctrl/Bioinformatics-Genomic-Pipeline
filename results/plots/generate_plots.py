import matplotlib
matplotlib.use('Agg') # عشان يشتغل في الخلفية بدون مشاكل
import matplotlib.pyplot as plt
import os

def save_project_plots():
    try:
        # الأرقام اللي طلعتلك في التقرير النهائي
        labels = ['Health Sample', 'Cancer Sample']
        q30_scores = [94.48, 94.06] 
        gc_content = [50.04, 49.98] 

        # 1. رسمة الـ Q30 Percentage
        plt.figure(figsize=(6, 4))
        plt.bar(labels, q30_scores, color=['#5DADE2', '#EC7063'])
        plt.title('Quality Score (Q30) Comparison')
        plt.ylabel('Percentage %')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # حفظ الصورة في نفس الفولدر اللي فيه الكود حالياً
        plt.savefig('q30_analysis.png')
        plt.close()
        print("✅ Success: q30_analysis.png saved!")

        # 2. رسمة الـ GC Content
        plt.figure(figsize=(6, 4))
        plt.bar(labels, gc_content, color=['#58D68D', '#F4D03F'])
        plt.title('GC Content Analysis')
        plt.ylabel('Percentage %')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # حفظ الصورة الثانية في نفس الفولدر
        plt.savefig('gc_analysis.png')
        plt.close()
        print("✅ Success: gc_analysis.png saved!")
        
        print("\nAll plots are now inside: results/plots/")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    save_project_plots()