"""
Test script to verify Streamlit pages structure
"""
import os
from pathlib import Path

def test_structure():
    """Test if pages structure is correct"""
    base_path = Path(__file__).parent
    pages_dir = base_path / "pages"
    app_file = base_path / "app.py"
    
    print("=" * 60)
    print("Testing Streamlit Pages Structure")
    print("=" * 60)
    
    # Check app.py exists
    if app_file.exists():
        print(f"✅ app.py exists: {app_file}")
    else:
        print(f"❌ app.py not found!")
        return False
    
    # Check pages directory
    if not pages_dir.exists():
        print("❌ pages/ directory not found!")
        return False
    
    print(f"✅ pages/ directory exists: {pages_dir}")
    
    # List Python files in pages
    py_files = list(pages_dir.glob("*.py"))
    print(f"\n📄 Found {len(py_files)} Python files in pages/ directory:")
    
    for py_file in sorted(py_files):
        print(f"  - {py_file.name}")
        
        # Check if file has st.set_page_config
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'st.set_page_config' in content:
                    print(f"    ✅ Has st.set_page_config")
                else:
                    print(f"    ⚠️  Missing st.set_page_config")
        except Exception as e:
            print(f"    ❌ Error reading file: {e}")
    
    print("\n" + "=" * 60)
    print("Structure Check Complete!")
    print("=" * 60)
    print("\n💡 Troubleshooting:")
    print("   1. Make sure to restart Streamlit: streamlit run app.py")
    print("   2. Clear browser cache or use incognito mode")
    print("   3. On Streamlit Cloud: Reboot the app after deploying")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_structure()

