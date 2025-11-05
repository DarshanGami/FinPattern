#!/usr/bin/env python3
"""
Main runner script for trading pattern analysis
Provides an interactive menu to run different analyses
"""

import os
import sys
import subprocess

def print_banner():
    print("=" * 70)
    print(" " * 15 + "TRADING PATTERN ANALYSIS TOOL")
    print("=" * 70)
    print()

def print_menu():
    print("\nSelect an option:")
    print()
    print("  1. Generate Head & Shoulder patterns only")
    print("  2. Generate ALL trading patterns (9 charts)")
    print("  3. View pattern guide documentation")
    print("  4. Open outputs folder")
    print("  5. Exit")
    print()

def run_script(script_name):
    """Run a visualization script"""
    script_path = os.path.join('scripts', script_name)
    if not os.path.exists(script_path):
        print(f"❌ Error: Script not found: {script_path}")
        return False
    
    print(f"\n🚀 Running {script_name}...")
    print("-" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            check=True,
            capture_output=False,
            text=True
        )
        print("-" * 70)
        print("✅ Analysis completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print("-" * 70)
        print(f"❌ Error running script: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Analysis interrupted by user")
        return False

def view_documentation():
    """Display the pattern guide"""
    doc_path = os.path.join('docs', 'PATTERNS_GUIDE.md')
    if os.path.exists(doc_path):
        print("\n📖 Pattern Guide:")
        print("-" * 70)
        with open(doc_path, 'r') as f:
            content = f.read()
            # Print first 50 lines
            lines = content.split('\n')[:50]
            print('\n'.join(lines))
            if len(content.split('\n')) > 50:
                print("\n... (see docs/PATTERNS_GUIDE.md for full documentation)")
        print("-" * 70)
    else:
        print("❌ Documentation not found")

def open_outputs():
    """Open outputs directory"""
    output_dir = 'outputs'
    if os.path.exists(output_dir):
        files = [f for f in os.listdir(output_dir) if f.endswith('.png')]
        if files:
            print(f"\n📁 Output files in '{output_dir}':")
            for f in sorted(files):
                print(f"  - {f}")
            print(f"\nTotal: {len(files)} chart(s) generated")
        else:
            print(f"\n📁 '{output_dir}' directory is empty. Run an analysis first!")
    else:
        print(f"\n📁 '{output_dir}' directory doesn't exist yet. Run an analysis first!")

def main():
    print_banner()
    
    # # Check if virtual environment is activated
    # if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    #     print("⚠️  Warning: Virtual environment not activated")
    #     print("   Run: source patscanx/bin/activate")
    #     print()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                run_script('visualize_head_shoulder.py')
                
            elif choice == '2':
                run_script('visualize_all_patterns.py')
                
            elif choice == '3':
                view_documentation()
                
            elif choice == '4':
                open_outputs()
                
            elif choice == '5':
                print("\n👋 Goodbye! Happy trading!")
                sys.exit(0)
                
            else:
                print("\n❌ Invalid choice. Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy trading!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()

